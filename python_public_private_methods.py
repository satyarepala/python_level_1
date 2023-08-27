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
