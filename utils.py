import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Execution time of {func.__name__}: {end_time - start_time:.4f} seconds')
        return result
    return wrapper

@time_it
def expensive_operation(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

@time_it
def optimized_operation(n):
    return sum(i ** 2 for i in range(n))

# Example usage
if __name__ == '__main__':
    print(expensive_operation(10000))
    print(optimized_operation(10000))