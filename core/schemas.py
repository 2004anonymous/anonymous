from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import Base, engine

tablename = "user"
class User(Base):
    __tablename__ = tablename

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)

def createTable():
    Base.metadata.create_all(engine)
    print(f"Table {tablename} created !")