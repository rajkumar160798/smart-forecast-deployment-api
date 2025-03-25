# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
from .forecast_utils import generate_forecast

app = FastAPI()

# Input schema
class ForecastRequest(BaseModel):
    start_date: str  # e.g., "2024-04-01 00:00:00"
    periods: int     # Number of future hours to predict

# Output schema
class ForecastPoint(BaseModel):
    ds: str
    yhat: float
    failure_risk: bool

class ForecastResponse(BaseModel):
    forecast: List[ForecastPoint]

@app.post("/predict", response_model=ForecastResponse)
def predict(request: ForecastRequest):
    try:
        forecast_df = generate_forecast(request.start_date, request.periods)
        response = [
            ForecastPoint(
                ds=row.ds.strftime("%Y-%m-%d %H:%M:%S"),
                yhat=round(row.yhat, 2),
                failure_risk=row.yhat > 78
            ) for row in forecast_df.itertuples()
        ]
        return {"forecast": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
