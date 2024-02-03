# Write a program that reads the contents of a text file and rewrites the file with formatting that allows a browser to display it.
# Work with information in a text file, the first step is to read the file into memory. read the entire file or one line at a time
# Reading an entire file
# Opens a file contains pi to 30 decimal places, with 10 decimal places per line
# Reader program opens the file, reads it, and prints the content of the file to the screen
# Use file relative path or absolute longer path to pass to open() function for the location of the desired file
with open('text_files/pi_digits.txt') as file_object: # With block is executed ( to open and close the file properly), open() function to open the file to access its contents, open() function returns an object representing the file pi_digits.txt.
    contents = file_object.read() # read() method to read entire content of file and store it as one long string in contents variable
print(contents)
print(contents.rstrip()) # Removing any white space characters from the right side of a string

print("\n")

# Reading line by line using a for loop on the file object
filename = 'text_files/pi_digits.txt' # Assign a variable to the file where are reading from
with open(filename) as file_object:
    for line in file_object: # Use a for loop to loop through the lines in a file
        print(line.rstrip()) # Stripping two blank lines, one invisible newline character at the end of each line from file and one added from print() function recalling

