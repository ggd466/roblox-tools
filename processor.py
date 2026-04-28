import json
import logging

# Configure logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ProcessingError(Exception):
    pass

def process_data(data):
    if not isinstance(data, dict):
        logger.error('Invalid input: expected a dictionary')
        raise ProcessingError('Invalid input format')
    
    try:
        # Simulate data processing
        result = {key: value * 2 for key, value in data.items() if isinstance(value, (int, float))}
    except Exception as e:
        logger.exception('Error processing data')
        raise ProcessingError('Data processing failed') from e
    
    if not result:
        logger.warning('No numeric values found to process')
    return result

if __name__ == '__main__':
    data = {'a': 1, 'b': 2, 'c': 'three'}
    try:
        processed = process_data(data)
        print(json.dumps(processed, indent=2))
    except ProcessingError as e:
        logger.error(f'Processing failed: {e}')