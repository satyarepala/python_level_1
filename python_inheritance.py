# Example 1: Single Inheritance

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

# Child class inheriting from Animal
class Dog(Animal):

    def speak(self):
        return "Woof! Woof!"

dog = Dog("Buddy")
# The Dog class inherits the name attribute from Animal
print(dog.name)       # Output: "Buddy"
# When calling the speak method on a Dog instance, it executes the overridden version
print(dog.speak())    # Output: "Woof! Woof"


# Example 2: Multi-Level Inheritance

# Parent class
class Shape:
    def __init__(self, color):
        self.color = color

# Child class inheriting from Shape
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

# Grandchild class inheriting from Circle
class ColoredCircle(Circle):

    def get_area(self):
        return 3.14 * self.radius * self.radius

colored_circle = ColoredCircle("Red", 5)
# The ColoredCircle class inherits both color and radius attributes
print(colored_circle.color)      # Output: "Red"
print(colored_circle.radius)     # Output: 5
# The ColoredCircle class has its own method, get_area
print(colored_circle.get_area()) # Output: 78.5


# Example 3: Multiple Inheritance

# Parent classes
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"{self.make} {self.model}"

class Electric:
    def __init__(self, battery_capacity):
        self.battery_capacity = battery_capacity

    def recharge(self):
        return "Charging in progress..."

# Child class inheriting from multiple classes - Vehicle and Electric
class ElectricCar(Vehicle, Electric):
    def __init__(self, make, model, battery_capacity):
        # Call the constructors of both parent classes using super()
        super().__init__(make, model)
        Electric.__init__(self, battery_capacity)

electric_car = ElectricCar("Tesla", "Model S", "100 kWh")
# The ElectricCar class inherits attributes and methods from both Vehicle and Electric
print(electric_car.get_info())      # Output: "Tesla Model S"
print(electric_car.recharge())      # Output: "Charging in progress..."
