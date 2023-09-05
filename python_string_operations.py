# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# String interpolation
age = 30
info = f"Name: {full_name}, Age: {age}"

# String length
length = len(full_name)

# String slicing
greeting = "Hello, World!"
substring = greeting[0:5]  # Extracts "Hello"

# String upper and lower case
uppercase_name = full_name.upper()
lowercase_name = full_name.lower()

# String splitting
text = "This is a sample sentence"
words = text.split()  # Splits into a list of words

# String replacing
sentence = "I like cats."
replaced = sentence.replace("cats", "dogs")

# String searching
contains_cat = "cat" in sentence

# String formatting
number = 42
formatted_text = "The answer is: {}".format(number)

# String repetition
repeated_text = "abc" * 3  # Produces "abcabcabc"

# String stripping
whitespace_text = "   Trim me   "
stripped_text = whitespace_text.strip()

# String find and count
text = "Python is awesome and Python is versatile."
count_python = text.count("Python")
position_first_python = text.find("Python")

# Printing results
print("Full Name:", full_name)
print("Interpolated Info:", info)
print("Length of Full Name:", length)
print("Substring:", substring)
print("Uppercase Name:", uppercase_name)
print("Lowercase Name:", lowercase_name)
print("Words in Text:", words)
print("Replaced Text:", replaced)
print("Contains 'cat':", contains_cat)
print("Formatted Text:", formatted_text)
print("Repeated Text:", repeated_text)
print("Stripped Text:", stripped_text)
print("Count of 'Python':", count_python)
print("Position of First 'Python':", position_first_python)
