import random
import art

DIFFICULTY = {
    "easy": 10,
    "hard": 5
}


def get_random() -> int:
    return random.randint(1, 100)


def game_logic(number_to_guess: int, attempts: int) -> None:
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess: int = int(input("Make a guess: "))
        if number_to_guess > guess:
            print("Too low.")
        elif number_to_guess < guess:
            print("Too high.")
        else:
            print(f"You got it! The answer was {number_to_guess}.")
            return
        attempts -= 1
    print(f"You lost. The answer was {number_to_guess}.")


def main() -> None:
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    number_to_guess: int = get_random()
    print("I'm thinking of a nuber between 1 and 100")
    while True:
        try:
            choice: str = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
            attempts: int = DIFFICULTY[choice]
            break
        except KeyError:
            print(f"\tIncorrect input for difficulty. Try again.")

    game_logic(number_to_guess, attempts)


if __name__ == '__main__':
    main()
