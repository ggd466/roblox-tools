import json
import random
import string

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


def read_json_file(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def write_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return float('inf')  # Return infinity if denominator is zero


def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]
