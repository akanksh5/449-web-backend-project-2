from sqlalchemy import Column, ForeignKey, Integer, String , Boolean
from database import Base,Session



class Subscription(Base):
    __tablename__ = "subscription"

    id = Column(Integer, primary_key=True,index=True)
    plan = Column(String(20), index=True)
    description = Column(String(20))
    api_permissions = Column(String(30)) #['get:books','post:books']
    usage_limits = Column(Integer)

class Permission(Base):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20), index=True)
    api_endpoint = Column(String(20), index=True)
    description = Column(String(20), index=True)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(40))
    password = Column(String(20))
    is_admin = Column(Boolean, default=False)
    subscription = Column(Integer,ForeignKey("subscription.id"))
    used = Column(Integer)
    limit = Column(Integer)
    ttl = Column(Integer)



