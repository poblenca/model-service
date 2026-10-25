from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="model-service")


class PredictRequest(BaseModel):
    features: list[float] = Field(min_length=1)


class PredictResponse(BaseModel):
    prediction: float
    model_version: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    # placeholder model: the average of the features
    result = sum(req.features) / len(req.features)
    return PredictResponse(prediction=result, model_version="dummy-0.1")
