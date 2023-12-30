# greeter program: use a function with a while loop to greet users more formally
# first attempt at greeting people using their first and last names:

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# This is an infinite loop !
while True:  # while loop asks the user to enter their name, and we prompt for their first and last name separately
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
# quit condition (break statement to exit the loop) needed when you ask for a series of inputs
# user to be able to quit as easily as possible, so each prompt should offer a way to quit.
# break statement to exit the loop can be placed at either prompt
# message that informs the user how to quit, and then we break out of the loop if the user enters the quit value at either prompt.
