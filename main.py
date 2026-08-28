import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

load_dotenv()

Api_Key = os.getenv("Gemini_Api")
client = genai.Client(api_key= Api_Key)

class Schema(BaseModel):
    topic:str = Field(
        description="name the topic"
    )
    fact:str = Field(
        description="explain fact in 1 line"
    )


history = []
def ask_ques(prompt)-> str:
    history.append(types.Content(
        role="user",
        parts=[types.Part(text=prompt)]
    ))
    response = client.models.generate_content(
        model = "gemini-3.6-flash",
        contents = history,
        config = types.GenerateContentConfig(
            temperature=0.1,
            system_instruction="ruthless sarcastic",
            automatic_function_calling=types.AutomaticFunctionCallingConfig(
            disable=True),
            response_mime_type="application/json",
            response_schema= Schema
        )
    )

    full_text = response.parsed
    history.append(types.Content(
        role="model",
        parts=[types.Part(text=response.text)]
    )
)    
    return full_text




if __name__ == "__main__":

    while True:
        prmpt = input("ask ur ques mf: ")
        if prmpt.lower() == "quit":
            break
        result = ask_ques(prmpt)

        print("Topic: ", result.topic)
        print("Fact: ", result.fact)