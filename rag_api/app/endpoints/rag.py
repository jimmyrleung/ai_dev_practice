from fastapi import APIRouter
from app.models.dtos import Prompt
from app.services.simple_rag import sendSimpleRagPrompt

router = APIRouter(prefix="/rags", tags=["Simple Rag"])

messages = []

@router.post("/simple")
def simpleRag(prompt: Prompt):
    answer = sendSimpleRagPrompt(prompt.query)
    return answer
