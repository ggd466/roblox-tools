class RobloxError(Exception):
    """Base class for Roblox exceptions."""
    pass

class NotFoundError(RobloxError):
    """Exception raised when a resource is not found."""

    def __init__(self, resource: str, *args: object) -> None:
        """Initialize NotFoundError with resource details.

        Args:
            resource (str): The name of the missing resource.
            *args (object): Additional arguments for the exception.
        """
        super().__init__(f"Resource '{resource}' not found.", *args)
        self.resource = resource

class PermissionDeniedError(RobloxError):
    """Exception raised for permission-related errors."""

    def __init__(self, action: str, *args: object) -> None:
        """Initialize PermissionDeniedError with action details.

        Args:
            action (str): The action for which permission was denied.
            *args (object): Additional arguments for the exception.
        """
        super().__init__(f"Permission denied for action: '{action}'.", *args)
        self.action = action

class RateLimitExceededError(RobloxError):
    """Exception raised when rate limits are exceeded."""

    def __init__(self, limit: int, *args: object) -> None:
        """Initialize RateLimitExceededError with limit details.

        Args:
            limit (int): The rate limit that was exceeded.
            *args (object): Additional arguments for the exception.
        """
        super().__init__(f"Rate limit of {limit} exceeded.", *args)
        self.limit = limit
