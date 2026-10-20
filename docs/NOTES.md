# InferScope — Learning Notes

## Concepts
## Interview Questions
## Debugging & Lessons

## FastAPI & Uvicorn
- FastAPI: Defines API endpoints and request handling
- Uvicorn: ASGI server that runs our application
- `@app.get("/health")`: Maps GET requests to a Python function.
- `/health`: Endpoint used to check service availability.

## Debugging & Lessons

- ModuleNotFoundError: Python couldnt locate main.py
- Fix: 'uv run python -m pytest -v' 
- Running pytest with 'python -m' includes the current directory in the import path