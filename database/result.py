import datetime

from sqlalchemy import Column, VARCHAR, Integer, ARRAY, Boolean, TIMESTAMP, ForeignKey
from .base import BaseModel
class Result(BaseModel):
    __tablename__ = "results"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), unique=True, nullable=False)
    answers = Column(ARRAY(Integer))
    finished = Column(Boolean, default=False)
    updated = Column(TIMESTAMP, onupdate=datetime.datetime.now())