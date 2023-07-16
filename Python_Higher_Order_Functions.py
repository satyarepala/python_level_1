# simple examples

# Example 1: map() - Applies a function to all elements of a sequence
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example 2: filter() - Filters elements from a sequence based on a function condition
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Example 3: reduce() - Combines elements of a sequence into a single value using a function
from functools import reduce

def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # Output: 15

# Example 4: lambda functions - Anonymous functions used as arguments to higher-order functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15

# Example 5: sorted() - Sorts a sequence based on a function/key
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
sorted_names = sorted(names, key=lambda name: len(name))
print(sorted_names)  # Output: ['Bob', 'Eve', 'Alice', 'David', 'Charlie']


# Complex Examples - Higher-Order Functions

# Example 1: Using map() and filter() together
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_squares = list(map(lambda x: x ** 2, filter(is_prime, numbers)))
print(prime_squares)  # Output: [4, 9, 25, 49]

# Example 2: Using reduce() with lambda to find the maximum element in a list
from functools import reduce

numbers = [21, 8, 36, 12, 45]
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # Output: 45

# Example 3: Sorting a list of dictionaries based on a specific key using sorted() and lambda
students = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 22},
    {'name': 'David', 'age': 28}
]

sorted_students = sorted(students, key=lambda x: x['age'])
print(sorted_students)
# Output: [{'name': 'Charlie', 'age': 22},
#          {'name': 'Alice', 'age': 25},
#          {'name': 'David', 'age': 28},
#          {'name': 'Bob', 'age': 30}]

# Example 4: Using map() and filter() to transform and filter a list of strings
def remove_vowels(word):
    vowels = 'aeiou'
    return ''.join(filter(lambda letter: letter.lower() not in vowels, word))

words = ["apple", "banana", "orange", "grape"]
modified_words = list(map(remove_vowels, words))
print(modified_words)  # Output: ['ppl', 'bnn', 'rng', 'grp']

# Example 5: Using reduce() to find the product of elements in a list
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120


# More Complex Examples - Higher-Order Functions

# Example 1: Using map(), filter(), and reduce() together
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

numbers = [1, 2, 3, 4, 5]
factorials_of_odds = list(map(factorial, filter(lambda x: x % 2 != 0, numbers)))
print(factorials_of_odds)  # Output: [1, 6, 120]

# Example 2: Higher-order function with a function as an argument
def apply_operation(operation, x, y):
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(add, 3, 5)
print(result1)  # Output: 8

result2 = apply_operation(multiply, 3, 5)
print(result2)  # Output: 15

# Example 3: Higher-order function with a function returning a function
def power(x):
    def inner_power(y):
        return y ** x
    return inner_power

square = power(2)
cube = power(3)

print(square(4))  # Output: 16
print(cube(3))    # Output: 27

# Example 4: Using map() and lambda to apply multiple functions to a list
def double(x):
    return x * 2

def add_one(x):
    return x + 1

def subtract_five(x):
    return x - 5

numbers = [1, 2, 3, 4, 5]
transformed_numbers = list(map(lambda x: subtract_five(add_one(double(x))), numbers))
print(transformed_numbers)  # Output: [-3, -1, 1, 3, 5]

# Example 5: Using filter() and lambda to find common elements in multiple lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

common_elements = list(filter(lambda x: x in list2 and x in list3, list1))
print(common_elements)  # Output: [5]

# Example 6: Using reduce() and lambda to find the longest string in a list
strings = ["apple", "banana", "orange", "grape", "kiwi"]
longest_string = reduce(lambda x, y: x if len(x) > len(y) else y, strings)
print(longest_string)  # Output: "banana"
