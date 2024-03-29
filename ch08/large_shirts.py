# Large shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
# Make a large shirt and a medium shirt with the default message, and 
# A shirt of any size with a different message

def make_shirt(msg='I love Python', size='large'):
    """Prints a message on T-shirts"""
    print(f'\n{size} shirt is printed with the message: "{msg}"')
make_shirt() # Make a large shirt
make_shirt(size='large'.title())
print()
# Make a medium shirt
make_shirt(size='medium'.title())
print()

# A shirt of any size with a different message
make_shirt(size='small'.title(), msg='I love flying')
print()

# Solution 2: 
def make_shirt(size='large', message='I love Python'):
    """Summarize the shirt that's going to be made"""
    print(f"\nI'm going to make a {size} t-shirt.")
    print(f'It will say, "{message}"')
make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
