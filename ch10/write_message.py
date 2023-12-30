# Saving data and writing to an empty file
# To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.
# Program writes a simple message and stores it in a file instead of printing it to screen
# You can open a file in 'r' read, 'w' write, 'a' append, 'r+' read and write modes
# Be careful opening a file in write mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.
# Python creates the file as it writes in it if it does not exist
filename = 'text_files/programming.txt'
with open(filename, 'w') as file_object: # call to open() in this example has two arguments (filename we want to open, write mode)
    file_object.write("I love programming.\n") # Use write() method on the object file to write a string to the file
    file_object.write("3\n") # numerical values must be converted into strings using str()
    file_object.write("I love creating new games.\n")
