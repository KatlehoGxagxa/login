from sqlalchemy import Column, Integer, String, DateTime
import datetime
from . import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer(), autoincrement=True, primary_key=True)
    first_names = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(20), nullable=False)
    last_updated = Column(DateTime(), default=datetime.datetime.now, onupdate=datetime.datetime.now)
    