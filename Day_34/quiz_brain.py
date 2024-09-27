from question_model import Question
import html


class QuizBrain:

    def __init__(self, q_list: list[Question]) -> None:
        self.question_number: int = 0
        self.question_list: list[Question] = q_list
        self.score: int = 0
        self.current_question = None

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text: str = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}: "
        # user_answer: str = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str):
        if user_answer.lower() == self.current_question.answer.lower():
            self.score += 1
            return True
        return False

