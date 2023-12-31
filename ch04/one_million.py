# Exercise 4-4 One million: make a list of the numbers from one to one million
# And then use a for loop to print the numbers
# (if the output is taking too long, stop it by pressing CTRL-C) or by closing the output window)

#for number in range(1, 1_000_000): # making a list from 1 to 1 million
#    print(number)

# Solution 2: 
#numbers = list(range(1, 1_000_000))
#print(numbers)

# Solution 3:
list_num = list(range(1, 1_000_000))
for x in list_num:
    print(x)
