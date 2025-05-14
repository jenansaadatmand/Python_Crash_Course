# Exercise 4-2 animals: Think of at least three different that have a common characteristic
# Store the names of these animals in a list, and then use a for loop to 
# Print out the name of each animal
# Modify your program to print a statement about each animal, such as 
# A dog would make a great pet
# Add a line at the end of your program, stating what these animals have in common 
# You should print a sentence, such as Any of these animals would make a great pet!

animals = ['dog','cat','bird']
print(animals)
for animal in animals:
    print(animal.title()) # for loop to print out the name of each animal
    print(f"A {animal.title()} would make a great pet\n")
print("Any of these animals would make a great pet!")
