# Using get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}
# Print(alien_0['points'])  # error due to key does not exist
# Use get() method to set a value that will be returned if the requested key does not exist
# Handling error of abscence of key in dictionary using get()
# Dictionary name.get('key', 'associated value') returns a clean message instead of an error
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
# If you don't include a value in the get() python returns none indicating " no value exists"
point_value = alien_0.get('points')
print(point_value)
