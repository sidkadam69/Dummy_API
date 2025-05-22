from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
from app.model import classify

app = FastAPI(title="Dummy Classifier API")

class FeaturesInput(BaseModel):
    features: Annotated[list[float], Field(min_items=4, max_items=4)]

@app.post("/predict")
def predict(input_data: FeaturesInput):
    prediction = classify(input_data.features)
    return {"prediction": prediction}
