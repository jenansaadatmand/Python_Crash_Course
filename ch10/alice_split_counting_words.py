# Split method : counting the words in alice in wonderland file alice.txt

filename = 'text_files/alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else: # code only words if the code in try block is executed successfully
    # count the approximate number of words in the file.
    words = contents.split() # produce a list of all words in a strings
    num_words = len(words) # examine the length of the list as approximation of the number of words in the original string
    print(f"The file {filename} has about {num_words} words.")
