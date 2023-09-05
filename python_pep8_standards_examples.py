# pep8_examples.py

# 1. Use snake_case for variable and function names.
def calculate_sum(a, b):
    result = a + b
    return result

# 2. Use spaces around operators and after commas, but no space directly inside parentheses.
x = 10
y = 5
z = calculate_sum(x, y)

# 3. Indent with 4 spaces (no tabs) for code blocks.
if z > 10:
    print("The sum is greater than 10.")
else:
    print("The sum is not greater than 10.")

# 4. Limit line length to 79 characters.
#    (This comment exceeds 79 characters for demonstration purposes.)

# 5. Use blank lines to separate logical sections of code.
def multiply(a, b):
    result = a * b
    return result

# 6. Use descriptive variable and function names.
number_of_students = 50
passing_score = 70

def calculate_percentage(achieved_score, total_score):
    percentage = (achieved_score / total_score) * 100
    return percentage

# 7. Use docstrings to document functions and modules.
def greet(name):
    """
    Greets a person by their name.

    Args:
        name (str): The name of the person to greet.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"

# 8. Imports should be on separate lines.
import math
import random

# 9. Use explicit import statements and avoid wildcard imports.
from collections import namedtuple
from itertools import chain


# 10. Put a single space after the '#' in comments.
# This is a comment.

# 11. Avoid extraneous whitespace at the end of lines.
message = "This is a message."

# 12. Use blank lines sparingly within functions to separate logical blocks.
def process_data(data):
    # Pre-processing
    cleaned_data = preprocess_data(data)

    # Data transformation
    transformed_data = transform_data(cleaned_data)

    # Post-processing
    processed_data = postprocess_data(transformed_data)

    return processed_data

# 13. Use blank lines before class and function definitions.
class MyClass:
    def __init__(self):
        self.my_attribute = 0

    def my_method(self):
        return self.my_attribute

# 14. Use triple quotes for multi-line strings.
multi_line_string = """
This is a multi-line string.
It spans across multiple lines.
"""

# 15. Use built-in constants like None, True, and False instead of comparing with literals.
if value is None:
    print("Value is None.")

if flag is True:
    print("Flag is True.")

if flag is False:
    print("Flag is False.")

# 16. Use underscores for unused variables (if required) to indicate that they are intentionally unused.
unused_variable_1 = 42
_ = unused_variable_1  # Indicates that this variable is intentionally unused.

# 17. Avoid writing long expressions on a single line. Break them into multiple lines for readability.
result = (
    (x + y) *
    (x - y)
)

# 19. doc string format for class
class ExampleClass:
    """This is a brief description of the ExampleClass.

    This docstring provides more detailed information about the class.
    You can use multiple lines to describe the purpose, attributes,
    methods, and other relevant details of the class.

    Attributes:
        attribute1 (type): Description of attribute1.
        attribute2 (type): Description of attribute2.

    Methods:
        method1(param1, param2): Description of method1.
        method2(param): Description of method2.

    Examples:
        You can include usage examples or sample code snippets here
        to demonstrate how to use the class and its methods.
        Example:
        ```
        obj = ExampleClass()
        result = obj.method1(10, 20)
        print(result)
        ```
    """
    # Class implementation goes here...

# Main code starts here...
