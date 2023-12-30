# Favourite place: Make a dictionary called favourite_places
# Think of three names to use as keys in the dictionary
# and store one to three favorite places for each person
# To make this exercise a bit more interesting, 
# Ask some friends to name a few of their favorite places
# Loop through the dictionary, and print each person's name and their favorite places


favourite_places = {
                   'jenan':{'swiss', 'USA', 'Cambodia'},
                   'jimmy':{'kuwait', 'netherland', 'ireland'},
                   'tom': {'endland', 'eygpt', 'sudan'},
                   }
for name, places in favourite_places.items(): # loop through main dictionary
    print(f"\n{name.title()} likes the following places:")
    for place in places: # looping through each dictionary
        print(f"-{place.title()}")
