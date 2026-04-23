import time
import requests
from requests.exceptions import RequestException

def retry_request(url, max_retries=5, delay=2):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad HTTP response
            return response.json()  # Assuming we want JSON response
        except RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            attempt += 1
            time.sleep(delay)
            if attempt == max_retries:
                raise RuntimeError(f"Max retries exceeded for URL: {url}")
    return None

# Example usage:
# data = retry_request('https://api.example.com/data')
# print(data)