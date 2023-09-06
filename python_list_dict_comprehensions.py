# List Comprehensions
# Example 1: Creating a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]

# Example 2: Generating a list of squares for even numbers from 1 to 10
even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]

# Example 3: Converting a list of temperatures from Celsius to Fahrenheit
celsius_temperatures = [0, 10, 20, 30, 40]
fahrenheit_temperatures = [(temp * 9/5) + 32 for temp in celsius_temperatures]

# Dictionary Comprehensions
# Example 4: Creating a dictionary of squares for numbers from 1 to 5
squares_dict = {x: x ** 2 for x in range(1, 6)}

# Example 5: Filtering items in a dictionary based on values
fruits = {'apple': 3, 'banana': 5, 'cherry': 2, 'date': 4}
popular_fruits = {key: value for key, value in fruits.items() if value >= 3}

# Display Results
print("Even Numbers:", even_numbers)
print("Even Squares:", even_squares)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
print("Dictionary of Squares:", squares_dict)
print("Popular Fruits:", popular_fruits)

print("-----------------------------------------------------", "\n")
print("Complex Examples:")
#COMPLEX examples
# List Comprehensions with 'else'
# Example 1: Create a list of squares for numbers from 1 to 5; if the number is odd, add 1 instead
squares_with_else = [x ** 2 if x % 2 == 0 else x + 1 for x in range(1, 6)]

# Example 2: Create a list of positive, negative, or zero based on the sign of the numbers
numbers = [-3, 7, 0, -2, 9, -1]
signs = ['Positive' if x > 0 else 'Negative' if x < 0 else 'Zero' for x in numbers]

# Dictionary Comprehensions with 'else'
# Example 3: Create a dictionary with even and odd numbers
even_odd_dict = {x: 'Even' if x % 2 == 0 else 'Odd' for x in range(1, 6)}

# Example 4: Filter items in a dictionary based on values and set a default value for filtered items
fruits = {'apple': 3, 'banana': 5, 'cherry': 2, 'date': 4}
filtered_fruits = {key: value if value >= 3 else 'Not Popular' for key, value in fruits.items()}

# Display Results
print("Squares with 'else':", squares_with_else)
print("Signs of Numbers:", signs)
print("Even-Odd Dictionary:", even_odd_dict)
print("Filtered Fruits:", filtered_fruits)