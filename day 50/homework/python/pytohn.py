# 1. Create and Print a List
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)

# 2. Add and Remove Elements
my_list.append(6)  # Add an element
print("After adding:", my_list)
my_list.remove(3)  # Remove an element
print("After removing:", my_list)

# 3. Sort a List
unsorted_list = [5, 2, 9, 1, 7]
unsorted_list.sort()
print("Sorted List:", unsorted_list)

# 4. List Comprehension
squared_list = [x**2 for x in range(1, 6)]
print("Squared List:", squared_list)

# 5. Find Length of a List
print("Length of List:", len(my_list))

# 6. Using an If Statement
x = 10
if x > 5:
    print("x is greater than 5")

# 7. Using an If-Else Statement
y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# 8. Using an If-Elif-Else Statement
z = 8
if z > 10:
    print("z is greater than 10")
elif z == 10:
    print("z is equal to 10")
else:
    print("z is less than 10")

# 9. Nested If Statements
age = 20
if age >= 18:
    if age >= 21:
        print("You can drink and vote.")
    else:
        print("You can vote but not drink.")

# 10. While Loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 11. While Loop with Break
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

# 12. While Loop with Continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 13. Infinite Loop and Stopping It
count = 0
while True:
    print("Infinite Loop")
    count += 1
    if count == 3:
        break

# 14. Iterate Over a List with While
items = ['apple', 'banana', 'cherry']
i = 0
while i < len(items):
    print(items[i])
    i += 1

# 15. For Loop
for i in range(1, 6):
    print(i)

# 16. Iterate Over a List
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# 17. Nested For Loops
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")

# 18. For Loop with Else Clause
for i in range(3):
    print("Inside loop:", i)
else:
    print("Loop completed")
