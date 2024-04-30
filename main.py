from fastapi import FastAPI

from domain.question import question_router
from domain.answer import answer_router

app = FastAPI()

# include_router로 라우터 추가
app.include_router(question_router.router)
app.include_router(answer_router.router)