# Loops and Conditional Statements Examples

# Example 1: for loop to print numbers from 1 to 5
for num in range(1, 6):
    print(num)
# Output:
# 1
# 2
# 3
# 4
# 5

# Example 2: while loop to print even numbers from 2 to 10
num = 2
while num <= 10:
    print(num)
    num += 2
# Output:
# 2
# 4
# 6
# 8
# 10

# Example 3: for loop with conditional statement to print odd numbers from 1 to 9
for num in range(1, 10):
    if num % 2 != 0:
        print(num)
# Output:
# 1
# 3
# 5
# 7
# 9

# Example 4: while loop with conditional statement to find the sum of numbers from 1 to 10
total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(total)  # Output: 55

# Example 5: for loop to iterate through a list and use a conditional statement
fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)
# Output:
# banana
# orange

# Example 6: nested for loop to create a multiplication table
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}")
# Output:
# 1 x 1 = 1
# 1 x 2 = 2
# 1 x 3 = 3
# 1 x 4 = 4
# 1 x 5 = 5
# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 3 x 1 = 3
# ...
# 5 x 5 = 25

# Example 7: if-elif-else conditional statements
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is {grade}")
# Output: Your grade is B

# complex_loops.py

# Example 1: Nested loops - Multiplication table
for i in range(1, 11):
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Add a blank line after each row of the table

# Example 2: Looping through a list of dictionaries
students = [
    {"name": "Alice", "age": 20, "major": "Computer Science"},
    {"name": "Bob", "age": 22, "major": "Engineering"},
    {"name": "Charlie", "age": 19, "major": "Mathematics"}
]

for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Example 3: Loop with else block
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"Even number found: {num}")
        break
else:
    print("No even number found in the list.")

# Example 4: Looping with continue and break
for i in range(1, 11):
    if i == 3:
        continue  # Skip printing 3 and continue to the next iteration
    if i == 8:
        break  # Exit the loop when i is 8
    print(i)

# Example 5: Looping with enumerate
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# Example 6: Looping with zip
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 22]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


# Complex Examples - Loops and Conditional Statements

# Example 1: Generating Fibonacci sequence up to a given limit
def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number > limit:
            break
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence

limit = 100
fibonacci_seq = generate_fibonacci(limit)
print(fibonacci_seq)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Example 2: FizzBuzz - Print numbers from 1 to 100, but replace multiples of 3 with "Fizz",
# multiples of 5 with "Buzz", and multiples of both with "FizzBuzz"
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# Example 3: Generating a multiplication table using a nested list comprehension
multiplication_table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
for row in multiplication_table:
    print(row)
# Output: Each row represents the multiplication table from 1 to 10

# Example 4: Collatz conjecture - Generate the sequence for a given number until it reaches 1
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

number = 12
collatz_seq = collatz_sequence(number)
print(collatz_seq)  # Output: [12, 6, 3, 10, 5, 16, 8, 4, 2, 1]

# Example 5: Finding the common elements in multiple lists using a list comprehension
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

common_elements = [num for num in list1 if num in list2 and num in list3]
print(common_elements)  # Output: [5]

# Complex Examples - Integer Division (//) in Python

# Example 1: Calculating average without using floating-point division
def calculate_average(scores):
    total_sum = sum(scores)
    number_of_scores = len(scores)
    average = total_sum // number_of_scores
    return average

scores = [85, 92, 78, 95, 88]
average_score = calculate_average(scores)
print(average_score)  # Output: 87

# Example 2: Implementing a function to find the n-th digit from the right of a number
def find_nth_digit(number, n):
    if n < 1:
        raise ValueError("n must be a positive integer.")
    return (number // 10**(n - 1)) % 10

number = 987654321
nth_digit = find_nth_digit(number, 3)
print(nth_digit)  # Output: 7

# Example 3: Converting seconds to hours, minutes, and remaining seconds
def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

total_seconds = 9876
hours, minutes, seconds = convert_seconds_to_time(total_seconds)
print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
# Output: 2 hours, 44 minutes, 36 seconds

# Example 4: Implementing a function to find the quotient and remainder of division
def divide_with_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

numerator = 17
denominator = 5
quotient, remainder = divide_with_remainder(numerator, denominator)
print(f"Quotient: {quotient}, Remainder: {remainder}")
# Output: Quotient: 3, Remainder: 2

# Example 5: Simulating a vending machine to calculate the number of items to return as change
def calculate_change(total_amount, item_price):
    change_amount = total_amount - item_price
    num_quarters = change_amount // 25
    change_amount %= 25
    num_dimes = change_amount // 10
    change_amount %= 10
    num_nickels = change_amount // 5
    change_amount %= 5
    num_pennies = change_amount
    return num_quarters, num_dimes, num_nickels, num_pennies

total_amount_paid = 100
item_cost = 67
quarters, dimes, nickels, pennies = calculate_change(total_amount_paid, item_cost)
print(f"Change: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")
# Output: Change: 1 quarters, 1 dimes, 1 nickels, 3 pennies

