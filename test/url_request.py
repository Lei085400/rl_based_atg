import time

# import requests
import urllib.request
import json

from submission import *

submission = Submission("D:\PyCharmFile\ReinLearning\ActorCrital\output.jsonl")
axioms_path = "axioms.jsonl"
symbols_path = "symbols.jsonl"
submission.base_url = "http://101.200.56.238"
submission.port = 11451
submission.run(axioms_path, symbols_path)

exit(0)


headers = {"Content-Type": "application/json"}

url = "http://127.0.0.1:8000/axioms_and_symbols"
url2 = "http://127.0.0.1:8000/get_one_theorem/"



def load_axioms(path):
    axioms = []
    with open(path, "r+") as file:
        for _line in file.readlines():
            axioms.append(json.loads(_line))

    return axioms


def load_symbols(path):
    symbols = []
    with open(path, "r+") as file:
        for _line in file.readlines():
            symbols.append(json.loads(_line))

    return symbols


axioms = load_axioms(axioms_path)
symbols = load_symbols(symbols_path)

data = {"axioms": axioms, "symbols": symbols}

request = urllib.request.Request(url=url, data=json.dumps(data).encode(), headers=headers, method="POST")
repose = urllib.request.urlopen(request, ).read()
print(type(repose), repose.decode())
