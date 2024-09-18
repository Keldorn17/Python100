import random
import character_set


def generate_password(nletters: int, nsymbols: int, nnumbers: int) -> str:
    password: list[str] = []

    for _ in range(nletters):
        password.append(random.choice(character_set.LETTERS))
    for _ in range(nsymbols):
        password.append(random.choice(character_set.SYMBOLS))
    for _ in range(nnumbers):
        password.append(random.choice(character_set.NUMBERS))

    random.shuffle(password)
    return ''.join(password)
