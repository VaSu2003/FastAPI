from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title:str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{'title': 'title of post 1', 'content': 'content of post 1', 'id': 1}, {'title':'favourite food', 'content':'I like cheese'}]


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts")
def get_posts():
    return {"data" : my_posts}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post)
    print(new_post.model_dump())
    return {"data": "new_post"}