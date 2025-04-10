import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def streaming_generator(messages):
    for response in client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        stream=True
    ):
        ch = response.choices[0].delta.content
        if ch is not None:
            yield ch