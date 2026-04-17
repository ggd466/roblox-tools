import json

class RobloxDataHandler:
    def __init__(self, data):
        self.data = data

    def filter_data(self, filters):
        return [item for item in self.data if all(item.get(k) == v for k, v in filters.items())]

    def to_json(self):
        return json.dumps(self.data, indent=4)

    def from_json(self, json_str):
        self.data = json.loads(json_str)

    def get_unique_values(self, key):
        return set(item.get(key) for item in self.data if key in item)

# Example usage
if __name__ == '__main__':
    sample_data = [
        {'player_id': 1, 'name': 'PlayerOne', 'score': 150},
        {'player_id': 2, 'name': 'PlayerTwo', 'score': 200},
        {'player_id': 1, 'name': 'PlayerOne', 'score': 150}
    ]
    handler = RobloxDataHandler(sample_data)
    print(handler.to_json())
    unique_players = handler.get_unique_values('player_id')
    print(unique_players)