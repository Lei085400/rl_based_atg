import json
import os

class Translator:
    def __init__(self):
        
        self.translations = []
        self.outputs = {'$p':{}, 
                        '$a':{}, 
                        '$f':{}}
    
    def load(self, filename):
        if filename.endswith('.json'):
            with open(filename, 'r') as f:
                self.translations.extend(json.load(f))
        elif filename.endswith('.jsonl'):
            with open(filename, 'r') as f:
                for line in f:
                    self.translations.append(json.loads(line))

        
    def _dump(self, s, w):
        s.extend(w)
        s.append('\n')

    def show(self):
        for theorem in self.translations:
            for k in theorem:
                print(k,":", theorem[k])
    
    def to_metamath_p(self, label, value, name) -> list:
        
        if label == 'theorem':
            sentence = [value]
            return sentence
        
        if label == 'type':
            return ['$p']
        
        if label == 'conclusion':
            return [value, '$=']
        
        if label == 'd_vars':
            if value:
                raise NotImplementedError('no implement for d_vars json to metamath sentence')

        if label == 'f_hypos':
            sentence = []
            # for v in value:
            #     v = v.split()
                
            #     if v[0] == 'wff':
            #         sentence.append('w' + v[1])
                    
            #     if v[0] == 'setvar':
            #         sentence.append('v' + v[1])
                
            #     sentence.append('$f')
            #     sentence.extend(v)
            #     sentence.append('$.\n')
            return sentence
        
        if label == 'e_hypos':
            sentence = []
            idx = 1
            for v in value:
                sentence.append(f'{name}.{idx}')
                sentence.append('$e')
                sentence.append(v)
                sentence.append('$.\n')
                idx += 1
            return sentence
        
        if label == 'proof_steps':
            return [value]
        
        if label == 'references':
            sentence = []
            if value:
                sentence = ['('] + value + [')']
            return sentence
        
    def dump_p(self, theorem):
        sentences = ['${\n']
        self._dump(sentences, theorem['f_hypos'])
        self._dump(sentences, theorem['e_hypos'])
        sentences.extend(theorem['theorem'])
        sentences.extend(theorem['type'])
        self._dump(sentences, theorem['conclusion'])
        sentences.extend(theorem['references'])
        sentences.extend(theorem['proof_steps'])
        sentences.append('$.')
        sentences.append('\n$}\n')
        
        self.outputs['$p'][theorem['theorem'][0]] = ' '.join(sentences)

    def to_metamath_a(self, label, value, name) -> list:
        if label == 'theorem':
            return [value]

        if label == 'type':
            return ['$a']
        
        if label == 'f_hypos':
            sentence = []
            # for v in value:
            #     v = v.split()
                
            #     if v[0] == 'wff':
            #         sentence.append('w' + v[1])
                    
            #     if v[0] == 'setvar':
            #         sentence.append('v' + v[1])
                
            #     sentence.append('$f')
            #     sentence.extend(v)
            #     sentence.append('$.\n')
            return sentence
        
        if label == 'e_hypos':
            sentence = []
            idx = 1
            for v in value:
                sentence.append(f'{name}.{idx}')
                sentence.append('$e')
                sentence.append(v)
                sentence.append('$.\n')
                idx += 1
            return sentence
        
        if label == 'conclusion':
            return [value]

        return []
    
    def dump_a(self, theorem):
        sentences = []
        sentences = ['${\n']
        self._dump(sentences, theorem['f_hypos'])
        self._dump(sentences, theorem['e_hypos'])
        sentences.extend(theorem['theorem'])
        sentences.append('$a')
        sentences.extend(theorem['conclusion'])
        sentences.append('$.\n')
        sentences.append('\n$}\n')

        self.outputs['$a'][theorem['theorem'][0]] = ' '.join(sentences)

    def to_metamath_f(self, label, value) -> list:
        if label == 'theorem':
            return [value]

        if label == 'type':
            return ['$f']
        
        if label == 'conclusion':
            return [value]

        return []

    def dump_f(self, theorem):
        sentences = []
        sentences.extend(theorem['theorem'])
        sentences.append('$f')
        sentences.extend(theorem['conclusion'])
        sentences.append('$.\n')
        
        self.outputs['$f'][theorem['theorem'][0]] = ' '.join(sentences)
    
    def translate(self):
        for theorem in self.translations:
            the_meta = {}
            theorem_name = theorem['theorem']
            for label, value in theorem.items():
                if theorem['type'] == '$p':
                    the_meta[label] = self.to_metamath_p(label, value, theorem_name)
                
                elif theorem['type'] == '$a':
                    the_meta[label] = self.to_metamath_a(label, value, theorem_name)

                elif theorem['type'] == '$f':
                    the_meta[label] = self.to_metamath_f(label, value)
            
            if theorem['type'] == '$p':
                self.dump_p(the_meta)
                
            elif theorem['type'] == '$a':
                self.dump_a(the_meta)

            elif theorem['type'] == '$f':
                self.dump_f(the_meta)
    
    def _output(self, out_dir, type, model):
        with open(out_dir, mode=model) as f:
            for v in self.outputs[type].values():
                f.write(v)
                f.write('\n')

    def output(self, out_dir):  
        self._output(out_dir, type='$f', model='a')
        self._output(out_dir, type='$a', model='a')
        self._output(out_dir, type='$p', model='a')
        
    
    def verify(self):
        translator.translate()
        filename = "test.mm"
        template_filename = "template.mm"
        with open(filename, 'w') as f:
            with open(template_filename, 'r') as t:
                for line in t.readlines():
                    f.write(line + "\n")
            
        
        self.output(out_dir=filename)

        verbosity = 5
        log_filename = f"{filename}-{verbosity}.log"
        
        try:
            os.system(f"python3 mmverify_zero.py {filename} --logfile {log_filename} -v {verbosity}")
        except Exception as e:
            e.with_traceback()
        
        stmt = ""
        with open(log_filename, 'r') as f:
            stmt = f.readlines()[-1]

        try:
            os.system(f"rm -rf {filename}")
            os.system(f"rm -rf {log_filename}")
        except Exception as e:
            e.with_traceback()

        return stmt == "No errors were found.\n"

    
if __name__ == "__main__":
    path = '../../data/'
    symbols_filename = 'symbols.jsonl'
    axioms_filename = 'axioms.jsonl'
    theorem_filenames = ['theorems/theorem00_13.json']
    

    translator = Translator()
    translator.load(path + symbols_filename)
    translator.load(path + axioms_filename)
    translator.load(path + theorem_filenames[0])
    # translator.load(path + theorem_filenames[1])
    
    print(translator.verify())
  
