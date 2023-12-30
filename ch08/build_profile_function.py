# Build_profile_function.py

def build_profile(first, last, **user_info): # also can use **kwargs
    """Builds a dictionary containing everything we know about a user."""
    user_info['first'] = first
    user_info['last'] = last
    return user_info


