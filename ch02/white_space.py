# Adding white space to strings with Tabs or Newlines
# White space any nonprinting characters
# spaces, tabs, and end-of-line symbols

print()

print("Python")

# To add a tab use \t at the beginning 
print("\tPython")  # Adds a tab at the beginning 
print("Python\t")  # No tab

print()


# To add a newline in a string use \n
print("Languages:\nPython\nC\nJavascript")
print()

# Combine newlines and tabs in a single string using \n\t
# \n\t move to a new line and start the next line with a tab
# Use a one-line string to generate a four lines output

print("Languages\n\tPython\n\tC\n\tJavascript")

print()

# Manipulating strings via Stripping methods rstrip(), lstrip(), strip()
# Used to clean up user input before storing it in a program

# Stripping whitespace eg. 'python' and 'python '
# Important when comparing two strings to be the same or not
# example checking people's usernames when logging in to a website 
# Python makes it easy to eliminate extra whitespace from data that people enter
# Python looks for extra space on the right or left of a string

# Use rstrip() method to ensure no extra whitespace exists on the right side of a string
# To see the action of this code, need to type it in the Python terminal
favorite_language = 'python '
favorite_language.rstrip() # Removes space from right temporarily 
print(favorite_language) # When asking the value of variable again, it is the same with the space on right of string

print()

# To remove the whitespace from the right permanently 
# You have to associate the stripped value with the variable name
# Changing the variable's value and updating it as program is executed or in response to user input


favorite_language = 'python '
favorite_language = favorite_language.rstrip() # reassign the stripped value to the variable
print(favorite_language) # stripped permanently due to reassingment of variable

print()


# Strip whitespace from left of string using lstrip() method
# Strip whitespace from both sides at once strip() method
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

print()

# Removing a prefix from string
# Example: removing a URL prefix http:// to focus on URL part only that users need to enter into an address bar

nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))
print()
# removeprefix() leaves the original string unchanged 
# Reassign the new value to the original variable or assign it to a new variable to keep the new value without the prefix
# When you see a URL with http is not shown, the browser is using a removeprefix() method behind the scenes 

nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)
# or assign it to new value
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)  

print()
# Avoiding Syntax error with string
# Syntax error occurs when python does not recognize a section of your program as valid python code
# eg. if you use apostrophe within single quotes, you'll produce error
# How to use single and double quotes correctly
# See program apostrophe.py




