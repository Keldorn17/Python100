import pandas


def main() -> None:
    nato_alphabet: pandas.DataFrame = pandas.read_csv("nato_phonetic_alphabet.csv")
    nato_dict: dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

    user_input: str = input("Enter a word: ").upper()
    user_nato: list[str] = [nato_dict[letter] for letter in user_input]
    print(user_nato)


if __name__ == '__main__':
    main()