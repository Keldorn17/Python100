from question_model import Question


class QuizBrain:

    def __init__(self, q_list: list[Question]) -> None:
        self.question_number: int = 0
        self.question_list: list[Question] = q_list
        self.score: int = 0

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer: str = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: str):
        if user_answer.lower() == correct_answer.lower():
            print("\tYou got it right!")
            self.score += 1
        else:
            print("\tThat's wrong.")
        print(f"\tThe correct answer was: {correct_answer}.")
        print(f"\tYou current score is: {self.score}/{self.question_number}\n")

