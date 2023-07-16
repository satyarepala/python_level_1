# python_functions.py

# Python User-Defined Functions
def greet(name):
    """Function to greet a person"""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Function to add two numbers"""
    return a + b

greet("Alice")
result = add_numbers(5, 3)
print("Sum:", result)

# Python Anonymous Functions (Lambda Functions)
multiply = lambda x, y: x * y
print("Product:", multiply(4, 5))

# Loops and Statements in Python
# Example 1: For loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example 2: While loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Python Modules and Packages
# Example 3: Using functions from a module
import math

radius = 5
area = math.pi * math.pow(radius, 2)
print("Area of the circle:", area)

# Example 4: Using functions from a package
import random

random_number = random.randint(1, 100)
print("Random number:", random_number)


# python_functions.py

# Complex Examples of User-Defined Functions
def factorial(n):
    """Recursive function to calculate factorial"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} is:", factorial(num))

def fibonacci_sequence(n):
    """Function to generate Fibonacci sequence"""
    fib_list = [0, 1]
    for i in range(2, n):
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    return fib_list

fib_sequence = fibonacci_sequence(10)
print("Fibonacci sequence:", fib_sequence)

# Complex Examples of Anonymous Functions (Lambda Functions)
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_squares = reduce(lambda x, y: x + y**2, numbers, 0)
print("Sum of squares:", sum_of_squares)

# Complex Examples of Loops and Statements in Python
# Example 1: Nested loops
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

# Example 2: Using else with loops
def is_prime(num):
    """Function to check if a number is prime"""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Complex Examples of Python Modules and Packages
# Example 3: Using a user-defined module
import custom_module

print("Custom module description:", custom_module.get_description())
print("Area of a rectangle:", custom_module.calculate_rectangle_area(4, 5))

# Example 4: Using a function from a package in a module
import datetime
current_time = datetime.datetime.now()
print("Current date and time:", current_time)
