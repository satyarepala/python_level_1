# Using try, except, and finally with examples

# Example 1: Handling ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Division attempt completed.")

# Example 2: Handling FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print("Error:", e)
finally:
    print("File reading attempt completed.")

# Example 3: Handling ValueError
try:
    number = int("abc")
except ValueError as e:
    print("Error:", e)
finally:
    print("Value conversion attempt completed.")

# Custom Exception
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message

# Example 4: Raising a Custom Exception
def divide(a, b):
    if b == 0:
        raise MyCustomException("Cannot divide by zero.")
    return a / b

try:
    result = divide(10, 0)
except MyCustomException as e:
    print("Custom Exception:", e)
finally:
    print("Division attempt completed.")

# Example 5: Handling multiple exceptions
try:
    x = 5 / 0
    number = int("abc")
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)
except ValueError as e:
    print("ValueError:", e)
finally:
    print("Exception handling completed.")

# More Examples - Exception Handling

# Example 6: Handling IndexError
try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError as e:
    print("Error:", e)
else:
    print("Indexing succeeded.")
finally:
    print("Indexing attempt completed.\n")

# Example 7: Handling KeyError
try:
    my_dict = {'key1': 10, 'key2': 20}
    print(my_dict['key3'])
except KeyError as e:
    print("Error:", e)
else:
    print("Key lookup succeeded.")
finally:
    print("Key lookup attempt completed.\n")

# Example 8: Handling TypeError
try:
    result = 10 + "5"
except TypeError as e:
    print("Error:", e)
else:
    print("Type addition succeeded.")
finally:
    print("Type addition attempt completed.\n")

# Example 9: Using 'finally' without 'except'
try:
    x = 10 / 2
finally:
    print("Finally block executed even without exception.\n")

# Example 10: Handling multiple exceptions in a single 'except' block
try:
    num = int("abc")
    print(10 / 0)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
else:
    print("Operations succeeded.")
finally:
    print("Exception handling completed.")
