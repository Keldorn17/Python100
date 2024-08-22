import random
import ascii

ROCK = 0
PAPER = 1
SCISSOR = 2


def user_choice():
    while True:
        try:
            users_choice: int = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
            if users_choice in [ROCK, PAPER, SCISSOR]:
                return users_choice
            else:
                print("Invalid choice. Please choose 0, 1, or 2.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    ascii_art: list[str] = [ascii.rock, ascii.paper, ascii.scissors]
    users_choice = user_choice()
    machine_choice: int = random.randint(0, 2)

    print(f'You chose: \n{ascii_art[users_choice]}')
    print(f'computer chose: \n{ascii_art[machine_choice]}')

    # Paper beats Rock (1 <- 0), Scissors beats Paper (2 <- 1), Rock beats Scissors (0 <- 2)
    # Explanation: If we calculate the differences based on the above
    # User can win if the difference is 1 or -2 ( 1 - 0 = 1, 2 - 1 = 1, 0 - 2 = -2 )
    # Computer can win if the difference is -1 or 2 ( 0 - 1 = -1, 1 - 2 = -1, 2 - 0 = 2 )
    # if users_choice == machine_choice:
    #     print('Draw')
    # elif users_choice - machine_choice == 1 or users_choice - machine_choice == -2:
    #     print('You win!')
    # else:
    #     print('You lose!')

    # We can get the same result by using modular 3
    # 1 % 3 = 1, -2 % 3 = 1
    if users_choice == machine_choice:
        print('Draw')
    elif (users_choice - machine_choice) % 3 == 1:
        print('You win!')
    else:
        print('You lose!')


if __name__ == '__main__':
    main()
