from fastapi import FastAPI
from pydantic import BaseModel 





class User(BaseModel):
    def __init__(self, username, id):
        username = str(username)
        id =  int(id) 


