import re

def validate_input(input_data):
    if not isinstance(input_data, str):
        raise ValueError('Input must be a string')
    if not input_data:
        raise ValueError('Input cannot be empty')
    if len(input_data) > 100:
        raise ValueError('Input cannot exceed 100 characters')
    if not re.match('^[a-zA-Z0-9_]*$', input_data):
        raise ValueError('Input can only contain alphanumeric characters and underscores')
    return True

if __name__ == '__main__':
    test_inputs = [
        'valid_input',
        'anotherValid123',
        '',
        123,
        'invalid!@#$',
        'this_input_is_way_too_long_to_pass_validation_and_should_fail'
    ]
    for inp in test_inputs:
        try:
            validate_input(inp)
            print(f'"{inp}" is valid.')
        except ValueError as e:
            print(f'"{inp}" is invalid: {e}')
