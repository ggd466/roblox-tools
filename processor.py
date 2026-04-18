import json

class RobloxDataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_by_attribute(self, attribute, value):
        return [item for item in self.data if item.get(attribute) == value]

    def sort_by_attribute(self, attribute, reverse=False):
        return sorted(self.data, key=lambda x: x.get(attribute), reverse=reverse)

    def convert_to_json(self):
        return json.dumps(self.data)

    def from_json(self, json_str):
        try:
            self.data = json.loads(json_str)
        except json.JSONDecodeError:
            raise ValueError('Invalid JSON data')

# Example usage:
if __name__ == '__main__':
    sample_data = [
        {'name': 'Player1', 'score': 150},
        {'name': 'Player2', 'score': 200},
        {'name': 'Player3', 'score': 100}
    ]
    processor = RobloxDataProcessor(sample_data)
    filtered_data = processor.filter_by_attribute('score', 200)
    sorted_data = processor.sort_by_attribute('score', reverse=True)
    json_data = processor.convert_to_json()
    print(filtered_data, sorted_data, json_data)