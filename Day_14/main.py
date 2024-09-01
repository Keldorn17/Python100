import art
import game_data
import random
import os


def clear() -> None:
    """Clear the console screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_new_data() -> dict:
    return random.choice(game_data.data)


def check_user_answer(data_a: dict, data_b: dict, user_answer: str) -> bool:
    follower_count = data_a["follower_count"] - data_b['follower_count']
    if user_answer == 'a':
        return follower_count >= 0
    else:
        return follower_count <= 0


def main() -> None:
    score: int = 0
    data_a: dict = get_new_data()
    data_b: dict = get_new_data()

    while True:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {data_a['name']}, a(n) {data_a['description']}, from {data_a['country']}")
        print(art.vs)
        print(f"Against B: {data_b['name']}, a(n) {data_b['description']}, from {data_b['country']}")
        while True:
            answer: str = input("Who has more followers? Type 'A' or 'B': ").lower()
            if answer == 'a' or answer == 'b':
                break
            print("Invalid input. Try again.")

        if not check_user_answer(data_a, data_b, answer):
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        score += 1
        if data_a['follower_count'] < data_b['follower_count']:
            data_a = data_b
        data_b = get_new_data()
        clear()


if __name__ == '__main__':
    main()
