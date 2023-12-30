# Pizza topping: write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value
# As they enter each topping, print a message saying you'll add that topping to their pizza

prompt = ("\nPlease choose your pizza toppings: ")
prompt += ("\nEnter 'quit' to end the program.")

msg = ""
while msg != 'quit':
    msg = input(prompt)
    if msg != 'quit':  # this if test prevents the word quit to be printed on the screen but it allows the while loop to quit
        print(msg)  # prints input or quit as actual message if you don't include an if test prior to it

# in line 10 a modified version with if test is added 
# now the program makes a quick check before displaying the message and only prints the message if it does not match the quit value

