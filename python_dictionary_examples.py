# Simple examples

# Dictionary creation and indexing examples
my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'occupation': 'Engineer'
}

print(my_dict['name'])  # Output: 'Alice'
print(my_dict['age'])   # Output: 30

# Dictionary class methods examples
# Adding a new key-value pair
my_dict['email'] = 'alice@example.com'
print(my_dict)

# Updating an existing value
my_dict['age'] = 31
print(my_dict)

# Removing a key-value pair
del my_dict['occupation']
print(my_dict)

# Processing dictionaries using different loops
# For loop
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

# Using dictionary items() method
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squared_ages = {key: value ** 2 for key, value in my_dict.items() if key == 'age'}
print(squared_ages)  # Output: {'age': 961}

# Examples with different scenarios
# Checking if a key exists in the dictionary
if 'name' in my_dict:
    print("Name exists in the dictionary.")
else:
    print("Name does not exist in the dictionary.")

# Getting a default value for a missing key
phone = my_dict.get('phone', 'N/A')
print(phone)  # Output: 'N/A'

# Merging two dictionaries
additional_info = {
    'hobbies': ['reading', 'painting'],
    'education': 'Bachelor of Science'
}

my_dict.update(additional_info)
print(my_dict)

# Finding the length of the dictionary
dict_length = len(my_dict)
print(dict_length)  # Output: 5

# Clearing all elements from the dictionary
my_dict.clear()
print(my_dict)  # Output: {}

# Complex Examples - Dictionary Manipulation

# Example 1: Counting occurrences of elements in a list using a dictionary
data_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

count_dict = {}
for item in data_list:
    count_dict[item] = count_dict.get(item, 0) + 1

print(count_dict)
# Output: {1: 1, 2: 2, 3: 3, 4: 4}

# Example 2: Finding the intersection of values in multiple dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}
dict3 = {'c': 3, 'd': 4, 'e': 5}

common_values = set(dict1.values()) & set(dict2.values()) & set(dict3.values())
print(common_values)
# Output: {3}

# Example 3: Grouping a list of tuples into a dictionary based on a key
data_tuples = [("Alice", 25), ("Bob", 30), ("Alice", 35), ("Charlie", 22)]

grouped_data = {}
for name, age in data_tuples:
    if name in grouped_data:
        grouped_data[name].append(age)
    else:
        grouped_data[name] = [age]

print(grouped_data)
# Output: {'Alice': [25, 35], 'Bob': [30], 'Charlie': [22]}

# Example 4: Sorting a dictionary by its values
data_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grapes': 3}

sorted_dict = {k: v for k, v in sorted(data_dict.items(), key=lambda item: item[1])}
print(sorted_dict)
# Output: {'banana': 2, 'grapes': 3, 'apple': 5, 'orange': 8}

# Example 5: Converting a list of tuples into a dictionary
data_tuples = [("name", "Alice"), ("age", 25), ("city", "New York")]

converted_dict = dict(data_tuples)
print(converted_dict)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Example 6: Counting character occurrences in a string using a dictionary
input_string = "abracadabra"

char_count = {}
for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)
# Output: {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# Complex Examples - Dictionary Manipulation

# Example 1: Merging dictionaries with nested dictionaries
dict1 = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}
dict2 = {
    'person1': {'city': 'New York'},
    'person3': {'name': 'Charlie', 'age': 28, 'city': 'Los Angeles'}
}

merged_dict = {}
for key, value in dict1.items():
    if key in dict2:
        merged_dict[key] = {**value, **dict2[key]}
    else:
        merged_dict[key] = value

for key, value in dict2.items():
    if key not in dict1:
        merged_dict[key] = value

print(merged_dict)
# Output: {'person1': {'name': 'Alice', 'age': 30, 'city': 'New York'},
#          'person2': {'name': 'Bob', 'age': 25},
#          'person3': {'name': 'Charlie', 'age': 28, 'city': 'Los Angeles'}}

# Example 2: Inverting a dictionary (keys become values, values become keys)
original_dict = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {v: k for k, v in original_dict.items()}
print(inverted_dict)
# Output: {1: 'a', 2: 'b', 3: 'c'}

# Example 3: Calculating the word frequency in a text using a dictionary
text = "This is a simple text. Text processing is fun and useful."

# Removing punctuation and converting text to lowercase
import string
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator).lower()

word_frequency = {}
for word in clean_text.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1

print(word_frequency)
# Output: {'this': 1, 'is': 2, 'a': 1, 'simple': 1, 'text': 2, 'processing': 1, 'fun': 1, 'and': 1, 'useful': 1}

