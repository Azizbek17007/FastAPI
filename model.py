from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base
from typing import Optional
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    image = Column(Optional[str] or None)

