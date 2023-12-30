# Split method: counting the words in alice in wonderland file alice.txt

filename = 'text_files/alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else: # Code only works if the code in try block is executed successfully
    # Count the approximate number of words in the file.
    words = contents.split() # produces a list of all words in a string
    num_words = len(words) # examine the length of the list as an approximation of the number of words in the original string
    print(f"The file {filename} has about {num_words} words.")
