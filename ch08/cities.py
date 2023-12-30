# cities: write a function called describe_city() that accepts the name of a city and its country
# The function should print a simple sentence, 
# Such as Reykjavik is in Iceland.
# Give the parameter for the country a default value
# Call your function for three different cities, at least one of which is not in the default country

def describe_city(city, country= 'Iceland'):
    """prints city is in country, city's location"""
    print(f"{city} is in {country}")
describe_city(city= 'Reykjavik')
describe_city(city= 'Kópavogur')
describe_city(city='toronto', country='Canada')
describe_city('toronto', 'Canada')

print()

# Solution # 2:

def describe_city(city, country='chile'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)
describe_city('santiago')
describe_city('reykjavik', 'Iceland')
describe_city('punta arenas')
