from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import  models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

# Plan 1 -> get:api , post:api
# users 1 -> Plan 1
# Permission name : get:api , /thirdapi , Hi there

@app.post("/firstapi")
async def root():
    id = 1
    return {"message": "Hello World"}

@app.delete("/secondapi")
async def heyman():
    id = 2
    return {"message": "Hello World"}

@app.get("/thirdapi")
async def heyman():
    id = 3
    return {"message": "Hello World"}

@app.get("/fourthapi")
async def heyman():
    id = 4
    return {"message": "Hello World"}

@app.get("/fifthapi")
async def heyman():
    id = 5
    return {"message": "Hello World"}


