# Failing silently: telling Python not to report the exception error it catches using a pss statement
# We will not report to the user the exception we catch
# Let the program fail silently when an exception occurs and continue on as if nothing happened
# To make the program fail silently, we write the try block as usual, but explicitly tell Python to do nothing in the except block using the pass statement.

def count_words(filename): # Indentation matters in the next lines
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf=8') as f:
            contents = f.read()
    except FileNotFoundError: # Tell Python to fail silently using a pass statement
        pass # The code in the except block runs but nothing happens
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.") 

filenames = ['text_files/alice.txt', 'text_files/siddhartha.txt', 'text_files/moby_dick.txt', 'text_files/little_women.txt']
for filename in filenames: 
    count_words(filename)

# The pass statement also acts as a placeholder. a reminder that you are choosing to do nothing at a specific point in your program's execution and that you might want to do something there later
# eg: later you might decide to write any missing filenames to a file called missing_files.txt. users will not see this file, but we will be able to read the file and deal with any missing texts.
