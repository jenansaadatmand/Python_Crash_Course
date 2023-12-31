# Square numbers, make a list of the first 10 square numbers 
squares = []     # Start with an empty list
for value in range(1, 11):    # Loop through each value from 1 to 10 using the range() function
    square = value**2 # Assigning to a variable & raising the value to the second power and assigning to a variable 
    squares.append(square)
print(squares)
print()

# Solution 2: 

squares = []
for value in range(1, 11):
    squares.append(value**2) # Appending directly to the list no variable assignment 
print(squares)
print()

# Solution 3
squares = []
for x in range(1, 11):
    squares.append(x**2) # Appending to the list directly, no assignment to a variable 
print(squares)
print()

# List comprehension 
squares = [value**2 for value in range(1, 11)]
print(squares)
