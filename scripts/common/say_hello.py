import random


def return_a_string() -> str:
    random_int = random.randint(0, 10000)
    return f"Random integer calculated: {random_int}"
