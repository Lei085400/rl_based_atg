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
        file_path = "/root/icml-deploy/data"
        file_name = "theorems/theorem00_13.json"
        with open(os.path.join(file_path, file_name), 'r') as file:
            for json_item in json.load(file):
                if json_item["theorem"] not in {"theorem0", "theorem1"}:
                    continue
                outputs.append(json_item)
