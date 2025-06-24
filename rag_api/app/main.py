# app/main.py
from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from app.endpoints import hello_world_router, rag_router

app = FastAPI(title="My POC API")

app.include_router(hello_world_router)
app.include_router(rag_router)
# curl --header "Content-Type: application/json" --request POST --data '{"text":"hello"}' http://localhost:8000/messages/
# curl --header "Content-Type: application/json" --request POST --data '{"query":"Qual é a visão de Euclides da Cunha sobre o ambiente natural do sertão nordestino e como ele influencia a vida dos habitantes?"}' http://localhost:8000/rags/simple