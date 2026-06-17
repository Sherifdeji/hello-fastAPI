from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my Hello FastAPI app!"}

@app.get("/greet/{name}")
async def greet_user(name: str):
    return{"greeting": f"Hello there, {name}! Nice to have you here..."}