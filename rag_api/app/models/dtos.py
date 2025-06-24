from pydantic import BaseModel

class Message(BaseModel):
    # id: int | None = None
    text: str

class Prompt(BaseModel):
    query: str
