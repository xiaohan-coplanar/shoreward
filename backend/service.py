import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def prompt_to_response(prompt):
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
