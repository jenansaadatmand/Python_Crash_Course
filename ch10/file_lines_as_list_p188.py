# Making a list of lines from a file
# when you use with block, the file object returned by open() is only available inside the with block that contains it
# to retain access to a file's content outside the with block, you store the file's line in a list inside the block and then work with that list
# program stores the lines of pi_digits.txt in alist inside the with block and then prints the lines outside the with block

filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines() # readlines() method takes each line from the file and store it in a list, then assigned to lines variable
for line in lines: # for loop, to continue to work with the list variable outside the with block
    print(line.rstrip())  # output matches original file exactly
