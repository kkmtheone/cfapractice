from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import random

app = FastAPI()

# serve static files (CSS/JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# templates
templates = Jinja2Templates(directory="app/templates")

# sample questions (later connect to DB)
QUESTIONS = [
    {
        "id": 1,
        "question": "What is the formula for the present value of a perpetuity?",
        "choices": [
            "PV = C / r",
            "PV = C × (1+r)^n",
            "PV = C / (1+r)^n",
            "PV = r / C"
        ],
        "answer": 0,
        "explanation": "The present value of a perpetuity is cash flow divided by the discount rate (PV = C / r)."
    },
    {
        "id": 2,
        "question": "Which financial statement reports a company’s assets and liabilities?",
        "choices": [
            "Income Statement",
            "Cash Flow Statement",
            "Balance Sheet",
            "Statement of Retained Earnings"
        ],
        "answer": 2,
        "explanation": "The balance sheet reports assets, liabilities, and equity at a point in time."
    }
]

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # pick random question for demo
    q = random.choice(QUESTIONS)
    return templates.TemplateResponse("index.html", {"request": request, "question": q})
