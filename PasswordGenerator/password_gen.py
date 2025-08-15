# Password generator
# At least 12 characters, mix of upper and lowercase, includes numbers and special characters.

import string
import secrets
# import random

def generate_password(password_len = 14):
    letters = string.ascii_letters
    numbers = string.digits
    specialChars = string.punctuation

    passwordComponents = letters + numbers + specialChars

    # Deleted this, but this also worked. Just less control over components.
    # password_as_chars = random.sample(passwordComponents, password_len)
    # password_as_str = "".join(password_as_chars)

    password_is_strong = False
    pwd = ''

    while not password_is_strong:
        pwd = ''
        pwd += ''.join(secrets.choice(passwordComponents) for i in range(password_len))
        if (any(char in specialChars for char in pwd) and
            sum(char in numbers for char in pwd) >= 3):
            password_is_strong = True

    return pwd