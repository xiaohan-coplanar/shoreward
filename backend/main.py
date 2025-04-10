import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from openai import OpenAI
from model import ChatRequest

from service import streaming_generator


load_dotenv()

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
system_prompt = "You are a helpful assistant for travel planning. Maximum 100 words"

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    messages = []
    messages.append({"role": "system", "content": system_prompt})
    messages.extend(chat_request.history)
    messages.append({"role": "user", "content": chat_request.message})
    try:
        return StreamingResponse(streaming_generator(messages), media_type="text/event-stream")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))