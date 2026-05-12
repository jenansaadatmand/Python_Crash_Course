# Exercise 2-8: Python has a removesuffix() method that works exactly like 
# removeprefix()
# Assign the value 'python_notes.txt' to a variable called filename
# Then use the removesuffix() method to display the filename without the file extension
# like some file browsers do

file_name = 'python_notes.txt'
no_ext_file = file_name.removesuffix('.txt')
print(no_ext_file)
