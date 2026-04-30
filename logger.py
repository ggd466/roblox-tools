import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(log_file='app.log', max_bytes=10**6, backup_count=5):
    logger = logging.getLogger('rotating_logger')
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        # Create a directory for logs if it doesn't exist
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)
        # Create a rotating file handler
        handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up and ready to go!')