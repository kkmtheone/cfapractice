from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, nullable=False, unique=True)
    hashed_password: str
    is_active: bool = True
    is_premium: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    topic: str
    level: str  # e.g. "L1", "L2", "L3"
    stem: str
    choices: str  # store JSON list as string
    correct_choice: int
    explanation: Optional[str] = None
    tags: Optional[str] = None
