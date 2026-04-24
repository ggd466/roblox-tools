import re

def validate_username(username):
    return isinstance(username, str) and 3 <= len(username) <= 20 and re.match('^[a-zA-Z0-9_]+$', username)


def validate_email(email):
    return isinstance(email, str) and re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)


def validate_password(password):
    return isinstance(password, str) and len(password) >= 8 and any(c.isdigit() for c in password) and any(c.isalpha() for c in password)


def input_validation_loop():
    while True:
        username = input('Enter username: ')
        if not validate_username(username):
            print('Invalid username. Must be 3-20 characters with letters, numbers, and underscores. Try again.')
            continue

        email = input('Enter email: ')
        if not validate_email(email):
            print('Invalid email format. Try again.')
            continue

        password = input('Enter password: ')
        if not validate_password(password):
            print('Invalid password. Must be at least 8 characters, include letters and numbers. Try again.')
            continue

        print('All inputs are valid!')
        break