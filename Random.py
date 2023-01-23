import random

questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "Who is the author of the book 'To Kill a Mockingbird'?",
    "In what year did World War II start?",
    "What is the chemical symbol for gold?"
]

random.shuffle(questions)
for question in questions:
    print(question)
