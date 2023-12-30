# Common words: visit Gutenberg (https://gutenberg.org/ )
# And find a few texts you’d like to analyze. 
# Download the text files for these works, or copy the raw text from your browser into a text file on your computer.
# You can use the count() method to find out how many times a word or phrase in a string.
# For example, the following code counts the number of times 'row' appears in a string

#line = "Row, row, row your boat"
#print(line.count('row'))
#print(line.lower().count('row')) # disregards case sensitivity or formatting
# Notice that converting the string to lowercase using lower() catches all appearances of the word you're looking for, regardless of how it's formatted
# Write a program that reads the files you found at Project Gutenberg 
# and determines how many times the word 'the' appears in each text.  
# This will be an approximation because it will also count words such as 'then' and 'there'
# Try counting 'the', with a space in the string, and see how much lower your count is.

#filenames = ['text_files/dracula.txt', 'text_files/pride_and_prejudice.txt', 'text_files/a_tale_of_two_cities.txt', 'text_files/candide.txt']
#for filename in filenames:

#    try: 
#        with open(filename, 'r') as f:
#            contents = f.read()
#            word_count = contents.lower().count('the') # catches then and there too
#            word_count_2 = contents.lower().count('the ') # only the, much lower outcome
#    except FileNotFoundError:
#         print(f"\nSorry, the file {filename} does not exist.")
#    else:
#        print(f"\nThe file {filename} contains the word 'the' {word_count} times.")
#        print(f"\n The file {filename} contains the word 'the ' {word_count_2} times")

#print("\n")

# solution 2: pass the exception and do nothing
# This solution only examines one text, 
# but the function can be applied to any number of texts.

def count_common_words(filename, word):
    """count how many times word appears in the text."""
    # Note this is a really simple approximation, and the number returnes 
    # will be higher than the actual count.

    try: 
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else: 
        word_count = contents.lower().count(word)
        msg = f"'{word}' appears in {filename} about {word_count} times."
        print(msg)
filename = 'text_files/dracula.txt'
count_common_words(filename, 'the')
count_common_words(filename, 'the ')



