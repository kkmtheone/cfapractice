from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
import json

from app.database import get_session
from app import crud
from app.models import Question
from app.schemas import QuestionRead

router = APIRouter()

@router.get("/", response_model=List[QuestionRead])
def list_questions(session: Session = Depends(get_session)):
    questions = crud.get_questions(session)
    result = []
    for q in questions:
        result.append(
            QuestionRead(
                id=q.id,
                topic=q.topic,
                level=q.level,
                stem=q.stem,
                choices=json.loads(q.choices),
                explanation=q.explanation,
            )
        )
    return result

@router.post("/", response_model=QuestionRead)
def create_question(question: QuestionRead, session: Session = Depends(get_session)):
    q = crud.create_question(
        session,
        topic=question.topic,
        level=question.level,
        stem=question.stem,
        choices=question.choices,
        correct_choice=0,  # for now, default placeholder
        explanation=question.explanation,
    )
    return QuestionRead(
        id=q.id,
        topic=q.topic,
        level=q.level,
        stem=q.stem,
        choices=json.loads(q.choices),
        explanation=q.explanation,
    )
