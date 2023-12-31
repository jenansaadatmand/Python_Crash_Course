# Using a flag
# A program in which many different events could cause the program to stop running
# If many possible events might occur to stop the program, trying to test all these conditions in one while statement becomes complicated and difficult.
# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active.
# This variable is called a flag, and acts as a signal to the program 
# Write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.
# As a result, our overall while statement needs to check only one condition: whether or not the flag is currently True.
# Then, all our other tests (to see if an event has occurred that should set the flag to False) can be neatly organized in the rest of the program.

# Adding a flag to parrot.py
# Flag called active, will monitor whether or not the program should continue running

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."

active = True # setting up a flag by assigning the variable active to True, so program starts in active state
while active: # As long as the active variable remains True, the loop will continue running
    message = input(prompt)
    if message == 'quit':  # if statement inside the while loop, we check the value of message once the user enters their input.
        active = False # If the user enters 'quit', we set active to False, and the while loop stops.
    else: print(message)  # If the user enters anything other than 'quit' x, we print their input as a message.
