import datetime

from pydantic import BaseModel, field_validator


class AnswerCreate(BaseModel):
    content: str

    # @field_validator 유효성 검사 
    # content에 빈 값이 있는지 확인
    @field_validator('content')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.!!!')
        return v

class Answer(BaseModel):
    id: int
    content: str
    create_date: datetime.datetime