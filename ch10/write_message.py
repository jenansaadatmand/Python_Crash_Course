# Saving data and writing to an empty file
# To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.
# program writes a simple message and stores it in a file instead of printing it to screen
# you can open a file in 'r' read, 'w' write, 'a' append, 'r+' read and write modes
# Be be careful opening a file in write mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.
# python creates the file as it writes in it if it does not exist
filename = 'text_files/programming.txt'
with open(filename, 'w') as file_object: # call to open() in this example has two arguments (filename we want to open, write mode)
    file_object.write("I love programming.\n") # use write() method on object file to write a string to the file
    file_object.write("3\n") # numerical values must be convereted into strings using str()
    file_object.write("I love creating new games.\n")
