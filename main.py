from fastapi import FastAPI
from datetime import datetime
import random

PROPHETIC_QUOTES = [
    "On Brotherhood: 'None of you truly believes until he loves for his brother that which he loves for himself.' (Sahih al-Bukhari)",
    "On Kindness: 'Make things easy for people and do not make them difficult. Give people good news and bring them joy, and do not turn them away.' (Sahih al-Bukhari)",
    "On Speech: 'Whoever believes in Allah and the Last Day, let him speak good or remain silent.' (Sahih Muslim)",
    "On Charity: 'Do not underestimate any good deed, even meeting your brother with a cheerful face.' (Sahih Muslim)",
    "On True Strength: 'The strong man is not the one who can wrestle someone else down. The strong man is only the one who controls himself when he is angry.' (Sahih al-Bukhari)"
]

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my Hello FastAPI app!"}

@app.get("/greet/{name}")
async def greet_user(name: str):
    return{"greeting": f"Hello there, {name}! Nice to have you here..."}

@app.get("/time")
async def get_current_time():
    return{"current_time": datetime.now()}

@app.get("/quote")
async def get_random_quote():
    return{"Quote": random.choice(PROPHETIC_QUOTES)}