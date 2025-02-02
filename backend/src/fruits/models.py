from sqlalchemy import Column, Integer, String
from src.database import Base


class DBFruit(Base):
    __tablename__ = "fruit"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    color = Column(String)
