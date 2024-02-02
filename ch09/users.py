# Exercise 9-3 Users: make a class called user
# Create two attributes called first_name and last_name,
# and then create several other attributes that are typically stored in a user profile.
# Make a method called describe_user() that
# Print a summary of the user's information.
# Make another method called greet_user() that
# Prints a personalized greeting to the user
# Create several instances representing different users, and
# Call both methods for each user.


class User:
    """A class representing a user profile."""
 
    def __init__(self, first_name, last_name, age, gender, nationality, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender
        self.nationality = nationality.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Displays a summary of user's information."""
        print(f"\n- {self.first_name}, {self.last_name}")
        print(f"Age: {self.age}, Gender: {self.gender}, Nationality: {self.nationality}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Displays a personalized greeting to the user."""
        #print(f"Welcome back, {self.first_name}{self.last_name}!") can use this code for full name 
        print(f"Welcome back, {self.username}!") # Use this code for username

# Creating several instances representing different users:
jenan = User('jenan', 'saadatmand', '47', 'f', 'Canadian', 'jsaad', 'jenan@yahoo.com', 'canada') # alternatively, can use username_1 for the object or instance name instead of jenan 
jimmy = User('jimmy', 'saadatmand', '13', 'm', 'Canadian', 'jimsaad', 'jimmy@yahoo.com', 'canada')
soso = User('soso', 'Kawi', '35', 'f', 'Chinese', 'skaw', 'skawi@yahoo.com', 'China')
toto = User('toto', 'foo', '60', 'm', 'japanese', 'tfoo', 'tfoo@yahoo.com', 'japan')

jenan.describe_user()
jenan.greet_user()

jimmy.describe_user()
jimmy.greet_user()

soso.describe_user()
soso.greet_user()

toto.describe_user()
toto.greet_user()
