import json
import os

DEFAULT_CONFIG = {
    'username': 'guest',
    'game_id': 0,
    'sensitivity': 0.5,
    'auto_join': True,
    'language': 'en'
}

class ConfigLoader:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.config = self.load_config()

    def load_config(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return self._merge_defaults(json.load(file))
        return DEFAULT_CONFIG

    def _merge_defaults(self, user_config):
        return {**DEFAULT_CONFIG, **user_config}

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get(self, key, default=None):
        return self.config.get(key, default)

    def set(self, key, value):
        self.config[key] = value
        self.save_config()

# Example of usage
if __name__ == '__main__':
    loader = ConfigLoader()
    print(loader.get('username'))
    loader.set('username', 'roblox_user')
    print(loader.get('username'))