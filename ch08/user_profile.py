# Using arbitrary keyword arguments
# Sometimes you'll want to accept an arbitrary number of arguments, but you won't know ahead of time what kind of information will be passed to the function
# In this case, you write functions that accept as many key-value pairs as the calling statement provides
# Example, building user profiles, you know you will get information about the user profile
# You know you'll get information about user, but you're not sure what kind of information you'll receive.
# The function build_profile() always takes in a first and last name, but it accepts an arbitrary number of keyword arguments as well
# You'll often see the **kwargs parameter used to collect non-specific keyword arguments
# The double asterisk ** before the user_info parameter causes Python to create an empty dictionary called user_info and pack whatever name-value pairs it recieves into this dictionary 
# Within the function, you can access key-value pairs it recives just as you would for any dictionary.


def build_profile(first, last, **user_info): # Expects a first and last name, and as many name-value pairs as the user wants to enter, because of ** python stores name-value or key-value pairs in an empty dictionary 
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first # Add by accessing dictionary by assigning key to value 
    user_info['last_name'] = last 
    return user_info # this returns a dictionary of the key-values of the user stored information to the function's call line

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physicss') # Call the function and assign it to a variable

print(user_profile) # Print the variable containing the function call returned data
print("\n")

# Solution 2 using **kwargs (for keyword arguments)
print("\nSolution when replacing **user_info with **kwargs: \n")
def build_progile(first, last, **kwargs): # Accept as many as keyword arguments = name-value or key-value pairs and store in an empty dictionary)
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics') # call the function by passing it first and last name, and the two key-value pairs 
print(user_profile)

