# Reverse a string in Python
# We have a string and we want to reverse it
# Use a slice that steps backward, -1
# Create a slice that starts at the end of the slice, and moves backwards
# [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backward
# Slice represented as [start:stop:step] 
txt = "Hello world"[::-1]
print(txt)

# Creating a function that reverses a string
def my_function(x): # A function that takes a string as an argument
    """reverse a string"""
    return x[::-1] # Slice the string starting at the end of the string and move backward, return the backward string

mytxt = my_function("I wonder how this text looks like backwards") # Calling the function with a string as a parameter, and assigning the answer to a variable
print(mytxt)
