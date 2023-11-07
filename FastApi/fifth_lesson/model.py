from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, PositiveInt
from typing import Union


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: PositiveInt 
    is_subscribed: bool 