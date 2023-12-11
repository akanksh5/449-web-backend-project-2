import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
import bcrypt

security = HTTPBearer()


#define a base model for the token
class TokenPayload(BaseModel):
    sub: int = None
    role: str = None


#function to check the user's role based on the bearer token
async def check_user_role(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not credentials:
        raise HTTPException(status_code=401, detail="Bearer token missing")
    try:
        token = credentials.credentials
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        token_data = TokenPayload(**payload)
        if token_data.role not in ["admin","user"]:
            raise HTTPException(status_code=403, detail="Not authorized to access this resource")
        return token_data
    except jwt.exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")