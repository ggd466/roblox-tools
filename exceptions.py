class RobloxError(Exception):
    """Base class for all Roblox exceptions."""
    pass

class InvalidInputError(RobloxError):
    """Raised when input validation fails."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ResourceNotFoundError(RobloxError):
    """Raised when a resource is not found."""
    def __init__(self, resource):
        self.resource = resource
        self.message = f'{resource} not found.'
        super().__init__(self.message)

class PermissionDeniedError(RobloxError):
    """Raised when user lacks permissions."""
    def __init__(self, user):
        self.user = user
        self.message = f'Permission denied for user: {user}'
        super().__init__(self.message)

def handle_error(e):
    if isinstance(e, InvalidInputError):
        print(f'Invalid input: {e.message}')
    elif isinstance(e, ResourceNotFoundError):
        print(f'Error: {e.message}')
    elif isinstance(e, PermissionDeniedError):
        print(f'Access Error: {e.message}')
    else:
        print('An unexpected error occurred: ', str(e))

# Example usage
try:
    raise InvalidInputError('Negative value not allowed')
except RobloxError as ex:
    handle_error(ex)