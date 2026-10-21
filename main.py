from fastapi import FastAPI
from pydantic import BaseModel, Field
from llm_client import generate_text

app = FastAPI(title="InferScope")

@app.get("/health")
def health_check():
    return {"status": "healthy"}

class GenerateRequest(BaseModel):
    prompt : str = Field(min_length=1)

@app.post("/generate")
async def generate(request: GenerateRequest):
    base_url = "http://localhost:8001"
    result = await generate_text(request.prompt, base_url)
    return result   