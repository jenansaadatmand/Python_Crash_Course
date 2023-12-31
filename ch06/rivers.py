# Rivers: Make a dictionary containing three major rivers and the country each river runs through
# One key-value pair might be 'nile': 'egypt'
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary

rivers = {
    'nile': 'egypt', 
    'forat': 'iraq', 
    'Mississipi': 'united states',
    'fraser': 'canada',
    'kuskokwim': 'alaska',
    'yangtze': 'china',
    }
for river, country in rivers.items():
    print(f"\nThe {river.title()} flows through {country.title()}")
print()
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f"- {river.title()}")
print()

print("\nThe following countries are included in the data set:")
for country in rivers.values():
    print(f"- {country.title()}")
    
