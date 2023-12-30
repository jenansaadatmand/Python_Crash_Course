# Working with multiple files, adding more books to analyze
# Let's move the bulk of this program to a function called count_words()
# By using a predefined function, it will be easier to run the analysis for multiple books

def count_words(filename): # Create a function, containing a try-except-else block
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filename = 'text_files/alice.txt'
count_words(filename) # calling the functin on the filename

# Write a simple loop to count the words in any text we want to analyze
# do this by storing all the names of files to be analyzed in a list and then we call count_words() function for each file in the list.
# we will analyze/count words for files:
#alice in wonderland, moby dick, little women, and siddhartha.read
# we will intentionally leave out siddhartha.txt from the directory containing the word_count.py, to see how well the program handles a missing file
print("\n")

filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']
for filename in filenames: # using a for loop to loop through the list
    count_words(filename) # calling the defined function for each item in the list

# the missing siddhartha.txt file has no effect on the rest of the program's execution because python can handle the error within the function
