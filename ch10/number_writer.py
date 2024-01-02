# Storing Data/information into data structures (lists and dictionaries). eg: from user input, user preferences in the game, provide data for visualization
# Use JASON module (Javascript object notation format).
# When the user closes a program, he saves the information entered 
# json module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs
# json module can be used to share data between different python programs
# json module, share data between other programming languages
# Program stores a set of numbers and another program that reads these numbers back into memory
# Store data using json.dump() and read back into memory using json.load()
# json.dump(data piece to store, file object to store the data) takes two arguments 

# Program with json.dump() to store a list of numbers
# First import the json module

#import json # import json module
#numbers = [1, 3, 5, 7, 11, 13]  # create a list of numbers
#filename = 'numbers.json'  # choose filename, .json format, to store the list of numbers, and store it in a variable filename
#with open(filename, 'w') as f:  # Open file in write mode, allows json to write the data to the file
#    json.dump(numbers, f) # json.dump() function to store the list of numbers in the file object numbers.json

# Program has no output, but open file numbers.json (stored in the same directory as chapter_10) to see the list of numbers stored in it

# Program with json.load() to read the file or list back into memory

import json
filename = 'numbers.json' # Read from the same file we wrote 
with open(filename) as f: # Open in read mode by default or use 'r'
    numbers = json.load(f) # json.load() function to load information stored in numbers.json, assign it to variable numbers
print(numbers) # Print recovered list of numbers

# This is a simple way to share data between programs
