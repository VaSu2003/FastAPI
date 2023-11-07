from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/posts")
def get_posts():
    return {"data" : "this is your posts"}

@app.post("/createposts")
def create_posts(payload: dict = body(...)):
    print(payload)
    return {'new_post' : f"title {payload['title']} content: {payload['content']}"}