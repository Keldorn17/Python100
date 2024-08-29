import art
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


OPERATORS = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}


def main() -> None:
    clear()
    print(art.logo)
    first_num: int = int(input("What's the first number?: "))
    while True:
        while True:
            for operator in OPERATORS:
                print(operator)
            operator: str = input("Pick an operation: ")
            if operator in OPERATORS:
                break
            print("Not a valid operator try again.")
        second_num: int = int(input("What's the next number?: "))

        result: int = OPERATORS[operator](first_num, second_num)
        print(f"{first_num} {operator} {second_num} = {result}")

        response: str = input(
            f"Type 'y' to continue calculation with '{result}', or type 'n' to start a new calculation:")
        if response.lower() != 'y':
            main()

        first_num: int = result


if __name__ == '__main__':
    main()
