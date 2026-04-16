class RobloxError(Exception):
    """Base class for all exceptions related to Roblox."""
    pass

class AssetNotFoundError(RobloxError):
    """Raised when an asset cannot be found."""
    def __init__(self, asset_id):
        self.asset_id = asset_id
        super().__init__(f'Asset with ID {asset_id} not found.')

class PermissionDeniedError(RobloxError):
    """Raised when a user does not have permission."""
    def __init__(self, action):
        self.action = action
        super().__init__(f'Permission denied for action: {action}.')

class InvalidInputError(RobloxError):
    """Raised when the input is invalid."""
    def __init__(self, message):
        super().__init__(f'Invalid input: {message}')

class RobloxConnectionError(RobloxError):
    """Raised when a connection to Roblox fails."""
    def __init__(self, reason):
        self.reason = reason
        super().__init__(f'Connection failed: {reason}')

