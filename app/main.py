from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict


app = FastAPI()


class Input(BaseModel):
    adults: int
    children: int
    parking: int
    repeated_guest: int
    lead_time: int
    weekend: int
    weekday: int
    prev_cancel: int


class PredictionOut(BaseModel):
    is_canceled: int


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.post("/predict")
def WeatherResult(payload: Input):
    is_canceled = predict(payload.adults, payload.children, payload.parking, payload.repeated_guest, payload.lead_time, payload.weekend, payload.weekday, payload.prev_cancel)
    return {"Result": is_canceled}