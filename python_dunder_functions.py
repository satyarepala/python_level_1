# Dunder Methods in Python

# 1. __init__
class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(42)
print(obj.value)  # Output: 42

# 2. __str__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

person = Person("Alice", 30)
print(person)  # Output: Alice, 30 years old

# 3. __repr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

point = Point(2, 3)
print(point)  # Output: Point(2, 3)

# 4. __len__
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5

# 5. __add__
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(1, -1)
v3 = v1 + v2
print(f"({v3.x}, {v3.y})")  # Output: (3, 2)

# 6. __sub__
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

p1 = Point2D(5, 3)
p2 = Point2D(2, 1)
p3 = p1 - p2
print(f"({p3.x}, {p3.y})")  # Output: (3, 2)

# 7. __getitem__
class MyList:
    def __init__(self, items):
        self.items = items

    def __getitem__(self, index):
        return self.items[index]

my_list = MyList([1, 2, 3, 4, 5])
print(my_list[2])  # Output: 3

# 8. __setitem__
class MyList:
    def __init__(self, items):
        self.items = items

    def __setitem__(self, index, value):
        self.items[index] = value

my_list = MyList([1, 2, 3, 4, 5])
my_list[2] = 10
print(my_list.items)  # Output: [1, 2, 10, 4, 5]

# 9. __delitem__
class MyList:
    def __init__(self, items):
        self.items = items

    def __delitem__(self, index):
        del self.items[index]

my_list = MyList([1, 2, 3, 4, 5])
del my_list[2]
print(my_list.items)  # Output: [1, 2, 4, 5]

# 10. __contains__
class MyList:
    def __init__(self, items):
        self.items = items

    def __contains__(self, item):
        return item in self.items

my_list = MyList([1, 2, 3, 4, 5])
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False

# 11. __eq__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("Harry Potter", "J.K. Rowling")
book3 = Book("Lord of the Rings", "J.R.R. Tolkien")

print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False

# 12. __lt__, __le__, __gt__, __ge__ (Rich Comparison Methods)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1 < person2)  # Output: False
print(person1 <= person2)  # Output: False
print(person1 > person2)  # Output: True
print(person1 >= person2)  # Output: True
