import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel


class GeminiResult(BaseModel):
    query: str
    result: str


def generate_response(query: str) -> GeminiResult:
    load_dotenv()
    client = genai.Client(api_key=os.getenv("Gemini_Api"))
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=query,
        config=types.GenerateContentConfig(
            temperature=0,
            system_instruction=(
                "Answer with sarcastic, aggressive, and funny humor while remaining useful."
            ),
        ),
    )
    return GeminiResult(query=query, result=response.text.strip())


if __name__ == "__main__":
    print(generate_response(input("Enter your prompt: ")))
