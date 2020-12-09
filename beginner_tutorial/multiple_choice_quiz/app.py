from Question import Question

question_prompts = [
    "What is an apple?\n(a) Fruit\n(b) Vegetable\n",
    "What is an cauliflower?\n(a) Fruit\n(b) Vegetable\n",
    "What is an watermelon?\n(a) Fruit\n(b) Vegetable\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct") 

run_test(questions)