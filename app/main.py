from fastapi import FastAPI, HTTPException
from starlette.responses import Response

from app.db.models import Letters
from app.api import api

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Engie Fast API"}


@app.post("/convert", status_code=200)
def convert(payload: Letters):
    payload = payload.dict()

    return api.convert(payload)

