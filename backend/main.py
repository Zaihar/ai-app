from fastapi import FastAPI
from pydantic import BaseModel
from backend.llm import ask_llm
from backend.database import save_chat

app = FastAPI()



class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
def chat(request: ChatRequest):
    ans = ask_llm(request.question)
    
    save_chat(request.question,ans)

    return {
        "response": ans
    }