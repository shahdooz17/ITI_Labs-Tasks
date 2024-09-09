# a) A welcome message (Welcome IT students)
def welcome():
    print("Welcome IT students")

# b) A welcome message (Welcome user name) based on the name you enter to it
def welcome_user(name):
    print(f"Welcome {name}")

# Test the functions
welcome()  # prints: Welcome IT students
welcome_user("Shahd")  # prints: Welcome Shahd

def min_number(num1, num2, num3):
    return min(num1, num2, num3)

# Test the function
result = min_number(5, 10, 2)
print(f"The smallest number is: {result}")  # prints: The smallest number is: 2


def abs_value(num):
    return abs(num)

# Test the function
result = abs_value(-7)
print(f"The absolute value is: {result}")  # prints: The absolute value is: 7


def f(x):
    return x**3 - 4

# Test the function
result = f(4)
print(f"The result of f(x) when x=4 is: {result}")  # prints: The result of f(x) when x=4 is: 60


def f():
    x = "C++"
    print(x)

x = "Python"
f()
print(x)

def ini_ch(ch1, ch2):
    if ch1[0].lower() == ch2[0].lower():
        return True
    else:
        return False

x = ini_ch("python", "Program")
y = ini_ch("python", "java")
print(x)  # Output: True
print(y)  # Output: False
