# User profile: start with a copy of user_profile.py from page 149
# Build a profile of yourself by calling build_profile(), 
# Using your first and last names and three other key-value pairs that describe you


def build_profile(first, last, **user_info): # also can use **kwargs
    """Builds a dictionary containing everything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    print(user_info)

build_profile('jenan', 'saadatmand', age= '47', hair = 'brown', hobby = 'motorbiking')

print("\n")


# Solution 2
def build_profile(first, last, **user_info): # also can use **kwargs
    """Builds a dictionary containing everything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info

user_profile = build_profile('jenan', 'saadatmand', age = '47', hair = 'black', hobby = 'motorbiking')
print(user_profile)
