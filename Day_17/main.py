from data import DataFetch
from question_model import Question
from quiz_brain import QuizBrain
import random


def main() -> None:
    question_bank: list[Question] = []
    question_data: list[dict] = DataFetch(15).fetch_data()
    for question in question_data:
        question_bank.append(Question(q_text=question["question"], q_answer=question["correct_answer"]))

    random.shuffle(question_bank)
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz.")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")


if __name__ == '__main__':
    main()
