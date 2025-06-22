from typing import Union

from fastapi import FastAPI
from util import item_value

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Sathish"}


@app.get("/list")
def read_item(item_id: int, name: Union[str] = None, age: int = None):
    response = item_value(item_id, name)
    response["age"] = age
    return response