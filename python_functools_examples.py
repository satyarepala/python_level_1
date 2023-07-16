# functools_examples.py

import functools

# Example 1: Partial Functions
print("Example 1: Partial Functions")

# Using partial to create a new function with a fixed argument
def multiply(a, b):
    return a * b

double = functools.partial(multiply, b=2)
print("Double of 5:", double(5))  # Output: 10

triple = functools.partial(multiply, b=3)
print("Triple of 5:", triple(5))  # Output: 15

print()


# Example 2: Reduce
print("Example 2: Reduce")

from functools import reduce

# Using reduce to find the product of a list of numbers
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)  # Output: 120

print()


# Example 3: Cache with LRU
print("Example 3: Cache with LRU")

from functools import lru_cache

# A slow recursive function for Fibonacci numbers
@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 10:", fibonacci(10))  # Output: 55

print()


# Example 4: Wraps
print("Example 4: Wraps")

from functools import wraps

# A decorator using wraps to preserve function metadata
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    """A simple function that greets a person."""
    print(f"Hello, {name}!")

say_hello("Alice")
print("Function Name:", say_hello.__name__)  # Output: "say_hello"
print("Function Docstring:", say_hello.__doc__)  # Output: "A simple function that greets a person."

print()


# Example 5: Partial Method
print("Example 5: Partial Method")

from functools import partialmethod

class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # A method that uses partialmethod to fix an argument
    @partialmethod
    def multiply(self, factor):
        return self.x * self.y * factor

obj = MyClass(2, 3)
print("Result:", obj.multiply(4))  # Output: 24

print()

# ... Additional examples ...

