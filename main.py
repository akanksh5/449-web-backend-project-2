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

@app.post("/firstapi")
async def firstapihandler():
    # get id and role from token
    scope = "get:firstapi"
    user_id = "1"
    user_obj = session.get(models.User,user_id)
    if user_obj.used >= user_obj.limit:
        return {"message":"Usage limits exceeded"}
    user_obj.used += user_obj.used+1
    session.add(permission_obj)
    session.commit()
    session.refresh(permission_obj)
    return {"message": "Hello World"}

@app.delete("/secondapi")
async def heyman():
    scope = "get:secondapi"
    user_id = "1"
    user_obj = session.get(models.User,user_id)
    if user_obj.used >= user_obj.limit:
        return {"message":"Usage limits exceeded"}
    user_obj.used += user_obj.used+1
    session.add(permission_obj)
    session.commit()
    session.refresh(permission_obj)
    return {"message": "Hello World"}  

@app.get("/thirdapi")
async def heyman():
    scope = "get:thirdapi"
    user_id = "1"
    user_obj = session.get(models.User,user_id)
    if user_obj.used >= user_obj.limit:
        return {"message":"Usage limits exceeded"}
    user_obj.used += user_obj.used+1
    session.add(permission_obj)
    session.commit()
    session.refresh(permission_obj)
    return {"message": "Hello World"}  

@app.get("/fourthapi")
async def heyman():
    scope = "get:fourthapi"
    user_id = "1"
    user_obj = session.get(models.User,user_id)
    if user_obj.used >= user_obj.limit:
        return {"message":"Usage limits exceeded"}
    user_obj.used += user_obj.used+1
    session.add(permission_obj)
    session.commit()
    session.refresh(permission_obj)
    return {"message": "Hello World"}  

@app.get("/fifthapi")
async def heyman():
    scope = "get:fifthapi"
    user_id = "1"
    user_obj = session.get(models.User,user_id)
    if user_obj.used >= user_obj.limit:
        return {"message":"Usage limits exceeded"}
    user_obj.used += user_obj.used+1
    session.add(permission_obj)
    session.commit()
    session.refresh(permission_obj)
    return {"message": "Hello World"}

@app.get("/sixthapi")
async def heyman():
    scope = "get:sixthapi"
    user_id = "1"
    user_obj = session.get(models.User,user_id)
    if user_obj.used >= user_obj.limit:
        return {"message":"Usage limits exceeded"}
    user_obj.used += user_obj.used+1
    session.add(permission_obj)
    session.commit()
    session.refresh(permission_obj)
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


@app.post("/plan")
async def postplan(payload: Any = Body(None)):
    plan = payload["plan"]
    description = payload["description"]
    api_permissions = payload["api_permissions"]
    usage_limits = payload["usage_limits"]
    subscription_obj= models.Subscription(plan=plan, description=description,api_permissions=api_permissions,usage_limits=usage_limits)
    session.add(subscription_obj)
    session.commit()
    return {"Plan added": subscription_obj}

@app.delete("/plan/{subscription_id}")
async def deleteplan(subscription_id: int):
    subscription_obj = session.get(models.Subscription, subscription_id)
    if not subscription_obj:
            raise HTTPException(status_code=404, detail="Subscription not found")
    session.delete(subscription_obj)
    session.commit()
    return {"ok": True}

@app.put("/plan/{subscription_id}")
async def updateplan(subscription_id: int,payload: Any = Body(None)):
    subscription_obj = session.get(models.Subscription, subscription_id)
    if not subscription_obj:
        raise HTTPException(status_code=404, detail="Subscription not found")
    subscription_obj.plan = payload["plan"]
    subscription_obj.description = payload["description"]
    subscription_obj.api_permissions = payload["api_permissions"]
    subscription_obj.usage_limits = payload["usage_limits"]
    session.add(subscription_obj)
    session.commit()
    session.refresh(subscription_obj)
    return subscription_obj

@app.post("/subscribe")
async def postsubscription(payload: Any = Body(None)):
    subscription_id = payload["subscription_id"]
    subscription_obj = session.get(models.Subscription, subscription_id)
    user_obj = session.get(models.User,user_id)
    user_obj.subscription = subscription_id
    user_obj.limit - subscription_obj.usage_limit
    user_obj.used = 0
    session.add(user_obj)
    session.commit()
    return {"Subscription added": subscription_obj}

@app.put("/subscribe/{user_id}")
async def putsubscription(user_id: int,payload: Any = Body(None)):
    subscription_id = payload["subscription_id"]
    subscription_obj = session.get(models.Subscription, subscription_id)
    user_obj = session.get(models.User,user_id)
    user_obj.subscription = subscription_id
    user_obj.limit - subscription_obj.usage_limit
    user_obj.used = 0
    session.add(user_obj)
    session.commit()
    return {"Subscription updated": subscription_obj}


@app.get("/subscriptions/{user_id}")
async def viewsubscriptionhandler(user_id: int):
    user_obj = session.get(models.User,user_id)
    subscription_obj = session.get(models.Subscription,user_obj.subscription)
    return {
                "user": user_id,
                "plan name":subscription_obj.plan,
                "limit" : subscription_obj.usage_limit,
                "api_permissions" : subscription_obj.api_permissions,
                "description":subscription_obj.description
            }


@app.get("/subscriptions/{user_id}/usage")
async def viewsubscriptionhandler(user_id: int):
    user_obj = session.get(models.User,user_id)
    subscription_obj = session.get(models.Subscription,user_obj.subscription)
    return {
                "user": user_id,
                "usage":user_obj.used,
                "limit" : subscription_obj.usage_limits,
                "description":subscription_obj.description
            }

@app.post("/usage/{userId}")
async def postusage(payload: Any = Body(None)):
    usage = payload["usage"]
    user_obj = session.get(models.User,user_id)
    user_obj.used=usage
    session.add(user_obj)
    session.commit()
    return {"User added": subscription_obj}

@app.get("/usage/{user_id}/limit")
async def viewsubscriptionhandler(user_id: int):
    user_obj = session.get(models.User,user_id)
    subscription_obj = session.get(models.Subscription,user_obj.subscription)
    print(user_obj)
    print(subscription_obj)
    return {
                "user": user_id,
                "limit" : subscription_obj.usage_limits
            }


@app.post("/login")
async def postusage(payload: Any = Body(None)):
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email == None or password == None:
        return {"msg": "username or password is missing"}
    if obj:
        access_token = create_access_token(identity=username)
    #return token
    session.commit()
    return {"User added": subscription_obj}

@app.post("/register")
def registeruser(payload: Any = Body(None)):
    password = payload["password"]
    email = payload["email"]
    is_admin=payload["is_admin"]
    if password == None or email==None:
        return "email or password is absent",404
    user_obj = models.User(email=email,password=password,used=0,subscription=1,limit=20,ttl=0,is_admin=is_admin)
    session.add(user_obj)
    session.commit()
    return "The user has been registered",201

