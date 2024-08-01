import string
import random


def generate_password(length, include_symbols=True, include_uppercase=True,include_digits=True):
    # selected_characters = list("%_,.*[|/:(`:£\\})>$_\£--=")
    selected_characters = list(string.ascii_lowercase)\
    
    if include_symbols:
        selected_characters += list("%_,.*[|/:(`:£\\})>$_\£--=")
    if include_uppercase:
        selected_characters += list(string.ascii_uppercase)
    if include_digits:
        selected_characters += list(string.digits)

    password = ''.join(random.choice(selected_characters) for _ in range(length))
    return password


