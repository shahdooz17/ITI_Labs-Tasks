# Task 1
str1 = "physics"
str2 = "math"
str3 = "IT Department studies %s and %s" % (str1, str2)
print(str3)

# Task 2
str01 = "Welcome to NCT University"
str02 = "IT and Autotronics are two Departments at NCT University"

# a) Convert str01 to upper case
str01_upper = str01.upper()
print(str01_upper)

# b) Convert str02 to lower case
str02_lower = str02.lower()
print(str02_lower)

# c) Concatenate str01_upper and str02_lower, then calculate length
str12 = str01_upper + " " + str02_lower
print(str12)
print("Length of str12:", len(str12))

# d) Rewrite str01 with each word on a new line
print('\n'.join(str01.split()))

# Task 3
given_string = "python is a programming language"
new = given_string[:4] + given_string[-2:]
print(new)

# Task 4
find_g = "languages".find("g")
find_f = "languages".find("f")
print("Position of 'g':", find_g)
print("Position of 'f':", find_f)

# Task 5
string_it = "IT professionals may advance their careers by obtaining IT certificates"

# a) Count occurrences of "IT"
count_it = string_it.count("IT")
print("Occurrences of 'IT':", count_it)

# b) Replace "IT" with "ICT"
string_ict = string_it.replace("IT", "ICT")
print("After replacing 'IT' with 'ICT':", string_ict)

# c) Check if the string is lower case
is_lower = string_it.islower()
print("Is string in lowercase?", is_lower)

# d) Convert to upper case and check if upper case
string_upper = string_it.upper()
is_upper = string_upper.isupper()
print(string_upper, "\nIs string in uppercase?", is_upper)

# e) Add '*' around "IT"
string_starred = string_it.replace("IT", "*IT*")
print(string_starred)

# f) Replace 'a' with '--XIX--'
string_replaced = string_it.replace("a", "--XIX--")
print(string_replaced)
