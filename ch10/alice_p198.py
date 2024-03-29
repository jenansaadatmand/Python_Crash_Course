# Exception handling helps when you are working with more than one file and one file does not exist
# Analyzing data or files containing the entire book
# Pull alice in Wonderland book from Project Gutenberg
# Try to count the number of words in the text
# Use a string method split(), which builds a list of words from a string
# string() method separates a string into parts wherever it finds space and stores all the parts of a string in a list
# To count the number of words, we will use split() to separate strings into words in a list then count them with len()
title = 'Alice in wonderland'
list_of_words = title.split()
print(title) # output original string
print(title.split()) # output list of words from a string
print(list_of_words) # output list of words from a string
print(len(list_of_words))  # output count of words