# Example 4: Nested dictionary comprehension
nested_dict = {x: {y: x * y for y in range(1, 6)} for x in range(2, 5)}
print(nested_dict)
# Output: {2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
#          3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
#          4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}}

# Example 5: Counting occurrences of characters in multiple strings using dictionaries
strings = ["apple", "banana", "orange"]

char_occurrences = {}
for string in strings:
    for char in string:
        char_occurrences[char] = char_occurrences.get(char, 0) + 1

print(char_occurrences)
# Output: {'a': 2, 'p': 2, 'l': 1, 'e': 3, 'b': 1, 'n': 2, 'n': 1, 'a': 3, 'o': 1, 'r': 1, 'g': 1}

# Extreme Examples - Dictionary Manipulation

# Example 1: Recursive merging of dictionaries with nested dictionaries and lists
dict1 = {
    'person1': {'name': 'Alice', 'hobbies': ['reading', 'painting']},
    'person2': {'name': 'Bob', 'hobbies': ['swimming']}
}
dict2 = {
    'person1': {'age': 30, 'hobbies': ['cooking']},
    'person3': {'name': 'Charlie', 'age': 25, 'hobbies': ['coding']}
}

def recursive_merge(source, update):
    for key, value in update.items():
        if isinstance(value, dict):
            source[key] = recursive_merge(source.get(key, {}), value)
        elif isinstance(value, list):
            source[key] = source.get(key, []) + value
        else:
            source[key] = value
    return source

merged_dict = recursive_merge(dict1, dict2)
print(merged_dict)
# Output: {'person1': {'name': 'Alice', 'hobbies': ['reading', 'painting', 'cooking'], 'age': 30},
#          'person2': {'name': 'Bob', 'hobbies': ['swimming']},
#          'person3': {'name': 'Charlie', 'age': 25, 'hobbies': ['coding']}}

# Example 2: Converting a nested dictionary into a flat dictionary with nested keys
nested_dict = {
    'person1': {'name': 'Alice', 'age': 30, 'address': {'city': 'New York', 'zip': '10001'}},
    'person2': {'name': 'Bob', 'age': 25, 'address': {'city': 'Los Angeles', 'zip': '90001'}}
}

def flatten_dict(data, parent_key='', sep='.'):
    items = {}
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep))
        else:
            items[new_key] = value
    return items

flat_dict = flatten_dict(nested_dict)
print(flat_dict)
# Output: {'person1.name': 'Alice', 'person1.age': 30, 'person1.address.city': 'New York', 'person1.address.zip': '10001',
#          'person2.name': 'Bob', 'person2.age': 25, 'person2.address.city': 'Los Angeles', 'person2.address.zip': '90001'}

# Example 3: Generating all possible combinations of keys and values from nested dictionaries
nested_dict = {
    'A': {'a': 1, 'b': 2},
    'B': {'x': 10, 'y': 20}
}

def all_combinations(d):
    if not d:
        return [{}]
    key, values = d.popitem()
    rest_combinations = all_combinations(d)
    result = []
    for value in values:
        for combination in rest_combinations:
            temp_dict = combination.copy()
            temp_dict[key] = value
            result.append(temp_dict)
    return result

combinations = all_combinations(nested_dict)
print(combinations)
# Output: [{'A': 'a', 'B': 'x'}, {'A': 'a', 'B': 'y'}, {'A': 'b', 'B': 'x'}, {'A': 'b', 'B': 'y'}]

# Example 4: Finding the longest key in a deeply nested dictionary
deep_nested_dict = {'a': {'aa': {'aaa': {'aaaa': 1}}}, 'b': {'bb': {'bbb': 2, 'bbbb': 3}}}

def find_longest_key(data, prefix='', sep='.'):
    if not isinstance(data, dict):
        return prefix
    return max(find_longest_key(value, f"{prefix}{sep}{key}", sep) for key, value in data.items())

longest_key = find_longest_key(deep_nested_dict)
print(longest_key)
# Output: 'b.bb.bbbb'

# Example 5: Counting occurrences of values in nested dictionaries with lists of dictionaries
data_list = [
    {'name': 'Alice', 'skills': ['Python', 'Java']},
    {'name': 'Bob', 'skills': ['C++', 'Python', 'JavaScript']},
    {'name': 'Charlie', 'skills': ['Python']}
]

skill_occurrences = {}
for item in data_list:
    for skill in item['skills']:
        skill_occurrences[skill] = skill_occurrences.get(skill, 0) + 1

print(skill_occurrences)
# Output: {'Python': 3, 'Java': 1, 'C++': 1, 'JavaScript': 1}

