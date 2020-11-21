from typing import Optional
from fastapi import FastAPI
from src.service import service as sv
app = FastAPI()


@app.get("/prediction")
def predict_cost(q: Optional[str] = None):
    return {"data": q}