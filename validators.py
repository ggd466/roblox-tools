import re

class InputValidationError(Exception):
    pass

def validate_input(value):
    if not isinstance(value, str):
        raise InputValidationError("Input must be a string")
    if len(value) < 3:
        raise InputValidationError("Input must be at least 3 characters long")
    if not re.match("^[A-Za-z0-9_]*$, value):
        raise InputValidationError("Input must contain only alphanumeric characters or underscores")

    return True

def main_processing_loop(inputs):
    results = []
    for item in inputs:
        try:
            validate_input(item)
            results.append(f"Valid: {item}")
        except InputValidationError as e:
            results.append(f"Invalid: {item}, Reason: {str(e)}")
    return results

# Example usage
if __name__ == '__main__':
    sample_inputs = ["valid_input", "9", "!invalid!", 123, "ab"]
    print(main_processing_loop(sample_inputs))