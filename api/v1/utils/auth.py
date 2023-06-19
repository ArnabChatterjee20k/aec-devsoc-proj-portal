from fastapi import HTTPException
from datetime import datetime, timedelta
from typing import Any, Union

import jwt
from passlib.context import CryptContext

from api.v1.Config import Config
from api.v1.constants.status import FAIL

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


ALGORITHM = "HS256"


def create_access_token(subject: Union[str, Any]) -> str:
    payload = {
        'exp': datetime.utcnow() + timedelta(days=Config.access_token_expire_days),
        'iat': datetime.utcnow(),
        'sub': subject
    }
    return jwt.encode(
        payload,
        Config.secret,
        algorithm=ALGORITHM
    )


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, Config.secret, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        response = {}
        response.update(
            status=FAIL, message="Signature has expired", error=[], data={})
        raise HTTPException(status_code=401, detail=response)
    except jwt.InvalidTokenError as e:
        print(e)
        response = {}
        response.update(status=FAIL, message="Invalid token",
                        error=[], data={})
        raise HTTPException(status_code=401, detail=response)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)
