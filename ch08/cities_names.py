# Cities Names: Write a function called city_country() that takes in the name of a city and its country
# The function should return a string formatted like this: 
# " Santiago, Chile"
# Call your function with at least three city-country pairs, and 
# Print the values that are returned

def city_country(city, country):
    """Returns a neatly formatted string like 'Santiago, Chile'."""
    city_country = f'"{city}, {country}"' 
    return city_country.title()
land = city_country('toronto', 'canada')
print(land) 
land = city_country('Ottawa', 'Canada')
print(land) 
land = city_country('Montreal', 'Canada')
print(land) 

print()

# solution 2

def city_country(city, country):
    """Returns a neatly formatted string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"
city = city_country('santiago', 'chile')
print(city)
city = city_country('ushuaia', 'argentina')
print(city)
city = city_country('longearbyen', 'svalbard')
print(city)
