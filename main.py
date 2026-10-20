from fastapi import FastAPI

app = FastAPI(title="InferScope")

@app.get("/health")
def health_check():
    return {"status": "healthy"}