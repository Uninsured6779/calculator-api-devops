from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.version import VERSION

app = FastAPI(
    title="Calculator API",
    version=VERSION
)


class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/")
def root():
    return {
        "message": "Calculator API"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/version")
def version():
    return {
        "version": VERSION
    }


@app.post("/calculate")
def calculate(request: CalculationRequest):
    operation = request.operation.lower()

    if operation == "add":
        result = request.a + request.b

    elif operation == "subtract":
        result = request.a - request.b

    elif operation == "multiply":
        result = request.a * request.b

    elif operation == "divide":
        if request.b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )
        result = request.a / request.b

    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported operation"
        )

    return {
        "result": result
    }
