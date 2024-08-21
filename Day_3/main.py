from ascii import treasure_ascii


def main():
    print(treasure_ascii)
    print('Welcome to Treasure Island!')
    print('Your mission is to find the treasure')

    print('You\'re at a cross road. Where do you want to go?')
    first_choice = input('\tType "left" or "right" ').lower()

    if first_choice != 'left':
        print('You fell into a hole. Game Over.')
        return

    print('You\'ve come to a lake. There is an island in the middle of the lake.')
    second_choice = input('\tType "wait" to wai for a boat. Type "swim" to swim across. ').lower()

    if second_choice != 'wait':
        print('You got attacked by an angry trout. Game Over.')
        return

    third_choice = input('You arrive at the island unharmed. There is house with 3 doors.'
                         'One red, one yellow and one blue. Which color do you choose? ').lower()

    if third_choice == 'red':
        print('It\'s a room full of fire. Game Over.')
    elif third_choice == 'blue':
        print('You enter a room of beasts. Game Over.')
    elif third_choice == 'yellow':
        print('You found the treasure. You Win!')
    else:
        print('You chose a door that doesn\'t exist. Game Over.')


if __name__ == '__main__':
    main()
