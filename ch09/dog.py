# Creating and using a class
# You can model anything using classes
# Writing a simple class, Dog that represents any god
# We know that all dogs have information such as name and age, and behaviors such as sit and roll over.
# This class will tell Python how to make an object representing a dog.
# First we write the class, and then we use it to make individual instances, each of which represents one specific dog
# Every method call associated with an instance automatically passes self, which is a reference to the instance itself, it gives the individual instance access to the attributes and methods in the class
# _init_() method, a function that is part of a class called method, python runs, automatically when we create a new instance based on the Dog class, has two leading underscores and two trailing underscores, two underscores on each side of the init, takes three parameters: self(required and must come first), name and age. Pythons call this method to create an instance of class and automatically pass the self-argument
# First, creating the Dog class
# Each instance created from the dog class will store a name and an age, and we'll give each dog the ability to sit() and roll_over():

# When we make an instance of Dog, python will call the __ini__() method from the Dog class

class Dog:  # Define a class called Dog, by convention capitalized names refer to classes, no parenthesis () in classes
    """A simple attempt to model a dog.""" # A docstring describing what this class does
 
    def __init__(self, name, age): # Creates an instance representing a dog and sets the name and age attributes using the values provided in the class calls. --init--() takes the parameters and assigns them to the attributes that will be associated with instances made from this class
        """Initilaize name and age attributes."""
        self.name = name # create a variable with a prefix self., prefixed with self to be available to every method in the class, and be accessed through any instance created from the class
        self.age = age # Takes the value associated with the parameter age and assigns it to the variable age when then attached to the instance being created. Variables that are accessible through instances like this are called attributes

    def sit(self): # Method sit() does not need additional information to run, so it has one parameter, self
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Second, making an instance from a class 
# A class is a set of instructions for how to make an instance
# The class Dog is a set of instructions that tells Python how to make individual instances representing specific dogs
# Making an instance representing a dog

# Tell Python to create a dog whose name is 'Willie' and whose age is 6 years.
# Outcome, python returns an instance representing this dog using the attributes provided

my_dog = Dog('Willie', 6) # We don't pass self as an argument but we pass attributes willie and 6 here in the call, we assign this instance to my_dog variable. convension naming is capitalized name for class and lowercase name my_dog refer to single instance created from a class
print(f"My dog's name is {my_dog.name}.") # Accessing the value of the attribute name within the my_dog instance in the Dog class
print(f"My dog is {my_dog.age} years old.") # Accessing attribute age within the my_dog instance within the Dog class

# Accessing attributes of an instance, use dot notation
my_dog.name # dot notations syntax allows Python to look at the instance my_dog, then find the attribute's value associated with attribute name associated with my_dog. This is the same attribute referred to as self.name in the class Dog
print(my_dog.name)
my_dog.age
print(my_dog.age)


# Third, calling methods, after creating an instance from the class Dog, using dot notation to call any mthod defined in Dog class
# syntax: instance name.method
# Let's make our dog sit and roll over

my_dog.sit() # Calling sit() method from class Dog and runs on my_dog instance, no arguments passed, syntax: instance name.method
my_dog.roll_over() # Calling roll_over method
print("\n")

# In this program, attributes: name and age and methods: sit and roll_over

# Creating multiple instances from a class:
# Let's create a second dog called your_dog
# We create a dog nammed Jimmy and a dog named Lucy. Each dog is a separate instance with its own attributes, capable of the same set of actions

my_dog = Dog('Jimmy', 13)
your_dog = Dog('Lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()  # Notice, you don't need a print statement to display on screen, it will display automatically
my_dog.roll_over()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
