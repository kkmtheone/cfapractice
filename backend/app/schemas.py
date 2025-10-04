from pydantic import BaseModel, EmailStr
from typing import Optional, List

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    is_premium: bool

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class QuestionCreate(BaseModel):
    topic: str
    level: str
    stem: str
    choices: List[str]
    correct_choice: int
    explanation: Optional[str] = None

class QuestionRead(BaseModel):
    id: int
    topic: str
    level: str
    stem: str
    choices: List[str]
    explanation: Optional[str] = None
