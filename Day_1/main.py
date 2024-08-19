def main() -> None:
    print("Welcome to the Band Name Generator.")
    city: str = input("What's the name of the city you grew up in?\n")
    pet: str = input("What's your pet's name?\n")
    print(f"Your band name could be {city} {pet}")


if __name__ == '__main__':
    main()
    