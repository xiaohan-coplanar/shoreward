import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion
from backend.model import TravelPlanRequest
from backend.prompt_template import build_prompt

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def prompt_to_response(prompt: str) -> ChatCompletion:
    """
    Generate a response from the OpenAI API based on user's prompt.

    Args:
        prompt (str): The prompt to generate a response from.

    Returns:
        ChatCompletion: The response from the OpenAI API.
    """
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

def get_travel_plan(request: TravelPlanRequest) -> str:
    """
    Generate a travel plan from the OpenAI API based on user's request.

    Args:
        request (TravelPlanRequest): The request to generate a travel plan from.

    Returns:
        str: The travel plan from the OpenAI API.
    """
    prompt = build_prompt(request)
    response = prompt_to_response(prompt)
    return response.choices[0].message.content
