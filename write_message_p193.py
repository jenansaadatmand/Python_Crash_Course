# append mode: 'a' is used when you want to add content to a file instead of writing over existing content.
# python does not erase the contents of the file before running the file object, lines will be added to the end of the file
# modifying write_message.py by adding some new reasons we love programming to the existing file programming.txt
filename = 'text_files/programming.txt'
with open(filename, 'a') as file_object:  # use the 'a' argument to open the file for appending rather than writing over the existing file.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
