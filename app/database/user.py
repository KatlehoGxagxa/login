from sqlalchemy import Column, Integer, String, DateTime
from . import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer(), autoincrement=True)