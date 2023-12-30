# a function returning a value
# you store a first and last names separately and then call this function to display a neatly formatted full name 
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"  #  function body assigned to variable
    return full_name.title() # function returns a value that is converted to title case
musician = get_formatted_name('jimi', 'hendrix')  # call the function, the returned value is assigned to a variable
print(musician)  # output neatly formatted name
print()

# we could have used regular print function only
print('Jimi Hendrix')
print()

# we could have used the calling function only
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    print(full_name.title())
get_formatted_name(first_name='Jimi', last_name='Hendrix')
print()


# making an argument optional, so people using the function can choose to provide extra information only if they want to
# expand get_formatted_name() to handle middle names as well
# this function always requires middle name argument
def get_formatted_name(first_name, middle_name, last_name):
        """Return a full name, nestly formatted"""
        full_name= f"{first_name} {middle_name} {last_name}"
        return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)
print()
# this functon does not always require middle name argument
# making the middle name optional by giving them middle name argument an empty value
# set the dfault value of middle_name to an empty string and move it to the end of the llist of parameters
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name: # if test to check to see if middle name has been provided
        full_name = f"{first_name} {middle_name}, {last_name}" # combine all three togeather
    else:  # If no middle name is provided, the empty string fails the if test and the else block runs
        full_name = f"{first_name} {last_name}" # combine only first and last name
    return full_name.title()  # return and change to title case
musician = get_formatted_name('jimi', 'hendrix')  # assign to a variable
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')  # make sure that middle name is the last positional argument
print(musician)




