from fastapi import FastAPI, HTTPException,Request,Body
from sqlalchemy.orm import Session
import  models
from database import SessionLocal, engine
from sqlalchemy.orm import sessionmaker
from typing import Any

models.Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
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

@app.post("/permission")
async def postpermission(payload: Any = Body(None)):
    name = payload["permission_name"]
    api_endpoint = payload["api_endpoint"]
    description = payload["description"]
    permission = models.Permission(name=name, api_endpoint=api_endpoint,description=description)
    session.add(permission)
    session.commit()
    return {"todo added": permission.name}

@app.delete("/permission/{permission_id}")
async def deletepermission(permission_id: int):
    permission_obj = session.get(models.Permission, permission_id)
    if not permission_obj:
            raise HTTPException(status_code=404, detail="Permission not found")
    session.delete(permission_obj)
    session.commit()
    return {"ok": True}

@app.put("/permission/{permission_id}")
async def updatepermission(permission_id: int,payload: Any = Body(None)):
    permission_obj = session.get(models.Permission, permission_id)
    if not permission_obj:
        raise HTTPException(status_code=404, detail="Permission not found")
    permission_obj.name = payload["permission_name"]
    permission_obj.api_endpoint = payload["api_endpoint"]
    permission_obj.description = payload["description"]
    session.add(permission_obj)
    session.commit()
    session.refresh(permission_obj)
    return permission_obj



