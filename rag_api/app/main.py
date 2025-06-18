# app/main.py
from fastapi import FastAPI
from app.endpoints import hello_world_router

app = FastAPI(title="My POC API")

app.include_router(hello_world_router)
# curl --header "Content-Type: application/json" --request POST --data '{"text":"hello"}' http://localhost:8000/messages/