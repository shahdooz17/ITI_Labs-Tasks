
for i in range(6):
    print(i)  # Output: 0 1 2 3 4 5

for i in range(6, -1, -1):
    print(i)  # Output: 6 5 4 3 2 1 0

for i in range(6, -1, -1):
    if i == 4:
        break
    print(i)  # Output: 6 5

for i in range(1, 6):
    print(i)  # Output: 1 2 3 4 5
print("The loop is finished")  # Output after loop: The loop is finished

for i in range(9):
    if i == 2 or i == 8:
        continue
    print(i)  # Output: 0 1 3 4 5 6 7

for i in range(0, 11):
    if i % 2 != 0:
        print(i)  # Output: 1 3 5 7 9

i = 1
while (i < 10):
    print(i)
    i = i + 1

i = 1
while (i < 10):
    if i == 5:
        break
    print(i)
    i = i + 1
else:
    print("The loop has successfully completed!")

for i in "python":
    print(i)

for x in range(1, 12, 2):
    print(x)
