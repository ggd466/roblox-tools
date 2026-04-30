import math

class RobloxHelper:
    @staticmethod
    def calculate_distance(point1, point2):
        """Calculate the distance between two points in 3D space."""
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2 + (point2[2] - point1[2]) ** 2)

    @staticmethod
    def format_currency(amount):
        """Format the number to Roblox currency style (e.g., 1,000,000)"""
        return f'${amount:,.2f}'

    @staticmethod
    def find_closest_player(player_position, players):
        """Find the closest player to a given position."""
        closest_player = None
        closest_distance = float('inf')
        for player in players:
            distance = RobloxHelper.calculate_distance(player_position, player['position'])
            if distance < closest_distance:
                closest_distance = distance
                closest_player = player
        return closest_player

    @staticmethod
    def clamp(value, min_value, max_value):
        """Clamp a value between min and max."""
        return max(min_value, min(value, max_value))

    @staticmethod
    def is_valid_username(username):
        """Check if the username is valid in Roblox (length, characters)."""
        return 3 <= len(username) <= 20 and username.isalnum()