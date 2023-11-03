from fastapi import APIRouter
import requests

router= APIRouter()

@router.get("/users")

async def get_users():
   response= requests.get("https://jsonplaceholder.typicode.com/users")
   
   return response.json()
