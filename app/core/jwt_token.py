from datetime import datetime, timedelta, timezone
import jwt

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

def verify_token():
    pass