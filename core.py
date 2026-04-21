import logging

class RobloxError(Exception):
    pass

class RobloxAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.roblox.com/'
        self.logger = logging.getLogger(__name__)

    def fetch_data(self, endpoint):
        try:
            url = f'{self.base_url}{endpoint}'
            response = self.make_request(url)
            return response.json()
        except ValueError as ve:
            self.logger.error(f'ValueError: {ve}')
            raise RobloxError('Failed to decode JSON response.')
        except Exception as e:
            self.logger.error(f'Unexpected error: {e}')
            raise RobloxError('An error occurred while fetching data.')

    def make_request(self, url):
        import requests
        try:
            response = requests.get(url, headers={'Authorization': f'Bearer {self.api_key}'})
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            self.logger.error(f'HTTP error occurred: {http_err}')
            raise RobloxError(f'HTTP error: {http_err}')
        except requests.exceptions.Timeout:
            self.logger.error('Request timed out')
            raise RobloxError('The request timed out.')
        except requests.exceptions.RequestException as req_err:
            self.logger.error(f'Request exception: {req_err}')
            raise RobloxError('An error occurred while making the request.')

# Sample usage
if __name__ == '__main__':
    api = RobloxAPI('your_api_key')
    try:
        data = api.fetch_data('some-endpoint')
        print(data)
    except RobloxError as e:
        print(f'Error: {e}')