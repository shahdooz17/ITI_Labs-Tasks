# Task 1: Comparisons
x, y, z = 5, 8, 12

# a) Is x equal to y?
print("Is x equal to y? ", x == y)

# b) Is y less than z?
print("Is y less than z? ", y < z)

# c) Is z greater than x?
print("Is z greater than x? ", z > x)

# d) Is x less than or equal to y?
print("Is x less than or equal to y? ", x <= y)

# e) Is y not equal to x?
print("Is y not equal to x? ", y != x)

# f) Is z not less than or equal to x?
print("Is z not less than or equal to x? ", not (z <= x))


# Task 2: Logical Operations
a, b, c, d = 2, 4, 7, 9

# a) Is d greater than b and c not equal a?
print("Is d > b and c != a? ", d > b and c != a)

# b) Is b greater than d and a less than d?
print("Is b > d and a < d? ", b > d and a < d)

# c) Is d less than b or c not equal a?
print("Is d < b or c != a? ", d < b or c != a)

# d) Is b greater than d or a less than d?
print("Is b > d or a < d? ", b > d or a < d)

# e) Negates the value of (is a greater than or equal to d)
print("Negates the value of (a >= d): ", not (a >= d))

# f) a >= 2 and (a / b) > 2
print("a >= 2 and (a / b) > 2: ", a >= 2 and (a / b) > 2)


# Task 3: String Comparisons
student_one, student_two, student_three = "Omar", "omar", "Omar"

# a) student_one != student_two
print("student_one != student_two: ", student_one != student_two)

# b) student_two == student_three
print("student_two == student_three: ", student_two == student_three)


# Task 4: Check if a number is even or not
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# Task 5: Check if the number is positive, negative, or zero
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")


# Task 6: Find the largest of three input numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")


# Task 7: Compare sum of two numbers with 20
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_of_numbers = num1 + num2

if sum_of_numbers > 20:
    print("The sum is greater than 20")
elif sum_of_numbers < 20:
    print("The sum is less than 20")
else:
    print("The sum is equal to 20")
