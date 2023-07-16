# Simple Examples

# List creation and indexing examples
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
print(my_list[-1])  # Output: 5

# List class methods examples
# Append
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Extend
another_list = [7, 8, 9]
my_list.extend(another_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Insert
my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

# Remove
my_list.remove(3)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6, 7, 8, 9]

# Processing lists using different loops
# For loop
for item in my_list:
    print(item)

# While loop
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

# List comprehension
squared_numbers = [num ** 2 for num in my_list]
print(squared_numbers)  # Output: [1, 4, 100, 16, 25, 36, 49, 64, 81]

# Examples with different scenarios
# Filtering even numbers
even_numbers = [num for num in my_list if num % 2 == 0]
print(even_numbers)  # Output: [2, 10, 4, 6, 8]

# Summing the elements of the list
total_sum = sum(my_list)
print(total_sum)  # Output: 52

# Reversing the list
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 10, 2, 1]

# Finding the maximum and minimum values
max_value = max(my_list)
min_value = min(my_list)
print(max_value, min_value)  # Output: 10 1

# Complex Examples - List Manipulation

# Example 1: Finding common elements in two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [elem for elem in list1 if elem in list2]
print(common_elements)  # Output: [3, 4, 5]

# Example 2: Flattening a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = [item for sublist in nested_list for item in sublist]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]

# Example 3: Removing duplicates from a list while preserving order
duplicate_list = [1, 2, 2, 3, 4, 4, 5, 5]
unique_list = []
[unique_list.append(item) for item in duplicate_list if item not in unique_list]
print(unique_list)  # Output: [1, 2, 3, 4, 5]

# Example 4: Sorting a list of tuples based on a specific element
student_scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
sorted_students = sorted(student_scores, key=lambda x: x[1], reverse=True)
print(sorted_students)  # Output: [('David', 95), ('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Example 5: Finding the frequency of each element in a list
data_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency_dict = {item: data_list.count(item) for item in set(data_list)}
print(frequency_dict)  # Output: {1: 1, 2: 2, 3: 3, 4: 4}

# Example 6: List slicing and stepping
numbers_list = [i for i in range(1, 11)]
print(numbers_list[1:8:2])  # Output: [2, 4, 6, 8]

# Example 7: Merging two sorted lists into one sorted list
list_a = [2, 4, 6, 8]
list_b = [1, 3, 5, 7]
merged_list = sorted(list_a + list_b)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Example 8: Creating a list of Fibonacci numbers
def generate_fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]
        fib_list.append(next_num)
    return fib_list

fibonacci_sequence = generate_fibonacci(10)
print(fibonacci_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Example 9: Reversing words in a sentence while preserving word order
sentence = "Hello World, how are you?"
reversed_sentence = " ".join(word[::-1] for word in sentence.split())
print(reversed_sentence)  # Output: "olleH ,dlroW woh era ?uoy"

# Example 10: Combining multiple lists using zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 22]
countries = ["USA", "UK", "Canada"]
combined_list = list(zip(names, ages, countries))
print(combined_list)  # Output: [('Alice', 25, 'USA'), ('Bob', 30, 'UK'), ('Charlie', 22, 'Canada')]

# Extreme Examples - List Manipulation

# Example 1: Matrix Transposition
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transposed_matrix)
# Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Example 2: Grouping elements in chunks of a given size
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
chunk_size = 3

chunked_data = [data_list[i:i + chunk_size] for i in range(0, len(data_list), chunk_size)]
print(chunked_data)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

# Example 3: Removing elements from a list based on a condition
scores = [85, 90, 78, 95, 88, 62, 75, 82]
passing_scores = [score for score in scores if score >= 70]
print(passing_scores)
# Output: [85, 90, 78, 95, 88, 75, 82]

# Example 4: Finding the union and intersection of two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

union = list(set(list1) | set(list2))
intersection = list(set(list1) & set(list2))
print(union)         # Output: [1, 2, 3, 4, 5, 6, 7]
print(intersection)  # Output: [3, 4, 5]

# Example 5: List flattening using recursion
def flatten_list(input_list):
    output_list = []
    for item in input_list:
        if isinstance(item, list):
            output_list.extend(flatten_list(item))
        else:
            output_list.append(item)
    return output_list

nested_list = [[1, 2], [3, [4, 5]], [6, 7, [8, 9, [10]]]]
flattened_list = flatten_list(nested_list)
print(flattened_list)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Example 6: Finding the top N elements from a list
def top_n_elements(input_list, n):
    return sorted(input_list, reverse=True)[:n]

numbers = [25, 14, 32, 18, 7, 45, 21]
top_three = top_n_elements(numbers, 3)
print(top_three)
# Output: [45, 32, 25]
