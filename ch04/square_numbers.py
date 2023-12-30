# Square numbers, make a list of the first 10 square numbers 
squares = []
for value in range(1, 11):
    square = value**2 # assigning to a variable
    squares.append(square)
print(squares)
print()

# Solution 2: 
squares = []
for value in range(1, 11):
    squares.append(value**2) # appending directly to the list no variable assignement 
print(squares)
print()

# Solution 3
squares = []
for x in range(1, 11):
    squares.append(x**2) # appending to the list direclty, no assignment to a variable 
print(squares)
print()

# List comprehension 
squares = [value**2 for value in range(1, 11)]
print(squares)

