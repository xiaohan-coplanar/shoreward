import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from openai import OpenAI
from model import ChatRequest


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
system_prompt = "You are a helpful assistant for travel planning. Maximum 100 words"


@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    messages = []
    messages.append({"role": "system", "content": system_prompt})
    messages.extend(chat_request.history)
    messages.append({"role": "user", "content": chat_request.message})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    reply = response.choices[0].message.content
    return {"reply": reply}