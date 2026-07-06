from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

from app.version import VERSION


app = FastAPI(
    title="Calculator API",
    version=VERSION
)

templates = Jinja2Templates(directory="templates")

class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "version": VERSION
        }
    )


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
    
@app.get("/calculate-ui")
def calculate_ui(a: float, b: float, operation: str):
    operation = operation.lower()

    if operation == "add":
        result = a + b

    elif operation == "subtract":
        result = a - b

    elif operation == "multiply":
        result = a * b

    elif operation == "divide":
        if b == 0:
            raise HTTPException(
                status_code=400,
                detail="Division by zero is not allowed"
            )
        result = a / b

    else:
        raise HTTPException(
            status_code=400,
            detail="Unsupported operation"
        )

    return {"result": result}
