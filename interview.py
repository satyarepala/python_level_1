
users_info = {
    "akash": {
        "age": 25,
        "gender": "male",
        "income": 50000,
        "tax": 0.10,
        "purchase_history": (2000, 3000, 5000, 3500)
    },
    "harsha": {
        "age": 27,
        "gender": "male",
        "income": 70000,
        "tax": 0.08,
        "purchase_history": (200, 350, 5200, 2500)
    },
    "renuka": {
        "age": 22,
        "gender": "female",
        "income": 25000,
        "tax": 0.02,
        "purchase_history": (220, 3400, 110, 54)
    },
    "gayatri": {
        "age": 27,
        "gender": "female",
        "income": 80000,
        "tax": 0.12,
        "purchase_history": (200, 350, 42000, 210)
    },
}

# for key,value in users_info.items():
#     print(key)
#     print(value["purchase_history"])
#     print("--------------------------------------------")
#
from functools import reduce


# calculate sum of all elements of nested list

# my_list = [[1,2,3],[4,5,6],[7,8,9]]
# total_sum = 0
#
# for i in my_list:
#     print(i)
#     print(sum(i))
#     total_sum = sum(i) + total_sum

# generate fibonoccie series
# 0,1,1,2,3,5,8,13

# def fibonoccie(n):
#     fibonoccie_series = [0 ,1]
#     for i in range(n):
#         fibonoccie_series.append(sum(fibonoccie_series[-2:]))
#     print(fibonoccie_series ,n)
#     return n
# users_info = \
#     {"ashok": {"n": 10},
#     "akash": {"n": 20}
# }
#
# for key,value in users_info.items():
#     print(fibonoccie(value["n"]))

# print(sum(my_list[0]))
# print(sum(my_list[1]))
# print(sum(my_list[::]))


# for i in my_list:


# n = len(purchase_history)
# middle_index = ceil(n/2)
# print(middle_index)
# print(purchase_history[middle_index-1
# ])


# from math import pi
#
# class Circle:
#     def __init__(self,radius):
#         self.area = None
#         self.perimeter = None
#         self.radius = radius
#
#     def get_perimeter(self):
#         self.perimeter = 2 * pi * self.radius
#
#     def get_area(self):
#         self.area = pi * self.radius * self.radius
#
# c1 = Circle(5)
# c1.get_perimeter()
# c1.get_area()
# print(c1.perimeter)
# print(c1.area)



import re

text = "Contact us at +1 (555) 123-4567 or +91 9876543210."
# Regular expression to match phone numbers in the format: +X (XXX) XXX-XXXX or +XX XXXXXXXXXX
pattern = r"\+\d{1,2}\s?\(\d{3}\)\s?\d{3}-\d{4}|\+\d{2}\s?\d{10}"
phone_numbers = re.findall(pattern, text)
print("Phone Numbers:", phone_numbers)











