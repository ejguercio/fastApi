from fastapi import APIRouter
import requests

router= APIRouter(prefix="/users")

@router.get("/")
async def get_users():
   response= requests.get("https://jsonplaceholder.typicode.com/users")
   return response.json()

@router.get("/{id}")
async def getUserById(id: int):
   response= requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
   return response.json()
