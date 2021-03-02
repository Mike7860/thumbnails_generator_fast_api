from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel
#from sqlalchemy.orm import relationship
from .database import Base


class Image(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class Image(Base):
    __tablename__ = "images"

    id: Column(Integer, primary_key=True, index=True)
    name: Column(String, unique=True, index=True)
    # x_resolution: int
    # y_resolution: int