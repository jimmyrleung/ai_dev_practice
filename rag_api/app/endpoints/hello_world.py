from fastapi import APIRouter
from app.models.dtos import Message

router = APIRouter(prefix="/messages", tags=["Messages"])

messages = []

@router.get("/")
def list_messages():
    list = messages.copy()
    return list

@router.post("/")
def create_message(message: Message):
    print(">>>" + message.text)
    next_id = 1 if messages.__len__() == 0 else messages[messages.__len__() - 1]["id"] + 1
    messages.append({ "id": next_id, "text": message.text })
    return messages
