import art
import string

ALPHABET = string.ascii_lowercase


def cipher(direction: str, message: str, shift_number: int) -> str:
    '''
    :param direction: 'encode' for encoding, 'decode' for decoding
    :param message: message to encode or decode
    :param shift_number: number of times each letter is shifted
    :return: encoded or decoded message as a string
    '''

    coded_message: str = ''

    if direction.lower() == 'decode':
        shift_number *= -1

    for letter in message:
        if letter in ALPHABET:
            letter_index: int = ALPHABET.index(letter) + shift_number
            coded_message += ALPHABET[letter_index % len(ALPHABET)]
        else:
            coded_message += letter

    return coded_message


def main() -> None:
    print(art.logo)
    while True:
        while True:
            direction: str = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            if direction == 'encode' or direction == 'decode':
                break
            print(f'\'{direction}\' is not an acceptable answer for a crypt type')
        text: str = input("Type your message:\n").lower()
        while True:
            try:
                shift: int = int(input("Type the shift number:\n"))
                shift = shift % len(ALPHABET)
                break
            except ValueError:
                print('Please enter a valid integer for the shift number.')

        if direction == 'encode':
            print(f'The encoded message is {cipher('encode', text, shift)}')
        else:
            print(f'The decoded message is {cipher('decode', text, shift)}')

        restart: str = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart != 'yes':
            print('Bye')
            break


if __name__ == '__main__':
    main()
