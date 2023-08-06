import json

with open("questions.json", "r") as f:
    # questions = json.load(f)
    content = f.read()

data = json.loads(content)

# print(questions["questions"][0]["question"])
# print(questions)

print(data)
score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index+1}: {alternative}")
    user_choice = int(input("Enter your choice: "))
    question["user_choice"] = user_choice
    if question["user_choice"] == question["correct_answer"]:
        score += 1

print(f"Your score is {score} out of {len(data)}")
