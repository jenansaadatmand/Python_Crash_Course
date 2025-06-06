# People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, 
# And store all three dictionaries in a list called people. 
# Loop through your list of people.
# As you loop through the list, 
# Print everything you know about each person.

people = []
person = {
    'first_name': 'jimmy', 
    'last_name': 'saadatmand', 
    'age': 13, 
    'city': 'montreal',
    }
people.append(person)
person = {
    'first_name': 'jenan',
    'last_name': 'saadatmand',
    'age': 47,
    'city': 'montreal',
    }
people.append(person)
person = {
    'first_name': 'koko',
    'last_name': 'kiki',
    'age': 30,
    'city': 'toronto',
    }
people.append(person)
for person in people:  # Looping through the list
    name = f"{person['first_name'].title()} {person['last_name'].title()}" # storing dictionary key and associated value in variables
    age = person['age']
    city = person['city']
    print(f"{name}, of {city}, is {age} years old.")


