# Using break to exit a loop
# To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the break statement.
# Break statement directs the flow of your program; you can use it to control which lines of code are executed and which aren’t
# Program that asks the user about places they’ve visited
# We can stop the while loop in this program by calling break as soon as the user enters the 'quit' value:
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.)" 
while True:  # a loop that starts with while True will run forever unless it reaches a break statement
    city = input(prompt)
    if city == 'quit':
        break # When they enter 'quit', the break statement runs, causing Python to exit the loop:
    else: 
        print(f"I'd love to go to {city.title()}!")
