# Exercise 4-5 Summing a million: make a list of the numbers from one to one million
# And then use min() and max() to make sure your list starts at one and ends at one million
# Also, use the sum() function to see how quickly Python can add a million numbers

numbers = list(range(1, 1_000_000))
print(min(numbers))
print(max(numbers)) # Not inclusive of 1_000_000 
print(sum(numbers))


