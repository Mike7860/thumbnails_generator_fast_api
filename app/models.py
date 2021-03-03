from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from pydantic import BaseModel
# from sqlalchemy.orm import relationship
from .database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    #image = Column(Fil)
    # x_resolution: int
    # y_resolution: int
