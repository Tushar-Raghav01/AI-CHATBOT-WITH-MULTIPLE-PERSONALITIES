import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage

app = FastAPI()

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

class ChatRequest(BaseModel):
    message: str
    mode: str
    history: list = []

@app.get("/")
def home():
    return {"message": "AI Persona Chat API is running"}

@app.post("/api/chat")
def chat(request: ChatRequest):

    messages = [
        SystemMessage(content=request.mode)
    ]

    for item in request.history:
        if item["role"] == "user":
            messages.append(HumanMessage(content=item["content"]))
        else:
            from langchain_core.messages import AIMessage
            messages.append(AIMessage(content=item["content"]))

    messages.append(
        HumanMessage(content=request.message)
    )

    response = model.invoke(messages)

    return {
        "response": response.content
    }