import json
import os


def load_json(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"{file_path} not found")
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def list_directory_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


def pretty_print(data):
    print(json.dumps(data, indent=4, sort_keys=True))


def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}


def ensure_list(item):
    return item if isinstance(item, list) else [item]