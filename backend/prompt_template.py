from backend.model import TravelPlanRequest

def build_prompt(data: TravelPlanRequest) -> str:
    """
    Build a prompt for the OpenAI API based on user's request.

    Args:
        data (TravelPlanRequest): The request to generate a prompt from.

    Returns:
        str: The prompt for the OpenAI API.
    """
    # 150 words only for debugging reason
    # TODO: This part needs fine tune
    return (
        f"You are a travel planning assistant. Please create a {data.budget_level} travel plan "
        f"for a trip starting on {data.start_date} and ending on {data.end_date}. "
        f"The user will travel from {data.current_city} to {data.destination_city}. "
        "Suggest places to visit, daily itinerary, and general travel advice. Keep it under 150 words." 
    )
