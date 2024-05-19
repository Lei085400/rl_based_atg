import time
import urllib.request
import json
from submission import *


submission = Submission("/home/ssm/Metamath/icml-deploy/outputs/output.jsonl")
axioms_path = "../data/axioms.jsonl"
symbols_path = "../data/symbols.jsonl"
submission.base_url = "http://127.0.0.1"
submission.port = 11451
submission.run(axioms_path, symbols_path)