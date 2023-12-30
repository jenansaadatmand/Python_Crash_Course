# Login attempts: Add an attribute called login_attempts to your User class from excersize 9-3(page 162)
# write a method called increment_login_attempts() that increments the value of login attempts by 1
# write another method called reset_login_attempts() that resets the value of login_attempts to 0
# Make an instance of the user class and 
# call increment_login_attempts() several times
# print the value of login_attempts to make sure it was incremented properly, and
# call reset_login_attempts()
# print login_attempts again to make sure it was reset to 0

class User:
    """Represents as imple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the User."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Displays a summary of user's infomration"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")

    def greet_user(self):
        """Displays a personalized greeting to the user."""
        print(f"\nWelcome back {self.username}")

    def increment_login_attempts(self):
        """Increments the value of login_attempts"""
        self.login_attempts += 1
        #self.login_attempts = self.login_attempts + 1


 #       if login_attempts >= self.login_attempts:
 #           self.login_attempts = login_attempts + 1
 #       else:
 #           print("\nYou cannot roll back the number of login attempts!")

    def reset_login_attempts(self):
        """Resets login_attempts to 0"""
        self.login_attempts = 0
       

jimmy = User('jimmy', 'saadatmand', 'jimsaad', 'jimmysaad@yahoo.com', 'canada')


jimmy.describe_user()
jimmy.greet_user()
print()

print("\nMaking 3 login attempts...")

jimmy.increment_login_attempts()

jimmy.increment_login_attempts()

jimmy.increment_login_attempts()

print(f"  Login attempts: {jimmy.login_attempts}")

print("\nResetting login attempts...")

jimmy.reset_login_attempts()
print(f"\nlogin attempts: {jimmy.login_attempts}")



