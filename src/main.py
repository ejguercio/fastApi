from fastapi import FastAPI
import requests
from routes import users

app = FastAPI()

#Routers
app.include_router(users.router)

@app.get("/")
async def read_root():
    return {"FASTAPI"}

@app.get("/users")

async def get_users():
   response= requests.get("https://jsonplaceholder.typicode.com/users")
   
   return response.json()
