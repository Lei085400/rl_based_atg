import time
import urllib.request
import json
from submission import *


submission = Submission("/root/icml-deploy/outputs/output.jsonl")
axioms_path = "../data/axioms.jsonl"
symbols_path = "../data/symbols.jsonl"
submission.run(axioms_path, symbols_path)