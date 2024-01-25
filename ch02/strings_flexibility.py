# A string is a series of characters inside a single or double quotes
a = "This is a string"
b = 'This is also a string'
print(a)
print(b)
print(a,b)
print(b, a)
print(a+b)
# Flexibilty allows to use of quotes and apostrophes within a string
c = 'I told my friend, "Python is my favorite language!"'
print(c)
d = "The language 'Python' is named after Monty Python, not the snake."
print(d)
e = "One of Python's strengths is its diverse and supportive community."
print(e)
# Changing Case in a string with Methods
# The simplest task to do with strings is to change the case of the words in a string
name = "ada lovelace"
print(name)
print(name.title())  # method title() appears after the variable in the print() function call, title() method changes each word to title case
# A method is an action that Python can perform on a piece of data
# The dot (.) after name in name.title() tells Python to make the title() method act on the variable name
# Every method is followed by a set of parentheses because methods often need additional information to do their work. That information is provided inside the parentheses. The title() function doesn’t need any additional information, so its parentheses are empty
# Want your program to recognize the input values Ada, ADA, and ada as the same name, and display all of them as Ada.

# Change a string to all uppercase or all lowercase letters
name = "Ada LoveLace"
print(name.title())
print(name.upper())
print(name.lower()) # The lower() method is particularly useful for storing data. Many times you won’t want to trust the capitalization that your users provide, so you’ll convert strings to lowercase before storing them

# Using Variables in Strings (f-strings) f for format, in some situations you'll want to use a variable’s value inside a string
# Want two variables to represent a first name and a last name respectively, and then want to combine those values to display someone’s full name

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}" # To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark
# Put braces around the name or names of any variable you want to use inside the string
print(full_name)
print(full_name.title())
print(full_name.lower())
print(full_name.upper())


# Use f-strings to compose complete messages using the information associated with a variable
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name}{last_name}"
print(f"Hello, {full_name.title()}!") # full name is used in a sentence that greets the user, title() method changes the name to title case, code returns nicely formatted greeting
print(f"Hello, {full_name}!")


# Use f-strings to compose a message, and then assign the entire message to a variable
first_name = "ada"
Last_name = "lovelace"
full_name = f"{first_name}{last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
print(f"Nice to meet you {full_name.title()}!")

# Adding whitespace to string with tabs or Newlines
# whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols
# To add a tab use \t
print("Python")
print("\tPython")
print("Python\t")
print("\tPython\tCourse\n") # to add new line after the input

# To add a newline in a string, use the character combination \n
print("languages:\nPython\nC\nJavaScript\n")
# Combine new line and tab 
print("languages:\nPython\nC\tJavaScript\n")


# Combine tabs and newlines in a single string using "\n\t", tells Python to move to a new line, and start the next line with a tab
#Use a one-line string to generate four lines of output

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# Stripping Whitespace, Python makes it easy to eliminate extraneous whitespace from data that people enter
# Example eliminating whitespace from username when users log into the website via a username
# To ensure that no whitespace exists at the right end of a string, use the rstrip() method
favourite_language = 'python '  # Value of a variable contains extra whitespace at the end of the string
print(favourite_language)
favourite_language.rstrip() # Action of stripping whitespace from the right of the string can only be seen in the terminal 
