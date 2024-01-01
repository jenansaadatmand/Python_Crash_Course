# Handling the FileNotFoundError Exception: using a try-except block
# Handling missing files, different locations, misspelled filename, or does not exist at all
# Let's try to read a file that does not exist
# The program tries to read the contents of Alice in wonderland, but we haven't saved the file alice.txt in the same directory as alice.py

# Use of f to represent the file object, common convention
# Encoding argument needed when your system's default encoding doesn't match the encoding of the file that's being read
# UTF-8 is a variable-width character encoding used for electronic communication. Defined by the Unicode Standard, the name is derived from Unicode (or Universal Coded Character Set) Transformation Format – 8-bit. ... Code points with lower numerical values, which tend to occur more frequently, are encoded using fewer bytes.
# UTF-8 is the most widely used way to represent Unicode text in web pages, and you should always use UTF-8 when creating your web pages and databases
# Python cannot read from a missing file, so it raises an exception
# traceback reports a FileNotFoundError exception is created when Python cannot find the file it's trying to open
filename = 'alice.txt'

try:  # The code in the try block produces an error so Python looks for an except block that matches the error
    with open(filename, encoding = 'utf-8'):
        f.read()
except FileNotFoundError: # python runs the except block to handle the error
    print(f"sorry, the file {filename} doesn't exist.") # result in friendly error message is printed to the user instead of the traceback
