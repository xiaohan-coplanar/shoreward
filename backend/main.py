import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI()

# Allow CORS from your GitHub Pages domain (adjust when published)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Secure later
    allow_methods=["POST"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": chat_request.message}]
    )
    reply = response.choices[0].message.content
    return {"reply": reply}