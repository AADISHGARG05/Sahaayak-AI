# main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from pydantic import BaseModel
from app.predict_intent import predict_user_intent

app = FastAPI(
    title="Sahaayak – Emergency Assistant API",
    description="Multilingual emergency intent prediction system",
    version="1.0.0"
)

# Request body schema
class IntentRequest(BaseModel):
    text: str

# Root route
@app.get("/")
def read_root():
    return {"message": "🚑 Sahaayak API is running!"}

# Predict route
@app.post("/predict_intent/")
def predict_intent(request: IntentRequest):
    result = predict_user_intent(request.text)
    return result

# run by this
# python -m uvicorn main:app --reload



