# Class with Different Methods

class MyClass:
    # 1. Instance Method
    def instance_method(self):
        return "This is an instance method."

    # 2. Class Method
    @classmethod
    def class_method(cls):
        return "This is a class method."

    # 3. Static Method
    @staticmethod
    def static_method():
        return "This is a static method."

    # 4. Special (Dunder) Method
    def __str__(self):
        return "This is a special method (__str__)."

    # 5. Regular Method
    def regular_method(self):
        return "This is a regular method."

# Creating an instance of the class
obj = MyClass()

# Calling different methods

# 1. Instance Method
print(obj.instance_method())  # Output: "This is an instance method."

# 2. Class Method
print(MyClass.class_method())  # Output: "This is a class method."

# 3. Static Method
print(MyClass.static_method())  # Output: "This is a static method."

# 4. Special (Dunder) Method
print(obj)  # Output: "This is a special method (__str__)."

# 5. Regular Method
print(obj.regular_method())  # Output: "This is a regular method."


# Public, Private, and Protected Methods Example

class MyClass:
    def __init__(self):
        self.public_var = 10
        self._protected_var = 20
        self.__private_var = 30

    # Public Method
    def public_method(self):
        return "This is a public method."

    # Protected Method (convention using a single underscore)
    def _protected_method(self):
        return "This is a protected method."

    # Private Method (convention using double underscores)
    def __private_method(self):
        return "This is a private method."

# Creating an instance of the class
obj = MyClass()

# Accessing class variables and methods

# Public Variable (can be accessed directly)
print(obj.public_var)  # Output: 10

# Protected Variable (conventionally accessed directly, but consider it protected)
print(obj._protected_var)  # Output: 20

# Private Variable (name-mangled to avoid accidental access, but still can be accessed)
print(obj._MyClass__private_var)  # Output: 30

# Public Method (can be called directly)
print(obj.public_method())  # Output: "This is a public method."

# Protected Method (conventionally called directly, but consider it protected)
print(obj._protected_method())  # Output: "This is a protected method."

# Private Method (name-mangled to avoid accidental call, but still can be called)
print(obj._MyClass__private_method())  # Output: "This is a private method."
