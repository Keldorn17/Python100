def greet(name: str) -> None:
    print(f'Hello {name}')


greet('Zoli')


def greet_with(name: str, location: str) -> None:
    print(f'Hello {name}')
    print(f'What is it like in {location}')


greet_with('Zoli', 'Nowhere')
greet_with(location='Nowhere', name='Zoli')
