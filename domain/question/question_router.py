from fastapi import APIRouter, Depends , Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from domain.question import question_schema, question_crud
from models import Question

from starlette import status


# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

router = APIRouter(
    prefix="/api/question",
)

# response_model = question_list의 리턴 값이 Question스키마로 구성된 리스트
@router.get("/list", response_model=list[question_schema.Question])
def question_list(request: Request, db: Session = Depends(get_db)):
    
    _question_list = question_crud.get_question_list(db)
    # return _question_list
    return templates.TemplateResponse("index.html", {"request": request,'question_list' : _question_list})


@router.get("/detail/{question_id}", response_model=question_schema.Question)
def question_detail(question_id: int, request: Request,  db: Session = Depends(get_db)):
    question = question_crud.get_question(db, question_id=question_id)
    
    return templates.TemplateResponse("test.html", {"request": request,'text' : question})

@router.get("/create_site")
def qestion_site(request: Request):
     return templates.TemplateResponse("question_site.html", {"request": request})


@router.post("/create")
def question_create(_question_create: question_schema.QuestionCreate,
                    db: Session = Depends(get_db)):
    question_crud.create_question(db=db, question_create=_question_create)