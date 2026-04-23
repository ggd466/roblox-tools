import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, retries=3, backoff_factor=0.5):
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            if i < retries - 1:
                time.sleep(backoff_factor * (2 ** i))  # Exponential backoff
            else:
                raise NetworkError(f'Failed to fetch {url}: {e}') from e

# Example usage:
# data = retry_request('https://api.example.com/data')
# print(data)