from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from dotenv import load_dotenv
from openai import OpenAI
from model import TravelPlanRequest
from datetime import datetime
import os

from service import prompt_to_response
from prompt_template import build_prompt

load_dotenv()

app = FastAPI()

@app.post("/plan")
async def travel_plan_endpoint(request: TravelPlanRequest):
    try:
        prompt = build_prompt(request)

        response = prompt_to_response(prompt)

        plan_text = response.choices[0].message.content
        return {"plan": plan_text}

    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))