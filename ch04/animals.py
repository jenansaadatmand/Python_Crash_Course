# Exercise 4-2 animals: Think of at least three different that have a common characteristic
# store the names of these animals in a list, and then use a for loop to 
# print out the name of each animal
# modify your program to print a statement about each animal, such as 
# A dog would make a great pet
# Add a line at the end of your program , stating what these animals have in common 
# you should print a sentences, such as Any of these animals would make a great pet!

animals = ['dog','cat','bird']
print(animals)
for animal in animals:
    print(animal.title()) # for loop to print out the name of each animal
    print(f"A {animal.title()} would make a great pet\n")
print("Any of these animals would make a great pet!")