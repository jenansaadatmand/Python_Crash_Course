# Adding white space to strings with Tabs or Newlines
# White space any nonprinting characters
# spaces, tabs, and end-of-line symbols

print()

print("Python")

# To add a tab use \t at the beginning 
print("\tPython")  # adds a tab at the beginning 
print("Python\t")  # no tab

print()


# To add a newline in a string use \n
print("Languages:\nPython\nC\nJavascript")
print()

# Combine newlines and tabs in a single string using \n\t
# \n\t move to a newline and start the next line with a tab
# use one-line string to generate a four lines output

print("Languages\n\tPython\n\tC\n\tJavascript")

print()

# Manipulating strings via Stripping methods rstrip(), lstrip(), strip()
# used to clean up user input before storing it in a program

# stripping whitespace eg. 'python' and 'python '
# important when comparing two strings to be the same or not
# example checking people's usernames when logging in to a website 
# python makes it easy to eliminate extra whitespace from data that people enter
# python looks for extra space on the right or left of a string

# use rstrip() method to ensure no extra whitespace exists on the right side of a string
# to see the action of this code, need to type it in python terminal
favorite_language = 'python '
favorite_language.rstrip() # removes space from right temporarily 
print(favorite_language) # when ask the value of variable again, it is the same with space on right of string

print()

# To remove the whitespace from right permenantly 
# you have to associate the stripped value with the variable name
# Changing variable's value and updating it as program is executed or in response to user input


favorite_language = 'python '
favorite_language = favorite_language.rstrip() # reassign the stripped value to the variable
print(favorite_language) # stripped permanently due to reassingment of variable

print()


# strip whitespace from left of string using lstrip() method
# strip whitespace from both sides at once strip() method
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

print()

# Removing a prefix from string
# example: removing a URL prefix http:// to focus on URL part only that users need to enter into an address bar

nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
print(nostarch_url)
print(nostarch_url.removeprefix('https://'))
print()
# removeprefix() leaves the original string unchanged 
# reassign the new value to the original variable or assign it to a new variable to keep the new value without the prefix
# when you see a URL with http is not shown, the browser is using a removeprefix() method behind the scenes 

nostarch_url = nostarch_url.removeprefix('https://')
print(nostarch_url)
# or assign it to new value
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)  

print()
# Avoiding Syntax error with string
# syntax error occurs when python does not recognize a section of your program as valid python code
# eg. if you use apostrophe within single quotes, you'll produce error
# How to use single and double quotes correctly
# see program apostrophe.py




