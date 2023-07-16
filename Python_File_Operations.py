# file_operations.py

# Reading from a File (Mode: 'r')
file_name = 'sample.txt'
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(f"Content of '{file_name}':\n{content}")
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

# Writing to a File (Mode: 'w')
file_name = 'output.txt'
data_to_write = "Hello, this is a sample text.\n"
try:
    with open(file_name, 'w') as file:
        file.write(data_to_write)
    print(f"Data written to '{file_name}' successfully.")
except IOError:
    print(f"An error occurred while writing to '{file_name}'.")

# Appending to a File (Mode: 'a')
file_name = 'log.txt'
data_to_append = "This line is appended to the file.\n"
try:
    with open(file_name, 'a') as file:
        file.write(data_to_append)
    print(f"Data appended to '{file_name}' successfully.")
except IOError:
    print(f"An error occurred while appending to '{file_name}'.")

#complex examples

# Example 1: Reading lines from a file
file_name = 'sample.txt'
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())  # strip() to remove newline character
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

# Example 2: Writing multiple lines to a file
file_name = 'output.txt'
data_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
try:
    with open(file_name, 'w') as file:
        file.writelines(data_to_write)
    print(f"Data written to '{file_name}' successfully.")
except IOError:
    print(f"An error occurred while writing to '{file_name}'.")

# Example 3: Appending multiple lines to a file
file_name = 'log.txt'
data_to_append = ["Log entry 1\n", "Log entry 2\n", "Log entry 3\n"]
try:
    with open(file_name, 'a') as file:
        file.writelines(data_to_append)
    print(f"Data appended to '{file_name}' successfully.")
except IOError:
    print(f"An error occurred while appending to '{file_name}'.")

# Example 4: Reading and writing binary files
source_file = 'image.jpg'
destination_file = 'image_copy.jpg'
try:
    with open(source_file, 'rb') as src, open(destination_file, 'wb') as dst:
        data = src.read()
        dst.write(data)
    print(f"File '{source_file}' copied to '{destination_file}' successfully.")
except FileNotFoundError:
    print(f"One of the files '{source_file}' or '{destination_file}' does not exist.")

# Example 5: Using 'with' to process files
file_name = 'data.txt'
try:
    with open(file_name, 'r') as file:
        for line in file:
            if 'python' in line.lower():
                print(line.strip())
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist.")

# pickle_examples.py

import pickle

# Example 1: Writing a List to a Binary File
data_list = [1, 2, 3, 4, 5]
file_name = 'data_list.bin'
with open(file_name, 'wb') as file:
    pickle.dump(data_list, file)
print(f"List written to '{file_name}' successfully.")

# Example 2: Writing a Dictionary to a Binary File
data_dict = {'name': 'Alice', 'age': 30, 'occupation': 'Engineer'}
file_name = 'data_dict.bin'
with open(file_name, 'wb') as file:
    pickle.dump(data_dict, file)
print(f"Dictionary written to '{file_name}' successfully.")

# Example 3: Writing Custom Objects to a Binary File
class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

person_obj = Person('Alice', 30, 'Engineer')
file_name = 'person_obj.bin'
with open(file_name, 'wb') as file:
    pickle.dump(person_obj, file)
print(f"Custom object written to '{file_name}' successfully.")

# read_binary_files.py

import pickle

# Example 1: Reading a List from a Binary File
file_name = 'data_list.bin'
with open(file_name, 'rb') as file:
    data_list = pickle.load(file)
print("Data read from", file_name, ":", data_list)

# Example 2: Reading a Dictionary from a Binary File
file_name = 'data_dict.bin'
with open(file_name, 'rb') as file:
    data_dict = pickle.load(file)
print("Data read from", file_name, ":", data_dict)

# Example 3: Reading a Custom Object from a Binary File
file_name = 'person_obj.bin'
with open(file_name, 'rb') as file:
    person_obj = pickle.load(file)
print("Data read from", file_name, ":", person_obj.__dict__)
