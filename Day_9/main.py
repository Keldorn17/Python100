import art
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def get_highest_bid_key(bidder: dict) -> str:
    max_bidder = ''
    max_value = 0
    for person in bidder:
        if bidder[person] > max_value:
            max_value = bidder[person]
            max_bidder = person
    return max_bidder


def main() -> None:
    print(art.logo)
    print('Welcome to the secret auction program.')

    bid_dict: dict = {}

    while True:
        bidder_names: str = input('What is your name?: ')
        bidder_value: int = int(input('What is your bid?: $'))

        bid_dict[bidder_names] = bidder_value

        response: str = input('Are there any other bidders? Type \'yes\' or \'no\'.').lower()
        if response != 'yes':
            clear()
            break
        clear()

    winner_index: str = get_highest_bid_key(bid_dict)
    print(f'The winner is {winner_index} with a bid of ${bid_dict[winner_index]}.')


if __name__ == '__main__':
    main()
