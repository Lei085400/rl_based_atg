"""DO NOT rename this file!"""
import os
import json
import textwrap
import time
import urllib.request

class Submission:

    def __init__(self, output_file: str):
        """You need to specify the following arguments."""
        self.output_file = output_file
        self.base_url = "http://101.200.56.238"  # The base url of the model server
        self.port = 11451
        self.timeout = 5.0
        self.all_time_limit = 300.0
        self.ask_time_gap = 5.0


    def generate(self, prompt):

        return 1

    def post_axioms_ans_symbols(self, axioms, symbols):
        url = self.base_url + ":" + str(self.port) + "/axioms_and_symbols"
        headers = {"Content-Type": "application/json"}
        data = {"axioms": axioms, "symbols": symbols}
        request = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers=headers, method="POST")
        repose = urllib.request.urlopen(request, timeout=self.timeout).read()
        return json.loads(repose.decode())

    def post_theorems(self, idx):
        url = self.base_url + ":" + str(self.port) + "/post_theorems/" + str(idx)
        headers = {"Content-Type": "application/json"}
        request = urllib.request.Request(url=url, headers=headers, method="POST")
        repose = urllib.request.urlopen(request, timeout=self.timeout).read()
        return json.loads(repose.decode())

    def run(self, axiom_file: str, symbol_file: str):
        axioms, symbols = [], []

        with open(axiom_file, 'r', encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                axiom = json.loads(line)
                axioms.append(axiom)

        with open(symbol_file, 'r', encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                symbol = json.loads(line)
                symbols.append(symbol)

        repose = self.post_axioms_ans_symbols(axioms, symbols)
        assert repose["response"] == "have received axioms and symbols", "axioms error!"

        outputs = []
        start_time = time.time()
        while time.time() - start_time <= self.all_time_limit:
            time.sleep(self.ask_time_gap)
            try:
                new_theorems = self.post_theorems(len(outputs))["response"]

                if new_theorems == "please wait": continue
                elif new_theorems == "over": break
                else:
                    outputs.extend(json.loads(new_theorems))

            except Exception as ex:
                ex.with_traceback()

        if not os.path.exists(self.output_file):
            os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
        with open(self.output_file, 'w+', encoding='utf8') as f:
            for output in outputs:
                f.write(json.dumps(output))
                f.write('\n')
