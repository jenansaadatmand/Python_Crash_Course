# range() function to generate or print a series of numbers
# off-by-one behavior 
# range(start, stop, step)


for value in range(1,5): # only will print up to 5 not including 5, off-by one behavior
    print(value)
print()
for x in range(1,6): # It will print 1 to 5 not including 6
    print(x)
print()

for x in range(6): # It will start at 0 and end at 5, prints 0 through 5
    print(x)
print()

# Using range to make alist of numbers using list(range(start, end))
numbers = list(range(1, 6))
print(numbers)

# Passing range() one argument only, it will start at 0 and end at the provided value-1
for value in range(6):
    print(value)
print()

# Skip numbers in a list using a step size and passing the third argument within range()
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print()

# Using a range() function to make a list of numbers
# Raising a value to the second power

squares = []  # Start with an empty list
for value in range(1, 11): # Loop through the numbers 1, 10 using the range() function
    square = value **2 # Raise the value to the second power, assign it to a variable
    squares.append(square) # Append the variable to the list
print(squares)
print()

# Writing the raising a value to the second power code more concisely
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# Simple statistics with a list of numbers: 
# min(), max(), sum()

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

print()


# List comprehension: to generate lists using one line
# It combines a for loop and the creation of new elements in one line
# And automatically appends each new element
# Building a list of square numbers using list comprehension: 
squares = [value **2 for value in range(1, 11)]
print(squares)
