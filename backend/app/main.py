from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import users, questions
from app.database import create_db_and_tables

app = FastAPI(title="CFA Practice API")

# Allow CORS (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Routers
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(questions.router, prefix="/api/v1/questions", tags=["questions"])

@app.get("/")
async def root():
    return {"msg": "CFA Practice API — up and running"}
