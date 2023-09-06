# Basic Lambda Function
basic_lambda = lambda x: x * 2
result_basic = basic_lambda(5)

# Lambda Function with Multiple Arguments
multiply_lambda = lambda x, y: x * y
result_multiply = multiply_lambda(3, 4)

# Using Lambda in a List Comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [(lambda x: x ** 2)(x) for x in numbers]

# Lambda for Conditional Logic
even_or_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd'
result_even_or_odd = even_or_odd(7)

# Display Results
print("Basic Lambda:", result_basic)
print("Multiply Lambda:", result_multiply)
print("Squared Numbers List Comprehension:", squared_numbers)
print("Even or Odd Lambda:", result_even_or_odd)
