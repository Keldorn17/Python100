import morse_code


def decode_morse(morse: str) -> str:
    result = []
    for letter in morse.split(' '):
        try:
            result.append(morse_code.MORSE_TO_TEXT_DICT[letter])
        except KeyError:
            raise KeyError(f"'{letter}' is not recognized as a valid morse code.")
    return ''.join(result)


def encode_morse(text: str) -> str:
    result = []
    for letter in text:
        try:
            result.append(morse_code.TEXT_TO_MORSE_DICT[letter.upper()] + ' ')
        except KeyError:
            raise KeyError(f"'{letter}' is not available for translation into morse code.")
    return ''.join(result).strip()


def main() -> None:
    yes_options = {'Y', 'YES', 'YE$', 'Y3S', 'Y3$'}
    no_options = {'N', 'NO', 'N0'}
    while True:
        user_input: str = input("Convert text to Morse or vice versa? "
                                "('Y' for text to Morse, 'N' for Morse to text): ")
        if user_input.upper() in yes_options | no_options:
            break
        print(f"'{user_input}' is not a valid option. Try again.")

    if user_input.upper() in yes_options:
        while True:
            text = input('Enter text to translate: ')
            try:
                print(f"Morse Code: {encode_morse(text)}")
                break
            except KeyError as e:
                print(e.args[0])
    else:
        while True:
            morse = input('Enter Morse code to translate: ')
            try:
                print(f"Morse Code: {decode_morse(morse)}")

                break
            except KeyError as e:
                print(e.args[0])


if __name__ == '__main__':
    main()
