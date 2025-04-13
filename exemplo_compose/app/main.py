from fastapi import FastAPI
from sqlalchemy import create_engine

import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + PostgreSQL funcionando!"}
