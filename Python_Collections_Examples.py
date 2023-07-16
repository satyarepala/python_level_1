# useful_additions.py

from collections import namedtuple, defaultdict

# Named Tuples Example
print("Named Tuples Example:")
# Creating a named tuple for representing a Point in 2D space
Point = namedtuple('Point', ['x', 'y'])
p1 = Point(1, 2)
p2 = Point(3, 4)
print("p1:", p1)  # Output: Point(x=1, y=2)
print("p2:", p2)  # Output: Point(x=3, y=4)
print("Distance between p1 and p2:", ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**0.5)
print()


# Default Dictionaries Example
print("Default Dictionaries Example:")
# Creating a default dictionary to count occurrences of each letter in a string
text = "hello world"
letter_count = defaultdict(int)  # int will be used as default factory (default value is 0)
for letter in text:
    letter_count[letter] += 1
print("Letter Count:", letter_count)
print()

# Explanation of Default Dictionaries Example:
# The `defaultdict` from the `collections` module allows us to create dictionaries with default values for missing keys.
# In this example, we create a defaultdict with an integer default factory (default value is 0).
# Then, we iterate through the text "hello world" and update the count of each letter in the dictionary.

# ... Additional examples ...

# useful_additions.py

from collections import Counter, deque

# Counter Example
print("Counter Example:")
# Counting occurrences of elements in a list
numbers = [1, 2, 3, 4, 1, 2, 1, 1, 5, 5]
number_count = Counter(numbers)
print("Number Count:", number_count)  # Output: Counter({1: 4, 2: 2, 5: 2, 3: 1, 4: 1})

# Finding the most common elements
most_common_2 = number_count.most_common(2)
print("Most Common 2:", most_common_2)  # Output: [(1, 4), (2, 2)]

# Removing occurrences
number_count.subtract({1: 2, 5: 1})  # Subtract occurrences of elements
print("Updated Number Count:", number_count)  # Output: Counter({1: 2, 2: 2, 5: 1, 3: 1, 4: 1})
print()

# Explanation of Counter Example:
# The `Counter` from the `collections` module is a specialized dictionary that counts occurrences of elements in a collection.
# In this example, we create a counter from a list of numbers. It shows the count of each number in the list.
# We can find the most common elements (e.g., the top 2 most common numbers).
# We can also subtract occurrences of elements from the counter.

# Deque Example
print("Deque Example:")
# Creating a deque and adding elements
d = deque([1, 2, 3])
print("Original Deque:", d)  # Output: deque([1, 2, 3])

# Appending and popping elements from both ends of the deque
d.append(4)
d.appendleft(0)
print("Updated Deque:", d)  # Output: deque([0, 1, 2, 3, 4])

d.pop()
d.popleft()
print("Final Deque:", d)  # Output: deque([1, 2, 3])

# Rotating elements in the deque
d.rotate(1)  # Right rotation by 1 step
print("Rotated Deque:", d)  # Output: deque([3, 1, 2])
print()

# Explanation of Deque Example:
# The `deque` from the `collections` module is a double-ended queue, which allows efficient appending and popping elements from both ends.
# In this example, we create a deque and demonstrate appending and popping elements from the front and back of the deque.
# We can also rotate elements in the deque.

# ... Additional examples ...

