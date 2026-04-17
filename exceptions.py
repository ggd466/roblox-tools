class RobloxError(Exception):
    """Base class for all Roblox exceptions."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class AssetNotFoundError(RobloxError):
    """Exception raised when an asset is not found."""
    def __init__(self, asset_id):
        super().__init__(f'Asset with ID {asset_id} not found.')
        self.asset_id = asset_id

class UserNotFoundError(RobloxError):
    """Exception raised when a user is not found."""
    def __init__(self, username):
        super().__init__(f'User with username {username} not found.')
        self.username = username

class PermissionDeniedError(RobloxError):
    """Exception raised for permission errors."""
    def __init__(self, action):
        super().__init__(f'Permission denied for action: {action}.')
        self.action = action

class InvalidInputError(RobloxError):
    """Exception raised for invalid input errors."""
    def __init__(self, input_value):
        super().__init__(f'Invalid input: {input_value}.')
        self.input_value = input_value

class OperationFailedError(RobloxError):
    """Exception raised when an operation fails."""
    def __init__(self, operation):
        super().__init__(f'Operation failed: {operation}.')
        self.operation = operation