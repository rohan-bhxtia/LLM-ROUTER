import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

Api_Key = os.getenv("Gemini_Api")
client = genai.Client(api_key= Api_Key)

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
            disable=True)
        )
    )
    
    full_text = response.text
    history.append(types.Content(
        role="model",
        parts=[types.Part(text=full_text)]
    )
)    
    return full_text




if __name__ == "__main__":
    while True:

        prmpt = input("ask ur ques mf: ")
        if prmpt.lower() == "quit":
            break
        print("model: ", ask_ques(prmpt))
