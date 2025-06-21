from fastapi import FastAPI
from app.routes import router
from app.database import create_index

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    await create_index()
