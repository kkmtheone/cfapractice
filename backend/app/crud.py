from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select
from app.models import User, Question
from passlib.context import CryptContext
from typing import List, Optional
import json

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(session: Session, email: str) -> Optional[User]:
    return session.exec(select(User).where(User.email == email)).first()

def create_user(session: Session, email: str, password: str) -> User:
    hashed = pwd_context.hash(password)
    user = User(email=email, hashed_password=hashed)
    session.add(user)
    try:
        session.commit()
        session.refresh(user)
    except IntegrityError:
        session.rollback()
        raise
    return user

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

def create_question(
    session: Session,
    topic: str,
    level: str,
    stem: str,
    choices: List[str],
    correct_choice: int,
    explanation: str = None,
) -> Question:
    q = Question(
        topic=topic,
        level=level,
        stem=stem,
        choices=json.dumps(choices),
        correct_choice=correct_choice,
        explanation=explanation
    )
    session.add(q)
    session.commit()
    session.refresh(q)
    return q

def get_questions(session: Session, topic: Optional[str] = None) -> List[Question]:
    statement = select(Question)
    if topic:
        statement = statement.where(Question.topic == topic)
    return session.exec(statement).all()
