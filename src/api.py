import json
from fastapi import FastAPI, Request
from EcnuThread import EcnuThread, axioms, symbols, outputs
from loguru import logger

logger.remove()
logger.add("../logs/{time}.log")

app = FastAPI() # 部署的对象

ecnu_thread = EcnuThread() # 获取引理和符号后启动的线程

@app.post("/axioms_and_symbols")
async def get_axioms_and_symbols(request: Request):
    data = await request.json()
    axioms = data["axioms"]
    symbols = data["symbols"]

    logger.info("receive axioms and symbols:")
    logger.info(str(axioms) + "")
    logger.info(str(symbols) + "\n")

    ecnu_thread.start()

    logger.info("response: have received axioms and symbols")
    return {"response": "have received axioms and symbols"}


@app.post("/post_theorems/{idx}")
async def get_one_theorem(idx: int):
    logger.info(f"receive ask for idx {idx}")

    if len(outputs) <= idx:
        if ecnu_thread.is_alive():

            logger.info("response: please wait")
            return {"response": "please wait"}
        else:
            logger.info("response: over")
            return {"response": "over"}
    logger.info("response: \n" + json.dumps(outputs[idx:]))
    return {"response": json.dumps(outputs[idx:])}