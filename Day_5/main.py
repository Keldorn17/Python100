import random
import character_set


def user_information_request(character: str) -> int:
    while True:
        try:
            number: int = int(input(f'How many {character} would you like in your password?\n'))
            if number >= 0:  # Ensure number is non-negative
                return number
            else:
                print('Please enter a non-negative number.')
        except ValueError:
            print('Please enter a valid number!')


def generate_password(nletters: int, nsymbols: int, nnumbers: int) -> str:
    password: list[str] = []

    for _ in range(nletters):
        password.append(random.choice(character_set.LETTERS))
    for _ in range(nsymbols):
        password.append(random.choice(character_set.SYMBOLS))
    for _ in range(nnumbers):
        password.append(random.choice(character_set.NUMBERS))

    random.shuffle(password)
    return ''.join(password)


def main() -> None:
    print('Welcome to the PyPassword Generator!')
    number_of_letters: int = user_information_request('letters')
    number_of_symbols: int = user_information_request('symbols')
    number_of_numbers: int = user_information_request('numbers')

    new_password: str = generate_password(number_of_letters, number_of_symbols, number_of_numbers)
    print(f'Your password is: {new_password}')


if __name__ == '__main__':
    main()
