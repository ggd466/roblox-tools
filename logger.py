import logging

# Configuring the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

def log_input_validation(func):
    def wrapper(*args, **kwargs):
        input_data = args[0] if args else None
        if not isinstance(input_data, dict):
            raise ValueError('Input must be a dictionary')
        if 'user_id' not in input_data:
            raise ValueError('Input must contain user_id')
        return func(*args, **kwargs)
    return wrapper

@log_input_validation
def process_input(input_data):
    logger = Logger('InputProcessor')
    logger.info(f'Starting to process: {input_data}')
    # Processing logic here
    logger.info('Processing complete')

# Example usage
if __name__ == '__main__':
    try:
        process_input({'user_id': 123, 'action': 'jump'})  # Valid input
        process_input('invalid_input')  # Invalid input will raise ValueError
    except ValueError as e:
        logging.error(e)