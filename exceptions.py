class RobloxError(Exception):
    """Base class for exceptions in Roblox tools."""

class InvalidInputError(RobloxError):
    """Raised when an invalid input is provided."""

class ConnectionError(RobloxError):
    """Raised for connection-related issues."""

class NotFoundError(RobloxError):
    """Raised when an expected resource is not found."""

class UnauthorizedAccessError(RobloxError):
    """Raised when access to a resource is denied."""

# Example of usage in a function:

def fetch_user_data(user_id):
    if not isinstance(user_id, int) or user_id <= 0:
        raise InvalidInputError("User ID must be a positive integer")
    try:
        # Simulate fetching user data
        user_data = get_data_from_api(user_id)  # Hypothetical function
        if user_data is None:
            raise NotFoundError(f"User with ID {user_id} not found")
        return user_data
    except ConnectionError:
        print("Failed to connect to the server. Please try again later.")
    except UnauthorizedAccessError:
        print("You do not have permission to access this resource.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
