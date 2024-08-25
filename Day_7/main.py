import hangman_art
import hangman_words
import random


def get_random_word() -> str:
    return random.choice(hangman_words.word_list)


def create_blank_str(base_word: str) -> str:
    return '_' * len(base_word)


def check_if_user_guessed_right(base_word: str, user_guess: str) -> bool:
    return user_guess in base_word


def fill_blank(base_word: str, user_guess: str, blank_word: str) -> str:
    blank_list: list[str] = []
    for letter in blank_word:
        blank_list.append(letter)

    for index, letter in enumerate(base_word):
        if letter == user_guess:
            blank_list[index] = letter

    return ''.join(blank_list)


def guess_a_word() -> str:
    while True:
        user_guess: str = input('Guess a letter: ').lower()
        if user_guess.isnumeric():
            print('You cannot guess numbers. Try again.')
        elif len(user_guess) != 1:
            print('You cannot guess words. Try again.')
        else:
            return user_guess


def win_lose_check_loop_condition(life: int, base_word: str, blank_word: str) -> bool:
    if life == 0:
        print(f'You lost. The word was: {base_word}')
        return False

    if base_word == blank_word:
        print(f'You won. The word was: {base_word}')
        return False
    return True


def main() -> None:
    print(hangman_art.logo)
    word_to_guess: str = get_random_word()
    life: int = 6
    blank_word: str = create_blank_str(word_to_guess)

    while win_lose_check_loop_condition(life, word_to_guess, blank_word):
        print(f'*******************{life}/6 LIVES LEFT*******************')
        print(f'Word to guess: {blank_word}')
        user_guess: str = guess_a_word()

        if not check_if_user_guessed_right(word_to_guess, user_guess):
            print(f'You guessed {user_guess}, that\'s not in the word. You lose a life')
            life -= 1
        elif user_guess in blank_word:
            print(f'You have already guessed {user_guess}')
        else:
            blank_word: str = fill_blank(word_to_guess, user_guess, blank_word)

        print(hangman_art.stages[life])


if __name__ == '__main__':
    main()
