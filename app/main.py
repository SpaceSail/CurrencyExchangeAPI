from fastapi import FastAPI, Query
from .xml_get import calculate_cb
app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Hello World"}


@app.get("/api/rates")
async def root(source: str = Query(alias='from'),
               destination: str = Query(alias='to'),
               value: int = 1):
    rate = await calculate_cb(source, value, destination)
    return {'result': rate}
