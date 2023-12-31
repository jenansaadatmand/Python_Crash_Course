# Filling a dictionary with user input
# You can prompt for as much input as you need in each pass through a while loop
# Polling program in which each pass through the loop prompts for the participant's name and response
# Store the data we gather in a dictionary to connect each response with a particular user

responses = {}  # Defines an empty dictionary 
# Set a flag to indicate that polling is active.
polling_active = True

while polling_active: 
    # Prompt for the person's name and response.
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")

    # Store the response in the dictionary.
    responses[name] = response

    # The user is asked whether or not to keep the poll running
    # Find out if anyone else is going to take the poll.
    # If they enter yes, the program enters the while loop again.
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no': # If user enters no, the polling_active flag is set to False, the while loop stops running, and the final code block at x displays the results of the poll.
        polling_active = False
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():  # for loop to loop through the list
    print(f"{name} would like to climb {response}.")
