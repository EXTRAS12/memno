from datetime import datetime, timedelta
from typing import Optional

import jwt
from django.conf import settings


def create_token(user_id: int):
    """Создание токена"""
    access_token_expire = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return {
        "user_id": user_id,
        "access_token": create_access_token(
            data={"user_id": user_id}, expires_delta=access_token_expire
        ),
        "token_type": "Token",
    }


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Создание access token"""
    to_encode = data.copy()
    if expires_delta is not None:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": "access"})
    encode_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encode_jwt
