import json
import base64
from typing import Any, Dict

def roblox_data_handler(data: Dict[str, Any]) -> str:
    """
    Encodes Roblox data to a JSON string and base64
    :param data: Dictionary containing Roblox data
    :return: Base64 encoded JSON string
    """
    json_data = json.dumps(data)
    encoded_data = base64.b64encode(json_data.encode('utf-8')).decode('utf-8')
    return encoded_data


def decode_roblox_data(encoded_data: str) -> Dict[str, Any]:
    """
    Decodes Base64 encoded JSON string back to a dictionary
    :param encoded_data: Base64 encoded JSON string
    :return: Dictionary containing original Roblox data
    """
    decoded_json = base64.b64decode(encoded_data.encode('utf-8')).decode('utf-8')
    return json.loads(decoded_json)


def validate_roblox_data(data: Dict[str, Any]) -> bool:
    """
    Validates if the given Roblox data has required fields
    :param data: The Roblox data to validate
    :return: True if valid, False otherwise
    """
    required_fields = ['name', 'id', 'type']
    return all(field in data for field in required_fields)
