import random
import art
import os

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear() -> None:
    """Clear the console screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def get_card() -> int:
    """
        Draw a random card from the available deck.

        Returns:
        - An integer representing the value of the drawn card.
        """
    return random.choice(CARDS)


def calc_score(card_list: list[int]) -> int:
    """
        Calculate the score of a hand of cards, treating Aces as 11 or 1
        to avoid busting if the total exceeds 21.

        Note:
        - The original list will change if Aces have to count as 1.

        Parameters:
        - card_list: A list of integers representing the card values in hand.

        Returns:
        - The calculated score as an integer.
        """
    total_score: int = 0
    for card in card_list:
        total_score += card

    while total_score > 21 and 11 in card_list:
        for index, card in enumerate(card_list):
            if card == 11:
                card_list[index] = 1
                break
        total_score -= 10
    return total_score


def soft_17(card_list: list[int]) -> list[int]:
    """
        Ensure that the hand's score is at least 17 by drawing additional cards if necessary.
        If the score is 17 or higher, the function returns the hand as-is.

        Note:
        - The original card_list may be modified by this function as cards are appended.

        Parameters:
        - card_list: A list of integers representing the current hand of cards.

        Returns:
        - The modified card_list where the score is at least 17.
        """
    if calc_score(card_list) >= 17:
        return card_list
    card_list.append(get_card())
    return soft_17(card_list)
    # # Alternative solution:
    # while calc_score(card_list) < 17:
    #     card_list.append(get_card())
    # return card_list


def print_winner(player_score: int, dealer_score: int) -> None:
    """
        Determine and print the outcome of a card game based on the scores of the player and dealer.

        This function compares the player's score and the dealer's score to decide the winner.
        It prints different messages depending on whether the player or dealer has gone over 21,
        or if the player's score is higher, lower, or equal to the dealer's score.

        Parameters:
        - player_score: An integer representing the player's total score.
        - dealer_score: An integer representing the dealer's total score.

        Returns:
        - None: This function does not return a value. It prints the result directly to the console.
        """
    if player_score > 21:
        print("You went over. You lost.")
    elif dealer_score > 21:
        print("Dealer went over. You win.")
    elif player_score > dealer_score:
        print("You win")
    elif player_score < dealer_score:
        print("You lose.")
    else:
        print("Push")


def main() -> None:
    while True:
        print(art.logo)
        player_cards: list[int] = [get_card(), get_card()]
        dealer_cards: list[int] = [get_card(), get_card()]

        player_score: int = calc_score(player_cards)

        while player_score <= 21:
            print(f"\tYour cards: {player_cards}, current score: {player_score}")
            print(f"\tDealer's first card: {dealer_cards[0]}")
            player_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if player_choice != 'y':
                break
            player_cards.append(get_card())
            player_score = calc_score(player_cards)

        soft_17(dealer_cards)
        dealer_score: int = calc_score(dealer_cards)

        print(f"\tYour final hand: {player_cards}, final score: {player_score}")
        print(f"\tDealer's final hand: {dealer_cards}, final score: {dealer_score}")
        print_winner(player_score, dealer_score)

        response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if response != 'y':
            print("Thanks for playing!")
            break
        clear()


if __name__ == '__main__':
    main()
