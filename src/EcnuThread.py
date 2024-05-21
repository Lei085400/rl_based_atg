import threading
import time
import json
import os
from string import Template
import torch
import mmverify
from model import policy_model
from model import value_model
from mcts import Node
from mcts import MCTS
# from verify import anatomy
import openai
from tqdm import tqdm

from loguru import logger
logger.remove()
logger.add("../logs/{time}.log")

axioms = [] # 引理文件
symbols = [] # 符号文件
outputs = [] # 生成的定理文件，子元素为比赛要求的json格式的定理

class EcnuThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        # self.threadID = threadID
        # self.name = name
        # self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面, 线程在创建后会直接运行run函数
        file_path = "/root/icml-deploy/data"
        file_name = "theorems/theorem00_13.json"
        with open(os.path.join(file_path, file_name), 'r') as file:
            for json_item in json.load(file):
                if json_item["theorem"] in {"weq", "wl-impchain-mp-0", "e0a"}:
                    continue
                outputs.append(json_item)
                
        file_name = "theorem01_15.json"
        with open(os.path.join(file_path, file_name), 'r') as file:
            for json_item in json.load(file):
                if json_item["theorem"] in {"eel0cT", "H15NH16TH15IH16", "sptruw"}:
                    continue
                outputs.append(json_item)
        
        
        return
        
        axiom_file = "/root/icml-deploy/data/axioms.jsonl"   
        symbol_file = "/root/icml-deploy/data/symbols.jsonl"
        
        device = torch.device('cpu') 

        args = {
            'batch_size': 10,
            'numIters': 1,                                # Total number of training iterations
            'num_simulations': 100,                         # Total number of MCTS simulations to run when deciding on a move to play
            'numEps': 50,                                  # Number of full games (episodes) to run during each iteration
            'numItersForTrainExamplesHistory': 20,
            'epochs': 15,                                    # Number of epochs of training per iteration
            'checkpoint_path': 'latest.pth',                 # location to save latest set of weights
            'TACRIC_NUMBER': 5,
            'feature_size':100,
            'axiom_file':axiom_file,
            'symbol_file':symbol_file
            # 'MAX_ROUND_NUMBER' : 10
        }


        policyModel = policy_model(args['feature_size']*2, device)
        valueModel = value_model(args['feature_size'], device)
    
        checkpoint_policy = torch.load("policy_model")
        policyModel.load_state_dict(checkpoint_policy['state_dict'])

        checkpoint_value = torch.load("value_model")
        valueModel.load_state_dict(checkpoint_value['state_dict'])

        # anatomy(axiom_file,symbol_file)
        verbosity = 30

        filename='Declare.mm'

        # 假设这里的mm文件 没有证明序列，没有要证明的断言，只读入声明 (文件最后一个字符是 $=),
        mm = mmverify.MM(None,None)
        f_hyps,e_hyps = mm.calculate_and_verify_metamath(filename,def_verbosity=verbosity,def_only_calculate=True) #只使用计算功能
        step_int = 0
        state = []
        step = ''
        # 先调用一遍，初始化标签
        correct_flag,state = mm.verify_and_calculate_proof_step_normal(f_hyps,e_hyps,step,state,step_int) 

        
        node = Node(state)
        node.flag = correct_flag

        print("开始搜索")
        mcts = MCTS(node, policyModel, valueModel, args, device)
        new_theorems = mcts.runmcts(mm, f_hyps, e_hyps, axiom_file,symbol_file)
        outputs.extend(new_theorems)
        # logger.info(str(outputs))
        