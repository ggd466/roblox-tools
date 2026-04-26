
# Constants used throughout the Roblox tools project

from typing import Final

# Base URL for the Roblox API
API_BASE_URL: Final[str] = "https://api.roblox.com/"

# Default timeout for API requests in seconds
DEFAULT_TIMEOUT: Final[int] = 30

# User roles in Roblox
USER_ROLES: Final[dict[str, int]] = {
    "Admin": 1,
    "Moderator": 2,
    "User": 3,
    "Guest": 4,
}

# Default values for in-game settings
DEFAULT_SETTINGS: Final[dict[str, bool]] = {
    "music_enabled": True,
    "sound_effects": True,
    "notifications": True,
}

# Player status constants
PLAYER_STATUS_ACTIVE: Final[str] = "active"
PLAYER_STATUS_INACTIVE: Final[str] = "inactive"
PLAYER_STATUS_BANNED: Final[str] = "banned"

# Game environment types
ENVIRONMENTS: Final[list[str]] = ["testing", "development", "production"]

#  Error messages for the application
ERROR_MESSAGES: Final[dict[str, str]] = {
    "invalid_user": "User does not exist.",
    "permission_denied": "You do not have permission to perform this action.",
}
