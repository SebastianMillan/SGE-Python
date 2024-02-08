from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt

app=FastAPI()

class User(BaseModel):
    id: int
    name: str = 'Sebastian'
    singup_ts : datetime | None
    tastes: dict[str, PositiveInt]


@app.get("/")
async def get():
    return {"message":"Hola Mundo!"}

@app.post("post/")
async def post(user: User):
    return user

