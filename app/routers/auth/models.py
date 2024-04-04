from pydantic import BaseModel
from app.utilities.db import Base
from sqlalchemy import Column, String, func
from sqlalchemy.orm import mapped_column, Mapped
from uuid import UUID

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str
    password: str | None

class UserInDb(User):
    hashed_password: str

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.gen_random_uuid())
    username = Column(String)
    email = Column(String)
    hashed_password = Column(String)