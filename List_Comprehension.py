"""
double = []
for x in range(1, 11):
    double.append(x * 2)

print(double)
"""

"""
double = [x * 2 for x in range(1, 11)]
triple = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1,11)]
print(squares)
"""

"""
fruits = ["apple", "Banana", "Orange", "Coconut"]
fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)
"""
number = [1 ,-2, 3, -4, 5, -6]
positive_num = [num for num in number if num >= 0]
negative_num = [num for num in number if num < 0]
even_nums = [num for num in number if num % 2 == 0]
odd_nums = [num for num in number if num % 2 == 1]
print(odd_nums)