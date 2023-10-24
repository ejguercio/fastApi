from fastapi import FastAPI
import requests
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/users")

async def get_users():
   response= requests.get("https://jsonplaceholder.typicode.com/users")
   print(response)
   return response.json()
