import requests


class DataFetch:

    def __init__(self, amount_of_questions: int):
        self.question_count = amount_of_questions
        self.__URL = f"https://opentdb.com/api.php?"

    def fetch_data(self) -> list[dict]:
        """
        Fetches trivia questions from the Open Trivia Database API.

        :return: A list of dictionaries, where each dictionary contains information
                 about a trivia question, such as the question text, correct answer,
                 and category.
        """
        response = requests.get(url=self.__URL, params={
            "amount": self.question_count,
            "type": "boolean"
        })
        response.raise_for_status()
        return response.json()["results"]
