from Question import Question

question_prompts = [
    "What was Frodo Baggins's true name in Westron?\n(a) Maura Labingi\n(b) Balbo Ladingi\n(c) Freador Cabige\n\n",
    "What was Pipin's true name in Westron?\n(a) Peregrin\n(b) Razanur\n(c) Zilbirâpha\n\n",
    "What was king Théoden's true name in Westron?\n(a) Thranduil\n(b) Denzelor\n(c) Tûrac\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct. You're as knowledgeable in Tolkien lore as Stephen Colbert!")

run_test(questions)