# Privileges: write a separate privileges class 
# The class should have one attribute, privileges, that stores a list of strings as described in exercise 9-7.
# Move the show_privileges() method to this class.
# Make a privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges

class User: 
    """Represents a simple User's profile."""
    
    def __init__(self, first_name, last_name, username, email, location):       
        """Initialize the User."""

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of user's information"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Displays a personalized greetings to the user."""
        print(f"Welcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets user's login attempts to 0."""
        self.login_attempts = 0


class Admin(User):  # Don't forget to have the superclass or parent class in the parenthesis, otherwise you get an error: "TypeError: object.__init__() takes exactly one argument (the instance to initialize)"
    """Represents a user with administrative privileges."""
    
    def __init__(self, first_name, last_name, username, email, location):    
        """Initialize the administrator."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()          # Initialize an empty set of privileges.

class Privileges:
    """A class to store an admin's privileges."""

    def __init__(self, privileges = []):
        """Initialize the privileges."""
        self.privileges = privileges
    
    def show_privileges(self):
        """Displays this administrator's privileges."""
        print(f"Privileges:")
        if self.privileges:
            for privilege in self.privileges:
               print(f"- {privilege}")
               #print("-" + privilege)
        else: 
            print("-The user has no privileges.")
    

jenan = Admin('jenan', 'saadatmand', 'jsaad', 'jenansaad@yahoo.com', 'canada') 

jenan.describe_user()
print()

jenan.privileges.show_privileges()

print()

print("\nAdding privileges...")

jenan_privileges = [                # Notice the variable with underscore
    'can reset passwords', 
    'can moderate discussions',
    'can suspend accounts', 
    'can add post', 
    'can delete post', 
    'can ban user', 
    'can register new user',
    ] 

jenan.privileges.privileges = jenan_privileges  # Pay attention to this line !

jenan.privileges.show_privileges()

