from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Sathish"}


@app.get("/list")
def list_tasks():
    # your logic
