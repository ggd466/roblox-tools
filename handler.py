import json
import requests

class RobloxDataHandler:
    BASE_URL = 'https://api.roblox.com/'

    def __init__(self, username):
        self.username = username
        self.user_id = self.get_user_id()

    def get_user_id(self):
        response = requests.get(f'{self.BASE_URL}users/get-by-username?username={self.username}')
        if response.status_code == 200:
            return response.json().get('Id')
        raise ValueError('Username not found')

    def get_user_stats(self):
        stats_url = f'{self.BASE_URL}users/{self.user_id}/stats'
        response = requests.get(stats_url)
        if response.status_code == 200:
            return response.json()
        raise ValueError('Could not retrieve user stats')

    def save_stats_to_file(self, filename):
        stats = self.get_user_stats()
        with open(filename, 'w') as file:
            json.dump(stats, file, indent=4)
        print(f'Stats saved to {filename}')  

# Example usage, uncomment to run:
# handler = RobloxDataHandler('exampleUsername')
# handler.save_stats_to_file('user_stats.json')
