from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Integer,String
from sqlalchemy.orm import Mapped

from config.database import Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    username: Mapped[str] = Column(String, unique=True)
    email: Mapped[str] = Column(String, unique=True)
    password: Mapped[str] = Column(String)
