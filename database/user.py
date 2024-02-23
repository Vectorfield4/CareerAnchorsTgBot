from sqlalchemy import Column, VARCHAR, Integer

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    user_id = Column(Integer, unique=True, nullable=False, primary_key=True)
    username = Column(VARCHAR(32), unique=False, nullable=True)
    last_name = Column(VARCHAR(50), unique=False, nullable=True)
    first_name = Column(VARCHAR(50), unique=False, nullable=True)




