# a prompt longer than one line, build multi-line string
# assign your prompt to a variable and pass that variable to the input() function.
# allows you to build your prompt over several lines, then write a clean input() statement.
# use operator += to add new string onto the end of the string in the previous variable
prompt = "If you tell us who you are, we can personalize the messages you see." # first line assigns the first part of the message to the variable prompt.
prompt += "\nWhat is your first name? " # adds the new string to previous string
name = input(prompt) # first assign your prompt to a variable and pass that variable to the input() function.
print(f"\nHello, {name.title()}!")
