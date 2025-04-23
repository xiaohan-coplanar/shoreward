import os
from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion
from backend.model import TravelPlanRequest
from datetime import datetime

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def prompt_to_response(prompt: str, system_prompt="You are a helpful assistant for travel planning.") -> ChatCompletion:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )
    return response

def run_search_agent(request: TravelPlanRequest) -> str:
    prompt = f"""
        You are a travel search assistant. Based on the user's departure city {request.current_city}, destination {request.destination_city}, and travel period from {request.start_date} to {request.end_date}, list 3 top-rated attractions or must-do activities in the destination city.
    """
    return prompt_to_response(prompt).choices[0].message.content

def run_budget_agent(request: TravelPlanRequest, search_summary: str) -> str:
    prompt = f"""
        You are a travel budget assistant. The user has a {request.budget_level} budget. Using the following summary of searched attractions:

        {search_summary}

        Estimate if these attractions fit a {request.budget_level} travel style. Suggest any changes if necessary.
    """
    return prompt_to_response(prompt).choices[0].message.content

def run_weather_agent(request: TravelPlanRequest) -> str:
    prompt = f"""
        You are a weather assistant. Based on the user's destination {request.destination_city} and dates from {request.start_date} to {request.end_date}, describe the typical weather conditions for that period. Recommend suitable clothing and weather-related precautions.
    """
    return prompt_to_response(prompt).choices[0].message.content

def run_itinerary_agent(request: TravelPlanRequest, search_summary: str, weather_summary: str) -> str:
    prompt = f"""
        You are a travel itinerary assistant. Using the travel dates from {request.start_date} to {request.end_date}, the location {request.destination_city}, and the following search and weather summaries:

        Search Summary:
        {search_summary}

        Weather Summary:
        {weather_summary}

        Propose a brief 3-day itinerary suggestion, choosing activities suitable for the weather and mixing cultural, nature, and food experiences.
    """
    return prompt_to_response(prompt).choices[0].message.content

def get_travel_plan(request: TravelPlanRequest) -> str:
    search_result = run_search_agent(request)
    budget_result = run_budget_agent(request, search_result)
    weather_result = run_weather_agent(request)
    itinerary_result = run_itinerary_agent(request, search_result, weather_result)

    final_prompt = f"""
        You are a travel planning assistant. Given the following information:

        Search Agent Output:
        {search_result}

        Budget Agent Output:
        {budget_result}

        Weather Agent Output:
        {weather_result}

        Itinerary Agent Output:
        {itinerary_result}

        Generate a coherent and personalized travel plan summary that incorporates all these inputs. Make sure it's friendly, concise, and helpful to a traveler.
    """

    final_response = prompt_to_response(final_prompt)
    return final_response.choices[0].message.content
