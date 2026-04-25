from typing import Dict, Any
import os

class Config:
    """
    Configuration class to handle application settings.
    """
    def __init__(self, config_file: str) -> None:
        """
        Initialize the Config with a configuration file.
        
        :param config_file: Path to the configuration file.
        """
        self.settings: Dict[str, Any] = self.load_config(config_file)

    def load_config(self, config_file: str) -> Dict[str, Any]:
        """
        Load configuration settings from a file.
        
        :param config_file: Path to the configuration file.
        :return: Dictionary of configuration settings.
        """
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Config file not found: {config_file}")

        with open(config_file, 'r') as file:
            content = file.read()
        return self.parse_content(content)

    def parse_content(self, content: str) -> Dict[str, Any]:
        """
        Parse the configuration content into a dictionary.
        
        :param content: Raw configuration file content.
        :return: Parsed settings as a dictionary.
        """
        settings: Dict[str, Any] = {}
        for line in content.splitlines():
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                settings[key.strip()] = value.strip()
        return settings

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a configuration value by its key.
        
        :param key: The key of the setting to retrieve.
        :param default: The default value to return if key not found.
        :return: The configuration value or default if not found.
        """  
        return self.settings.get(key, default)