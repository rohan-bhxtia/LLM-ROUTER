from providers import gemini, mistral, llama

def route(category, prompt):

    if category == "coding":
        return gemini.generate(prompt)

    elif category == "research":
        return gemini.generate(prompt)

    elif category == "writing":
        return mistral.generate(prompt)

    elif category == "general":
        return llama.generate(prompt)

    else:
        return "Unknown category"