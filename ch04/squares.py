# List of the first 10 square numbers, square of each integer from 1 through 10
# Two asterisks ** represent exponents
# Example of how to put the first 10 square numbers into a list

import statistics
squares = []
for value in range(1, 11):
    square = value ** 2             # Each value in the loop is raised to the second power and assigned to the variable square
    squares.append(square)
print(squares)
print("\n\n")
print()

# Solution 2: To write this code more concisely, omit the temporary variable square and append each new value directly to the list

squares = []
for value in range(1, 11):
    squares.append(value ** 2)      # Each value in the loop is raised to the second power and appended directly to the list
print(squares)
print("\n\n")

# Solution 3:
# Using list comprehension: 
# Creating a list of square numbers

squares = [value **2 for value in range(1, 11)]
print(squares)



# Simple statistics functions minimum, maximum, sum of a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))
print("\n")
print(statistics.mean(digits))  # sum/n or 10 = mean
print("\n")

# print(stdev(digits))  # Standard Deviation is a measure of measure confidence in statistical calculations and spread in Statistics. It is used to quantify the measure of spread, variation of a set of data values

print(statistics.stdev(digits))  #  standard deviation is the square root of the average square deviation (computed from the mean)
