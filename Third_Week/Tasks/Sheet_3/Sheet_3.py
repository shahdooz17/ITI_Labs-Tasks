import math

# Task 1: Arithmetic Operations
num1, num2, num3 = 3, 4, 5

# a) num1 + num2
print("num1 + num2 =", num1 + num2)

# b) num3 - num1
print("num3 - num1 =", num3 - num1)

# c) num1 * num2 + num3
print("num1 * num2 + num3 =", num1 * num2 + num3)

# d) num1 * (num2 + num3)
print("num1 * (num2 + num3) =", num1 * (num2 + num3))

# e) num3 / num1
print("num3 / num1 =", num3 / num1)

# f) num3 // num1
print("num3 // num1 =", num3 // num1)

# g) num3 % num1
print("num3 % num1 =", num3 % num1)

# Task 1h: Changing to float and repeating
num1, num2, num3 = float(3), float(4), float(5)

print("num1 + num2 (float) =", num1 + num2)
print("num3 - num1 (float) =", num3 - num1)
print("num1 * num2 + num3 (float) =", num1 * num2 + num3)
print("num1 * (num2 + num3) (float) =", num1 * (num2 + num3))
print("num3 / num1 (float) =", num3 / num1)
print("num3 // num1 (float) =", num3 // num1)
print("num3 % num1 (float) =", num3 % num1)

# Task 2
x, y, z, g = 1, 2, 3, 4

# a) x + y * z / g
print("x + y * z / g =", x + y * z / g)

# b) y ** z
print("y ** z =", y ** z)

# Task 3: String operations
str_a, str_b, str_c, num = "Python", "is a", "times fun language", 1000

# a) Concatenate strings
str_ab = str_a + " " + str_b + " " + str(num) + " " + str_c
print("Concatenated string:", str_ab)

# b) Repeat str_a 10 times
str_a10 = str_a * 10
print("Repeated string:", str_a10)

# Task 4: Working with numbers
num_1, num_2, num_3, num_4 = -5, 3.2, 5.7, 625

# a) Absolute value of num_1
print("Absolute value of num_1:", abs(num_1))

# b) Round off num_2 and num_3
print("Rounded num_2:", round(num_2))
print("Rounded num_3:", round(num_3))

# c) Square root of num_4
print("Square root of num_4:", math.sqrt(num_4))

# Task 5: Basic calculator for multiplication
def multiply(a, b):
    return a * b

# Example usage
result_mult = multiply(6, 7)
print("Multiplication result:", result_mult)
