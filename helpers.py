import time
import random
from typing import Callable, TypeVar, Any

T = TypeVar('T')

def retry_operation(func: Callable[..., T], retries: int = 5, delay: float = 2.0) -> T:
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            print(f'Attempt {attempt + 1} failed: {e}')
            if attempt < retries - 1:
                backoff = delay * (2 ** attempt) + random.uniform(0, 1)
                print(f'Retrying in {backoff:.2f} seconds...')
                time.sleep(backoff)
            else:
                print('All attempts failed.')
                raise

# Example usage:
if __name__ == '__main__':
    def network_request():
        if random.random() < 0.7:
            raise Exception('Network error')  # Simulating network failure
        return 'Success'

    try:
        result = retry_operation(network_request)
        print(result)
    except Exception:
        print('Operation failed after retries.')