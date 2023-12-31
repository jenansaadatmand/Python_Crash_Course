# Exercise 4-8 cubes: a number raised to the third power is called a cube
# For example, he cube of 2 is written as 2**3 in Python
# make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10)
# And use a for loop to print out the value of each cube

cubes = list(range(1, 11))
for x in cubes: 
    cubes = x ** 3
    print(cubes)
