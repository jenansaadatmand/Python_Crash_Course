# Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167)
# Add an attribute, privileges, that store a list of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's set of privileges
# Create an instance of Admin, and call your method

class User:  # from Exercise 9-5 (page 167)
    """Represents a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the User."""

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Displays a summary of user's infomration."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f" Username: {self.username}")
        print(f" Email: {self.email}")
        print(f" Location: {self.location}")

    def greet_user(self):
        """Displays a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increments the value of login_attempts"""
        self.login_attempts += 1      # alternatively self.login_attempts += 1

        #self.login_attempts = self.login_attempts + 1
 
    def reset_login_attempts(self):
        """Resets user's login_attempts to 0."""
        self.login_attempts = 0
    

class Admin(User):
    """Represents a user with administrative privileges."""
    
    def __init__(self, first_name, last_name, username, email, location):
        """ 
        Initialize the admin.
        Initialize attributes of Users parent class.
        Then initialize attributes specific to Admin child class.
        """
        super().__init__(first_name, last_name, username, email, location)  # no : at the end
        self.privileges = []  # attribute that stores a list

    def show_privileges(self):
        """Displays this administrator's privileges."""
        print(f"\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# this is a regular user not an administrator:

#jimmy = User('jimmy', 'saadatmand', 'jimsaad', 'jimmysaad@yahoo.com', 'canada')


#jimmy.describe_user()
#jimmy.greet_user()
#print()

# Create an instance of Admin and calling the method

jenan = Admin('jenan', 'saadatmand', 'jsaad', 'jenansaad@yahoo.com', 'canada') 

jenan.describe_user()

jenan.privileges = ['can reset passwords', 'can moderate discussions','can suspend accounts', 'can add post', 'can delete post', 'can ban user', 'can register new user'] # define the list of privieges

jenan.show_privileges()

# If you forget the () brackets after the method, you are not excuting the method so you get bound error





