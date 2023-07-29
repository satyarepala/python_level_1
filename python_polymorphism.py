# Method Overloading

class Calculator:
    # Defining two versions of the add method with different parameters
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

calc = Calculator()
# When we call the add method with two parameters, it raises a TypeError
print(calc.add(2, 3))      # Output: TypeError: add() missing 1 required positional argument: 'c'
# When we call the add method with three parameters, it executes the second version
print(calc.add(2, 3, 4))   # Output: 9


# Method Overriding

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    # Override the sound method in the Animal class with a specific implementation for Dog
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    # Override the sound method in the Animal class with a specific implementation for Cat
    def sound(self):
        return "Meow!"

dog = Dog()
# When we call the sound method on a Dog instance, it executes the overridden version
print(dog.sound())   # Output: "Woof! Woof!"

cat = Cat()
# When we call the sound method on a Cat instance, it executes the overridden version
print(cat.sound())   # Output: "Meow!"


# Duck Typing

class Bird:
    def fly(self):
        return "Bird flying"

class Airplane:
    def fly(self):
        return "Airplane flying"

def make_fly(entity):
    # The make_fly function works with any object that has a fly method
    return entity.fly()

bird = Bird()
airplane = Airplane()

# Calling make_fly with a Bird instance executes the Bird's fly method
print(make_fly(bird))       # Output: "Bird flying"
# Calling make_fly with an Airplane instance executes the Airplane's fly method
print(make_fly(airplane))   # Output: "Airplane flying"
