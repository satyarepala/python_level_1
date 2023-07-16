# sets_and_tuples.py

# Examples of Sets

# Example 1: Creating a set
fruits = {'apple', 'banana', 'cherry'}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Example 2: Adding elements to a set
fruits.add('orange')
print(fruits)  # Output: {'orange', 'apple', 'banana', 'cherry'}

# Example 3: Removing elements from a set
fruits.remove('banana')
print(fruits)  # Output: {'orange', 'apple', 'cherry'}

# Example 4: Set union
fruits_2 = {'banana', 'grape', 'kiwi'}
all_fruits = fruits.union(fruits_2)
print(all_fruits)  # Output: {'orange', 'apple', 'cherry', 'grape', 'kiwi'}

# Example 5: Set intersection
common_fruits = fruits.intersection(fruits_2)
print(common_fruits)  # Output: set()

# Example 6: Checking for membership in a set
print('apple' in fruits)  # Output: True
print('mango' in fruits)  # Output: False

# Examples of Tuples

# Example 7: Creating a tuple
person = ('John', 30, 'Male')
print(person)  # Output: ('John', 30, 'Male')

# Example 8: Accessing elements of a tuple
name = person[0]
age = person[1]
gender = person[2]
print(name, age, gender)  # Output: John 30 Male

# Example 9: Unpacking a tuple
name, age, gender = person
print(name, age, gender)  # Output: John 30 Male

# Example 10: Combining tuples
address = ('123 Main Street', 'City', 'Country')
person_with_address = person + address
print(person_with_address)  # Output: ('John', 30, 'Male', '123 Main Street', 'City', 'Country')

# Example 11: Nested tuples
nested_tuple = (1, 2, (3, 4))
print(nested_tuple)  # Output: (1, 2, (3, 4))

# Example 12: Counting occurrences of an element in a tuple
numbers = (1, 2, 3, 4, 3, 3)
count_of_three = numbers.count(3)
print(count_of_three)  # Output: 3


# complex_sets_and_tuples.py

# Complex Examples of Sets

# Example 1: Removing duplicates from a list using set
numbers_with_duplicates = [1, 2, 3, 2, 4, 3, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(unique_numbers)  # Output: [1, 2, 3, 4, 5]

# Example 2: Finding common elements in multiple sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 6, 7, 8}
common_elements = set1.intersection(set2, set3)
print(common_elements)  # Output: {4}

# Example 3: Set difference and symmetric difference
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}
difference_AB = setA.difference(setB)
symmetric_difference_AB = setA.symmetric_difference(setB)
print(difference_AB)         # Output: {1, 2}
print(symmetric_difference_AB)  # Output: {1, 2, 5, 6}

# Complex Examples of Tuples

# Example 4: Using tuples in list comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [(x, x**2) for x in numbers]
print(squared_numbers)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# Example 5: Returning multiple values from a function using a tuple
def calculate_sum_and_product(a, b):
    return a + b, a * b

sum_result, product_result = calculate_sum_and_product(3, 4)
print("Sum:", sum_result)        # Output: Sum: 7
print("Product:", product_result)  # Output: Product: 12

# Example 6: Sorting a list of tuples based on a specific element
students = [("Alice", 25), ("Bob", 22), ("Charlie", 30)]
students_sorted_by_age = sorted(students, key=lambda x: x[1])
print(students_sorted_by_age)  # Output: [('Bob', 22), ('Alice', 25), ('Charlie', 30)]

# Example 7: Creating a dictionary from a list of tuples
fruits_with_prices = [("apple", 0.5), ("banana", 0.3), ("cherry", 0.8)]
fruits_dict = dict(fruits_with_prices)
print(fruits_dict)  # Output: {'apple': 0.5, 'banana': 0.3, 'cherry': 0.8}

# Example 8: Unpacking nested tuples
nested_tuple = (1, 2, (3, 4))
first, second, (third, fourth) = nested_tuple
print(first, second, third, fourth)  # Output: 1 2 3 4

