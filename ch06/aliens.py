# List of dictionaries:

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points' : 15}

aliens = [alien_0, alien_1, alien_2] # list of dictionaries
for alien in aliens:  # loop through the list
    print(alien)    # print each alien
print()


# Code to generate 30 aliens using range()
# Make an empty list for storing aliens
# range() returns a series of numbers, tells Python how many times we want the loop to repeat

aliens = []

# Make 30 green aliens
for alien_number in range(30):  # each time loop runs, we create an alien
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)  # append each new alien to list aliens

# Imagine that some aliens changing color and moving faster
# Use a for loop and if statement to change the color of aliens
# Change the first three aliens to yellow, medium-speed aliens worth 10 points each

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
# Expand this loop by adding an elif block that turns yellow
# Aliens into red, fast-moving ones worth 15 points each
    elif alien['color'] == 'yellow':
         alien['color'] = 'red'
         alien['speed'] = 'fast'
         alien['points'] = '15'      


# Show the first 5 aliens

for alien in aliens[:5]:    # use a slice to print the first five aliens
    print(alien)
print("...")        
# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")  # print the length of the list to proove we generated 30 aliens
print()
