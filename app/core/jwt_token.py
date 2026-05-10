from datetime import datetime, timedelta, timezone
import jwt
from fastapi import HTTPException

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_token(payload:dict):

    expiry = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # Add the 'exp' claim to the payload
    payload.update({"exp": expiry})

    # encode jwt 
    token = jwt.encode(payload=payload,
                       algorithm=ALGORITHM,
                       key=SECRET_KEY)
    return token

def verify_token(token:str):
    
    try:    
        payload = jwt.decode(token,key=SECRET_KEY,algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        # check user existence
        # backend can't trust frontend state as different devices
        if user_id is None:
            # client error 4xx
            raise HTTPException(status_code=401,detail="User does not exist")
        return user_id
    # token is expire
    # client error 4xx
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    # token is tampered or invalid signature/format
    # client error 4xx
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
        


    