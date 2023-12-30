# range() function to generate or print a series of numbers
# off-by-one behavior 
# range(start, stop, step)


for value in range(1,5): # only will print up to 5 not including 5, off-by one behavior
    print(value)
print()
for x in range(1,6): # it will print 1 to 5 not including 6
    print(x)
print()

for x in range(6): # it will start at 0 and end at 5, prints 0 through 5
    print(x)
print()

# using range to make alist of numbers using list(range(start, end))
numbers = list(range(1, 6))
print(numbers)

# passing range() one arrgument only, it will start at 0 and end at the provided value-1
for value in range(6):
    print(value)
print()

# skip numbers in a list using a step size and passing third argument within range()
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print()

# using a range() function to make a list of numbers
# raising a value to the second power

squares = []  # start with an empty list
for value in range(1, 11): # loop through the numbers 1, 10 using the range() function
    square = value **2 # raise the value to the second power, assign to a variable
    squares.append(square) # append the variable to the list
print(squares)
print()


