from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Question(Base):
    # __tablename__ 속성은 SQLAlchemy에서 사용되는 클래스 속성
    # 테이블 이름 지정
    __tablename__ = "question"

    id = Column(Integer, primary_key=True)
    subject = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)

class Answer(Base):
    __tablename__ = "answer"

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, nullable=False)
    # 외래키 question.id  
    question_id = Column(Integer, ForeignKey("question.id"))
    # relationship 첫 번째 파라미터 = 참조할 모델명 / 두 번째 파라미터 backref = 역 참조 
    question = relationship("Question", backref="answers")
