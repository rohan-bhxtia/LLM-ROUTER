from classifier import classify
from router import route

user_prompt = input("Enter your prompt: ")

category_from_classifier = classify(user_prompt)

response = route(category_from_classifier, user_prompt)

print(response)