# Letting the user choose when to Quit
# Make the parrot.py program run as long as the user wants by putting most of the program inside a while loop
# Define a quit value and then keep the program running as long as the user has not entered the quit value

# Define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit').
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
message = '' # Set up a variable message to keep track of whatever value the user enters. define message as an empty string, " "
while message != 'quit':  # compare the value of the message to 'quit',
    message = input(prompt)
    if message != 'quit':
        print(message)

# Python has some value stored in the message that it can check the first time it reaches the while loop
# The first time the program runs and Python reaches the while statement, it needs to compare the value of the message to 'quit', but no user input has been entered yet. If Python has nothing to compare, it won’t be able to continue running the program. 
# To solve this problem, we make sure to give the message an initial value. Although it’s just an empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work.
# While loop w runs as long as the value of the message is not 'quit'.
# The first time through the loop, the message is just an empty string, so Python enters the loop. At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter is assigned to message and printed; then, 
# Python reevaluates the condition in the while statement. As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. 
# When the user finally enters 'quit', Python stops executing the while loop and the program ends
