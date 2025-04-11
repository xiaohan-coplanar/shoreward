from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from dotenv import load_dotenv
from openai import OpenAI
from model import TravelPlanRequest
from datetime import datetime
import os

from service import prompt_to_response

load_dotenv()

app = FastAPI()

def build_prompt(data: TravelPlanRequest) -> str:
    # 150 words only for debugging reason
    # TODO: This part needs fine tune
    return (
        f"You are a travel planning assistant. Please create a {data.budget_level} travel plan "
        f"for a trip starting on {data.start_date} and ending on {data.end_date}. "
        f"The user will travel from {data.current_city} to {data.destination_city}. "
        "Suggest places to visit, daily itinerary, and general travel advice. Keep it under 150 words." 
    )

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