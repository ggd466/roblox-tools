import re

class Validator:
    @staticmethod
    def is_valid_username(username):
        # Alphanumeric check and length
        return re.match(r'^[A-Za-z0-9]{3,20}$', username) is not None

    @staticmethod
    def is_valid_password(password):
        # At least 8 characters, one upper, one number
        return (len(password) >= 8 and
                re.search(r'[A-Z]', password) and
                re.search(r'[0-9]', password))

    @staticmethod
    def is_valid_email(email):
        # Basic email format check
        return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email) is not None

    @staticmethod
    def validate_user_data(username, password, email):
        return (Validator.is_valid_username(username) and
                Validator.is_valid_password(password) and
                Validator.is_valid_email(email))

if __name__ == '__main__':
    print(Validator.validate_user_data('User123', 'Password1', 'user@example.com'))