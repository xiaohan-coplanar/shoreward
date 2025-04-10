import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
system_prompt = "You are a helpful assistant for travel planning. Maximum 100 words"

def streaming_generator(messages):
    try:
        for response in client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True
        ):
            ch = response.choices[0].delta.content
            if ch is not None:
                yield ch
    except Exception as e:
        raise e