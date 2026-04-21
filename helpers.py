import time
import random
import requests

def retry_request(url, method='GET', retries=3, delay=2, backoff=2, **kwargs):
    for attempt in range(retries):
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                sleep_time = delay * (backoff ** attempt)
                print(f'Attempt {attempt + 1} failed: {e}. Retrying in {sleep_time} seconds...')
                time.sleep(sleep_time)
            else:
                print(f'All attempts failed. Last exception: {e}')
                raise
    return None

# Example usage - Uncomment to test
# response = retry_request('https://example.com/api/data')
# print(response.json())