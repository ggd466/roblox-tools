import json
from typing import Any, Dict, Union

class RobloxDataHandler:
    @staticmethod
    def parse_response(response: str) -> Union[Dict[str, Any], str]:
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return 'Invalid JSON response'

    @staticmethod
    def construct_payload(data: Dict[str, Any]) -> str:
        return json.dumps(data)

    @staticmethod
    def update_data(original: Dict[str, Any], updates: Dict[str, Any]) -> Dict[str, Any]:
        updated = original.copy()
        updated.update(updates)
        return updated

    @staticmethod
    def format_response(data: Dict[str, Any]) -> str:
        return json.dumps(data, indent=4)

if __name__ == '__main__':
    example_data = {'name': 'Roblox', 'type': 'Game'}
    print(RobloxDataHandler.format_response(example_data))
    response = '{"status": "success", "data": {}}'
    print(RobloxDataHandler.parse_response(response))