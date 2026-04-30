import time

def optimized_process(data):
    start_time = time.time()
    processed_data = []
    for item in data:
        processed_data.append(item ** 2)  # Example processing step
    end_time = time.time()
    print(f"Processing took {end_time - start_time:.2f} seconds")
    return processed_data

if __name__ == '__main__':
    sample_data = range(1, 100000)
    result = optimized_process(sample_data)
    print(f"Processed {len(result)} items.")