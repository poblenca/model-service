from fastapi import FastAPI

app = FastAPI(title="model-service")


@app.get("/health")
def health():
    return {"status": "ok"}
