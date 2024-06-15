import json
from fastapi import FastAPI, Request
from EcnuThread import *



app = FastAPI() # 部署的对象

thread_list = []



@app.post("/axioms_and_symbols")
async def get_axioms_and_symbols(request: Request):
    axioms.clear()
    symbols.clear()
    outputs.clear()
    
    
    data = await request.json()
    axioms.extend(data["axioms"])
    symbols.extend(data["symbols"])

    axiom_file = "../data/temp_axioms.jsonl"   
    symbol_file = "../data/temp_symbols.jsonl"

    with open(axiom_file, 'w') as file:
        for _item in axioms:
            file.write(json.dumps(_item) + "\n")

    with open(symbol_file, 'w') as file:
        for _item in symbols:
            file.write(json.dumps(_item) + "\n")

    logger.info("receive axioms and symbols:")
    logger.info(str(axioms) + "")
    logger.info(str(symbols) + "\n")

    ecnu_thread = EcnuThread()
    thread_list.append(ecnu_thread)
    ecnu_thread.start()

    logger.info("response: have received axioms and symbols")
    return {"response": "have received axioms and symbols"}


@app.post("/post_theorems/{idx}")
async def get_one_theorem(idx: int):
    logger.info(f"receive ask for idx {idx}")

    if len(outputs) <= idx:
        if thread_list[-1].is_alive():

            logger.info("response: please wait")
            return {"response": "please wait"}
        else:
            thread_list.pop()
            logger.info("response: over")
            return {"response": "over"}
    logger.info("response: \n" + json.dumps(outputs[idx:]))
    return {"response": json.dumps(outputs[idx:])}