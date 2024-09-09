sub = ("C++", "java", "python", 50, True, 36.2)

# a) Print out the second item in the tuple.
print(f"Second item: {sub[1]}")  # Output: java

# b) Create a tuple named sub_mini by slicing the sub tuple from the 1st item to the 3rd, then print out the new tuple.
sub_mini = sub[0:3]
print(f"Sliced tuple (sub_mini): {sub_mini}")  # Output: ('C++', 'java', 'python')

# c) Print out a range of items beginning from the 2nd to the last item.
print(f"Items from 2nd to last: {sub[1:]}")  # Output: ('java', 'python', 50, True, 36.2)

# d) Update the last item in the sub tuple to be 85.6, then print out both the updated item and the updated tuple.
# Note: Tuples are immutable, so you cannot update them directly, but you can convert them to a list, update, and convert back.
sub_list = list(sub)
sub_list[-1] = 85.6
sub = tuple(sub_list)
print(f"Updated last item: {sub[-1]}")  # Output: 85.6
print(f"Updated tuple: {sub}")  # Output: ('C++', 'java', 'python', 50, True, 85.6)

# e) Unpack a sub tuple in several variables named x1, x2, x3, x4, x5, x6.
x1, x2, x3, x4, x5, x6 = sub
print(f"Unpacked values: {x1}, {x2}, {x3}, {x4}, {x5}, {x6}")

# f) Concatenate sub tuple with sub_mini tuple in a new tuple named sub_add.
sub_add = sub + sub_mini
print(f"Concatenated tuple (sub_add): {sub_add}")

# g) Print out the index of python in the sub_add tuple.
print(f"Index of 'python': {sub_add.index('python')}")

# h) Count the occurrence of an element 36.2 in the sub_add tuple.
print(f"Occurrence of 36.2: {sub_add.count(36.2)}")

# i) Calculate the total length of the sub_add tuple.
print(f"Total length of sub_add: {len(sub_add)}")

# j) Convert the sub_add tuple to a list.
sub_add_list = list(sub_add)
print(f"Converted list: {sub_add_list}")

# k) Delete the sub tuple.
del sub
# print(sub)  # This will raise an error as sub has been deleted.

sentence = "Welcome to the university"
sentence_list = sentence.split()
print(f"Converted list: {sentence_list}")  # Output: ['Welcome', 'to', 'the', 'university']

tuple_str = ("p", "y", "t", "h", "o", "n")
converted_str = ''.join(tuple_str)
print(f"Converted string: {converted_str}")  # Output: python

# a) 
a_tuple = (4, 77, 3, [98, 15])
a_tuple[3][0] = 44
print(a_tuple)  # Output: (4, 77, 3, [44, 15]) - Modifying list inside the tuple is allowed.

# b) 
b_tuple = ("python")
print(type(b_tuple))  # Output: <class 'str'> - A single string without a comma is treated as a string, not a tuple.

# c) 
c_tuple = ("python",)
print(type(c_tuple))  # Output: <class 'tuple'> - Adding a comma makes it a tuple.

# d) 
d_tuple = "java",
print(type(d_tuple))  # Output: <class 'tuple'> - A trailing comma makes it a tuple.

# e)
e_wor = "Data"
print(list(e_wor))  # Output: ['D', 'a', 't', 'a'] - Converts each character into a list element.

# f)
f_wor = "info"
print(tuple(f_wor))  # Output: ('i', 'n', 'f', 'o') - Converts each character into a tuple element.

# g)
g_tuple = ("a", "b", "c", "d")
print(list(g_tuple))  # Output: ['a', 'b', 'c', 'd'] - Converts the tuple to a list.

# h) 
print(list())  # Output: [] - Creates an empty list.

# i) 
print(tuple())  # Output: () - Creates an empty tuple.

# j) 
print(("why", "??") * 4)  # Output: ('why', '??', 'why', '??', 'why', '??', 'why', '??') - Repeats the tuple elements 4 times.

# k) 
print(["hi!"] * 3)  # Output: ['hi!', 'hi!', 'hi!'] - Repeats the list elements 3 times.

# l) 
print(["hi!"] * 3)  # Same as (k), Output: ['hi!', 'hi!', 'hi!']

# m) 
sub = "python, C++, java"
print(sub.split(","))  # Output: ['python', ' C++', ' java'] - Splits the string by commas.
