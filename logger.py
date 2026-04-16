import logging
import time

class PerformanceLogger:
    def __init__(self, name='PerformanceLogger'):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(name)

    def log_performance(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            self.logger.info(f'Function {func.__name__} executed in {execution_time:.5f} seconds')
            return result
        return wrapper

@PerformanceLogger().log_performance
def example_function(duration):
    time.sleep(duration)

if __name__ == '__main__':
    example_function(2)