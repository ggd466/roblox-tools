import json

def handle_request(data):
    try:
        json_data = json.loads(data)
        process_data(json_data)
    except json.JSONDecodeError:
        print("Invalid JSON data.")


def process_data(data):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"Processing {key}: {value}")
    else:
        print("Expected a dictionary.")


if __name__ == '__main__':
    sample_data = '{"name": "Roblox", "type": "game"}'
    handle_request(sample_data)