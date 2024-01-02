# Working with a File's contents
# After reading a file into memory, we can do whatever we want with the data
# Program to explore the digits of pi
# Build a single string containing all the digits in the file with no white space
filename = 'text_files/pi_digits.txt'
with open(filename) as file_object: # Open the file 
    lines = file_object.readlines() # Store each line in a list
pi_string = ''  # Create a variable to hold digits of pi as a list
for line in lines: # create a loop to add each line of digits to the variable pi_string
    pi_string += line.strip() # Remove newline character from each line on the right and left
print(pi_string) # Print the variable holding a single string
print(len(pi_string)) # print the length of the variable
# Output a string of pi to 30 decimal places, with 32 characters long
