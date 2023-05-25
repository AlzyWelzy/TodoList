import json

with open("questions.json", "r") as f:
    questions = json.load(f)

# print(questions["questions"][0]["question"])
print(questions)
