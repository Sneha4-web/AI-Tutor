# scoring.py


def calculate_score(questions, answers):
    """
    Calculate the student's quiz score.

    questions = list of quiz questions
    answers = student's selected answers
    """

    score = 0

    for i in range(len(questions)):

        correct_answer = questions[i]["answer"]
        student_answer = answers[i]

        if student_answer == correct_answer:
            score += 1

    total_questions = len(questions)

    if total_questions == 0:
        percentage = 0
    else:
        percentage = (score / total_questions) * 100

    return score, total_questions, percentage


def analyze_answers(questions, answers):
    """
    Find the student's strong and weak concepts.
    """

    weak_concepts = []
    strong_concepts = []

    for i in range(len(questions)):

        question = questions[i]
        student_answer = answers[i]

        correct_answer = question["answer"]
        concept = question.get("concept", "General")

        if student_answer == correct_answer:
            strong_concepts.append(concept)
        else:
            weak_concepts.append(concept)

    return weak_concepts, strong_concepts