def even_numbers_generator(limit):
    """
    Generates even numbers from 2 up to the specified limit.

    Args:
        limit (int): The upper limit for even numbers.

    Yields:
        int: Even numbers from 2 up to the limit.
    """
    num = 2
    while num <= limit:
        yield num
        num += 2


# Example usage:
limit = 10  # You can change the limit as needed
even_gen = even_numbers_generator(limit)

print(next(even_gen))
print(next(even_gen))