# 6_11 Cities: make a dictionary called cities
# Use the names of three cities as keys in your dictionary
# Create a dictionary of information about each city and include the country that the city is in, its approximate population and one fact about that city
# The keys for each city's dictionary should be something like country, population, and fact.
# Print the name of each city and all of the information you have stored about it

cities = {
    'montreal':{
        'country':'Canada', 
        'population': 10_000_000, 
        'fact': 'rocky'
        },
    'Toronto':{
        'country':'United States', 
        'population': 876, 
        'fact': 'alaska'
        },
    'Alberta': {
        'country': 'nepal', 
        'population': 975_453, 
        'fact': 'himilaya'
        },
    }
for name in cities.items():
    print(f"\n{name}")
    for key, value in cities.items():
        print(f"{key}{value}")
print()

# Solution 2: 

for city, city_info in cities.items():
    country = city_info['country'].title() 
    population = city_info ['population']
    fact = city_info['fact'].title()
    print(f"\n{city.title()} is in {country}.")
    print(f" It has a population of about {population}.")
    print(f" THe {'fact'} mountains are nearby")
