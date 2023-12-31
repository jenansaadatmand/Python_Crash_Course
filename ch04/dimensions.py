# Define a rectangle dimensions using a tuple

dimensions=(200, 50) # tuples: immutable cannot be changed
print(dimensions)
print(dimensions[0]) # Call first index in tuple
print(dimensions[1]) # Call second index in tuple

# Trying to change one item in tuple, impossible
# dimensions[0] = 250
# Print(dimensions)  # you get error
print()

# If you need to define a tuple with one item, you must include a comma
my_t = (3,)
print(my_t)
print(my_t[0])
print()

# Looping over all values in a tuple usinf a for loop
dimensions= (200, 50)
for dimension in dimensions: 
    print(dimension)
print()
# Over writing a tuple by reassigning a new value to a variable that represent a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100) # associate a new tuple with the variable dimensions
print("unmodified dimensions:")
for dimension in dimensions:
    print(dimension)
