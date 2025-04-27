# Pets: Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner's name.
# Store these dictionaries in a list called pets
# Next, loop through your list, and as you do, print everything in a list called pets
# Next, loop through your list and as you do, print everything you know about each pet

pets = []
pet = {
        'breed': 'labrador',
        'name': 'jimmy',
        'owner': 'Jenan',
        'weight': '110', 
        'eats': 'kibbles',
        }
pets.append(pet)
pet = {
       'breed': 'rottweiler',
       'name': 'fofo',
       'owner': 'tim',
       'weight': '80',
       'eats': 'bugs',
       }
pets.append(pet)
pet = {
       'breed': 'pointer',
       'name': 'toto',
       'owner': 'fito',
       'weight': '75',
       'eats': 'shoes',
       }
pets.append(pet)

for pet in pets: # Displays information about each pet
    print(f"\n{pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}:{value}")

print()

# Solution 2: 

for pet in pets: 
    print(f"\nHere's what I  know about {pet['name'].title()}:")
for key, value in pet.items():
    print(f"\t{key}:{value}")


