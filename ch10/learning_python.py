# Learning Python: open a blank file in your text editor and write a few lines summarizing what you've learned about Python so far
# Start each line with the phrase In Python you can .... 
# Save the file as learning_python.text in the same directory as your exercises from this chapter
# Write a program that reads the file and prints what you wrote three times
# Print the contents once by reading the entire file, 
# Once by looping over the file object
# And once by storing the lines in a list and then working with them outside the with block


filename = 'text_files/learning_python.txt'
print("--- Reading in the entire file:\n")
with open(filename) as f:
    contents = f.read()
print(contents)

print("--- Looping over the lines:\n")
with open(filename) as file_object:
    lines = file_object.readlines() # Assigning a variable lines to hold the lines
for line in lines: # for loop to loop through the list
    print(line.strip())

print("\n--- solution2: Looping over the lines:\n")
with open(filename) as f:
    for line in f: # using a for loop to loop through f
        print(line.rstrip())

print("\nStoring the lines in a list:\n")
with open(filename) as file_object:
    lines = file_object.readlines()
string = ''
for line in lines:
    string += line
print(string)  

print("\nsolution 2: Storing the lines in a list:\n")
with open(filename) as f:
    lines = f.readlines() # automatically stores the lines in list
for line in lines: 
    print(line.strip())



