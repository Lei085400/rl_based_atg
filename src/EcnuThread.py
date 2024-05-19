import threading
import time
import json
import os

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
        file_path = "/home/ssm/Metamath/icml-deploy/data"
        file_name = "theorems/theorem00_13.jsonl"
        with open(os.path.join(file_path, file_name), 'r') as file:
            for _line in file.readlines():
                outputs.append(json.loads(_line))
                time.sleep(0.02)
