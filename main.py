from classifier import classify

prompt = input("Enter your prompt: ")

category = classify(prompt)

print("Category:", category)