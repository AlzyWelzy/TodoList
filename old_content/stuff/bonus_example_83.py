mood_rating = {
    "1": "awful",
    "2": "bad",
    "3": "ok",
    "4": "good",
    "5": "excellent",
}

date = input("Enter the date: ")
mood = input("Enter your mood (1-5): ")
journal_entry = input("Enter your journal entry: ")

with open("journal.txt", "a") as journal:
    journal.write(f"Date: {date}\n")
    journal.write(f"Mood: {mood_rating[mood]}\n")
    journal.write(f"Journal Entry: {journal_entry}\n\n")


with open("journal.txt", "r") as journal:
    print(journal.read())
