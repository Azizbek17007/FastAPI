from django.forms import models
from fastapi import FastAPI, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal, engine

import model
import sxema

model.Base.metadata.create_all(bind=engine)
app = FastAPI(title='Crud for database')

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/product", response_model=sxema.ProductBase)
async def create_product(product: sxema.ProductBase, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())

