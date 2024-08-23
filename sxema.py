from pydantic import BaseModel
from typing import Optional, List

class ProductBase(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    image: Optional[str] = None

class ProductCreate(ProductBase):
    id: int

    class Config:
        orm_mode = True


