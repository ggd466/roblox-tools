import time
import random
import requests


def retry_request(url, retries=3, delay=1, backoff=2):
    for attempt in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < retries - 1:
                sleep_time = delay * (backoff ** attempt)
                print(f'Retrying in {sleep_time} seconds...')
                time.sleep(sleep_time)
            else:
                print('All attempts failed. Returning None.')  
    return None


# Example usage:
# result = retry_request('https://example.com/api/data')
# print(result)