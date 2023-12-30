# Cats and dogs:
# Make two files, cats.txt and dogs.txt
# Store at least three names of cats in the first file
# And three names of dogs in the second file
# Write a program that tries to read these files and print the content of the file to the screen
# Wrap your code in a try-except block to catch the FileNotFound error, and 
# Print a friendly message if a file is missing.
# Move one of the files to a different location on your system, and make sure the code in the except block executes properly

# Solution 1 with defined function that is recalled

#filenames = ['text_files/cats.txt', 'text_files/dogs.txt']
#for filename in filenames:
#    print(f"\nReading file: {filename}")

#    def read_files(filename):
#         """Reading and printing the contents of files"""
#    try:
#        with open(filename, 'r') as file_object:
#            contents = file_object.read()
#            print(contents.title())

#    except FileNotFoundError:
#        print(f"Sorry, the file {filename} does not exist.")
    
#read_files(filename)

# Move one of the files to a different location on your system, and make sure the code in the except block executes properly

# solution 2

filenames = ['text_files/cats.txt', 'text_files/dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")




