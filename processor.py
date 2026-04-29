import json
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self, data):
        self.data = data
        logger.debug('DataProcessor initialized')

    def process(self):
        logger.info('Processing data')
        return self._transform_data(self.data)

    def _transform_data(self, data):
        logger.debug('Transforming data')
        return [self._process_item(item) for item in data]

    def _process_item(self, item):
        logger.debug(f'Processing item: {item}')
        # Simulate a transformation
        return {key: self._sanitize(value) for key, value in item.items()}

    def _sanitize(self, value):
        if isinstance(value, str):
            sanitized_value = value.strip().lower()
            logger.debug(f'Sanitized value: {sanitized_value}')
            return sanitized_value
        return value

    def to_json(self):
        logger.info('Converting data to JSON')
        return json.dumps(self.process())

if __name__ == '__main__':
    sample_data = [ {'name': ' Roblox  '}, {'name': '  script '} ]
    processor = DataProcessor(sample_data)
    print(processor.to_json())