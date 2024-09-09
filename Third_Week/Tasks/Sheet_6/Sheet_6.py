rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# a) Print out the fourth item in the list.
print(f"Fourth item: {rainbow_colors[3]}")  # prints: green

# b) Slice the old list rainbow_colors from the 3rd item to the end and assign it in a new list named colors, then print out the new list.
colors = rainbow_colors[2:]
print(f"Sliced list from 3rd item: {colors}")  # prints: ['yellow', 'green', 'blue', 'indigo', 'violet']

# c) Print out a range of items beginning from 2nd to 5th items
print(f"Items from 2nd to 5th: {rainbow_colors[1:5]}")  # prints: ['orange', 'yellow', 'green', 'blue']

# d) Update the fourth item in the list to be a white color, then print out both the updated item and the updated list.
rainbow_colors[3] = "white"
print(f"Updated fourth item: {rainbow_colors[3]}")  # prints: white
print(f"Updated list: {rainbow_colors}")  # prints: ['red', 'orange', 'yellow', 'white', 'blue', 'indigo', 'violet']

# e) Change violet color to brown color and print out the updated list.
rainbow_colors[rainbow_colors.index("violet")] = "brown"
print(f"Updated list with brown: {rainbow_colors}")  # prints: ['red', 'orange', 'yellow', 'white', 'blue', 'indigo', 'brown']

numbers = [1, 3.7, 6, 8]

# a) Add a gray color to the rainbow_colors list, then print out the updated list.
rainbow_colors.append("gray")
print(f"Updated list with gray: {rainbow_colors}")  # prints: ['red', ..., 'gray']

# b) Add a pink color as the first element in the rainbow_colors list, then print out the updated list.
rainbow_colors.insert(0, "pink")
print(f"Updated list with pink at first: {rainbow_colors}")  # prints: ['pink', 'red', ..., 'gray']

# c) Add the numbers list to the rainbow_colors list, then print out the updated list.
rainbow_colors.extend(numbers)
print(f"Updated list with numbers: {rainbow_colors}")  # prints: ['pink', 'red', ..., 8]

# d) Remove 6 from the numbers list, then print out the updated list.
numbers.remove(6)
print(f"Updated numbers list without 6: {numbers}")  # prints: [1, 3.7, 8]

# e) Remove all of the elements in the rainbow_colors list.
rainbow_colors.clear()
print(f"Cleared rainbow_colors list: {rainbow_colors}")  # prints: []

countries = ["UK", "Egypt", "UAE", "France", "Oman", "France", "USA", "Italy", "UAE", "Egypt"]

# a) Remove the last element in the list, then print out the updated list.
countries.pop()
print(f"Updated list after removing last element: {countries}")  # prints: ['UK', ..., 'UAE']

# b) Remove the first element in the list, then print out the updated list.
countries.pop(0)
print(f"Updated list after removing first element: {countries}")  # prints: ['Egypt', ..., 'UAE']

# c) Print out the index of France.
print(f"Index of France: {countries.index('France')}")  # prints: 3

# d) Count the occurrence of an element Egypt and print out the result.
print(f"Count of 'Egypt': {countries.count('Egypt')}")  # prints: 2

# e) Sort the countries list based on the length of the elements, then print out the updated list.
countries.sort(key=len)
print(f"Sorted list by length: {countries}")  # prints: ['UAE', 'USA', ..., 'France']

# f) Reverse the countries list in a new list named rev_list and print out the new list.
rev_list = list(reversed(countries))
print(f"Reversed list (new): {rev_list}")  # prints: ['France', ..., 'UAE']

# g) Reverse the countries list and print out the updated list.
countries.reverse()
print(f"Reversed countries list: {countries}")  # prints: ['France', ..., 'UAE']

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a) Sort the list in descending order, then print out the updated list.
int_list.sort(reverse=True)
print(f"List in descending order: {int_list}")  # prints: [9, 8, ..., 1]

# b) Sort the list in ascending order, then print out the updated list.
int_list.sort()
print(f"List in ascending order: {int_list}")  # prints: [1, 2, ..., 9]

# c) Clone the old list int_list into a new list named new_list, then print the new list.
new_list = int_list.copy()
print(f"Cloned list: {new_list}")  # prints: [1, 2, ..., 9]

# d) Remove a range of numbers starting from 2 to 8 from a new_list list, then print out the updated list.
new_list = [num for num in new_list if num < 2 or num > 8]
print(f"Updated new_list after removing numbers 2 to 8: {new_list}")  # prints: [1, 9]
