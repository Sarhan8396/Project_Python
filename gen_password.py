import secrets
import string


def generate_secure_password(length):
    if length < 5:
        raise ValueError("Длина пароля должна быть минимум 5")

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    password = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols),
    ]

    all_chars = letters + digits + symbols

    for _ in range(length - 3):
        password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    return ''.join(password)


print(generate_secure_password(8))
print(generate_secure_password(9))
print(generate_secure_password(10))
