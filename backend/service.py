import os
from dotenv import load_dotenv
from openai import OpenAI
from backend.model import TravelPlanRequest
from backend.prompt_template import build_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def prompt_to_response(prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini", # use budget model for debugging
        messages=[
            {"role": "system", "content": "You are a helpful assistant for travel planning."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400 # TODO: max token adjust
    )

    return response

def get_travel_plan(request: TravelPlanRequest):
    prompt = build_prompt(request)
    response = prompt_to_response(prompt)
    return response.choices[0].message.content
