import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RobloxError(Exception):
    pass

class Handler:
    def __init__(self, data):
        self.data = data

    def process_data(self):
        try:
            self.validate_data()
            result = self.perform_action()
            return result
        except RobloxError as e:
            logging.error(f'RobloxError encountered: {str(e)}')
            return {'error': str(e)}
        except Exception as e:
            logging.error(f'Unexpected error: {str(e)}')
            return {'error': 'An unexpected error occurred.'}

    def validate_data(self):
        if not isinstance(self.data, dict):
            raise RobloxError('Data must be a dictionary.')
        if 'action' not in self.data:
            raise RobloxError('The key `action` is missing.')

    def perform_action(self):
        action = self.data['action']
        if action == 'create':
            return self.create_entity()
        elif action == 'delete':
            return self.delete_entity()
        else:
            raise RobloxError('Invalid action specified.')

    def create_entity(self):
        return json.dumps({'status': 'Entity created successfully.'})

    def delete_entity(self):
        return json.dumps({'status': 'Entity deleted successfully.'})

# Example usage
if __name__ == '__main__':
    handler = Handler({'action': 'create'})
    print(handler.process_data())
    
    handler = Handler({'action': 'invalid'})
    print(handler.process_data())
    
    handler = Handler('invalid_data')
    print(handler.process_data())