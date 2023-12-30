# function returning a dictionary, takes textual information and returns a data structure
# function takes in parts of a name and returns a dictionary representing a person 

def build_person(first_name, last_name): # function takes in first and last name puts them into a dictionary
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name} # a dictionary is created, value ot first_name stored in first key, value of last_name stored in key last
    return person # entire dictionary returned
musician = build_person('jimi', 'hendrix')
print(musician) # prints a dictionary with key and values
print()


# extending the function to accept an optional value like middle name, age and occupation
# add a new optional parameter age to the function definition and assign the parameter the special value None, which is used when a variable has no specific value assigned to it
def build_person(first_name, last_name, age=None): # None is a placeholder value, in conditional tests, None evaluates to False
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age: 
        person['age'] = age   # store as a value in key age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

