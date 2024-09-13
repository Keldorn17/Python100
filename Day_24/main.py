def read_file(file_path: str) -> str:
    with open(file_path) as file:
        return file.read()


def custom_letter(base_letter: str, name_list: list[str], item_to_replace: str) -> list[str]:
    final_list = []
    for name in name_list:
        new_letter: str = base_letter.replace(item_to_replace, name)
        final_list.append(new_letter)
    return final_list


def create_files(letters: list[str], name_list: list[str], file_path: str):
    for index, letter in enumerate(letters):
        with open(f"{file_path}/letter_for_{name_list[index]}.txt", "w") as file:
            file.write(letter)


def main() -> None:
    starting_letter: str = read_file("Input/Letters/starting_letter.txt")
    invited_names: str = read_file("Input/Names/invited_names.txt")
    invited_names_list: list[str] = invited_names.split()
    final_letter: list[str] = custom_letter(starting_letter, invited_names_list, "[name]")
    print(final_letter)
    create_files(final_letter, invited_names_list, "./Output/ReadyToSend")


if __name__ == '__main__':
    main()
