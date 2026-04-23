import re

def validate_input(user_input):
    if not isinstance(user_input, str):
        raise ValueError("Input must be a string.")
    if len(user_input) < 1:
        raise ValueError("Input cannot be empty.")
    if not re.match("^[A-Za-z0-9_]*$, user_input):
        raise ValueError("Input can only contain alphanumeric characters and underscores.")
    return True

def process_data(data):
    try:
        validate_input(data)
        print(f"Processing {data}...")
        # Simulate processing
        return f"Processed: {data}"
    except ValueError as e:
        print(f"Input validation error: {e}")
        return None

if __name__ == '__main__':
    sample_input = "valid_input_123"
    result = process_data(sample_input)
    print(result)

    invalid_input = "!invalid@input#"
    result = process_data(invalid_input)
    print(result)