# complex_class.py

from abc import ABC, abstractmethod

class Person(ABC):
    """
    A class representing a Person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.

    Methods:
        __init__: Initialize the Person object.
        say_hello: Prints a greeting message.
        __str__: Return the string representation of the Person.
        __eq__: Check if two Person objects are equal.
        get_age: Get the age of the person.
        set_age: Set the age of the person.
        __private_method: A private method (not meant to be accessed from outside).
        _protected_method: A protected method (should be accessed with caution).
        static_method: A static method (does not require instance reference).
        abstract_method: An abstract method (needs to be implemented in subclass).
    """

    def __init__(self, name, age):
        """
        Initialize the Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
        """
        self.name = name
        self.age = age

    def say_hello(self):
        """Prints a greeting message."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __str__(self):
        """Return the string representation of the Person."""
        return f"{self.name} (Age: {self.age})"

    def __eq__(self, other):
        """Check if two Person objects are equal."""
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False

    def get_age(self):
        """Get the age of the person."""
        return self.age

    def set_age(self, new_age):
        """Set the age of the person."""
        if isinstance(new_age, int) and new_age > 0:
            self.age = new_age

    def __private_method(self):
        """A private method (not meant to be accessed from outside)."""
        print("This is a private method.")

    def _protected_method(self):
        """A protected method (should be accessed with caution)."""
        print("This is a protected method.")

    @staticmethod
    def static_method():
        """A static method (does not require instance reference)."""
        print("This is a static method.")

    @abstractmethod
    def abstract_method(self):
        """An abstract method (needs to be implemented in subclass)."""
        pass

# Example Usage:
if __name__ == "__main__":
    # Create a Person object
    person = Person("Alice", 30)

    # Call methods
    person.say_hello()
    print(person)

    # Change age using set_age method
    person.set_age(35)

    # Get age using get_age method
    age = person.get_age()
    print(f"New age: {age}")

    # Call protected method (use with caution)
    person._protected_method()

    # Call static method
    Person.static_method()

    # Uncommenting the following line will raise an error since abstract_method is not implemented
    # person.abstract_method()
