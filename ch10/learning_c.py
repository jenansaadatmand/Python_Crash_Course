# Learning C: You can use replace() method to replace any word in a string with a different word
# Here's a quick example showing how to replace 'dog' with 'cat' in a sentence:
#>>> message = "I really like dogs."
#>>> message.replace('dog', 'cat')
# 'I really like cats.'
# Read in each line from the file you just created, learning_python.txt,
# And replace the word Python with the name of another language, such as C
# Print each modified line to the screen.

filename = 'text_files/learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:        
    line = line.replace('Python', 'C')
    print(line.strip()) 

print("\nSolution 2:")
with open(filename) as f:
    lines = f.readlines() 
for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.strip()
    print(line.replace('Python', 'C'))

print("\nsolution 3: Changing method, using rstrip() and replace() on the same line")
# The newline is stripped from the end of the line and then Python is replaced by C
with open(filename) as f: 
    lines = f.readlines()
for line in lines:
    # Get rid of newline, then replace Python with C
    print(line.rstrip().replace('Python', 'C'))
