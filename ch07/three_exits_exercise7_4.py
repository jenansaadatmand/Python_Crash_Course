# Exercise 7-6: Three exits: write different versions of either exercise 7-4 or exercise 7-5 that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs
# Use a break statement to exit the loop when the user enters a 'quit' value

#Original exercise 7-4: 
#prompt = "\nWhat topping would like on your pizza?"
#prompt += "\nEnter 'quit' when you are finished:"
#while True: 
#    topping = input(prompt)
#    if topping != 'quit':
#        print(f"I'll add {topping} to your pizza.")
#    else:
#        break

# Use a conditional test in the while statement to stop the loop.
#prompt = "\nWhat topping would you like on your pizza?"
#prompt += "\nEnter 'quit' when you are finished:"
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit': # now the program makes a quick check before displaying the message and only prints the message if it does not match the quit value
#        print(f"I will add {message} to your pizza.")

# Use an active variable (flag) to control how long the loop runs
#prompt = "\nWhat topping would like on your pizza?"
#prompt += "\nEnter 'quit' when you are finished:"
#active = True # program starts in active state
#while active:
#    message = input(prompt)
#    if message == 'quit':
#        active = False
#    else: 
#        print(f"I'll add {message} to your pizza.")

# Use a break statement to exit the loop when the user enter a 'quit' value

#prompt = "\nWhat topping would like on your pizza?"
#prompt += "\nEnter 'quit' when you are finished:"
#while True:
#    topping = input(prompt)
#    if topping == 'quit':
#        break
#    else: 
#        print(f"I'll add {topping.title()} to your pizza.")

# Original excersize 7-5 movie tickets:
#prompt = "\nHow old are you?"
#prompt += "\nEnter 'quit' after you finished:"

#while True:
#    age = input(prompt)
#    if age == 'quit':
#        break
#    age = int(age)
    
#    if age < 3:
#        print("You get in free!")
#    elif age < 13:
#        print("Your ticket is $10.")
#    else:
#        print("You ticket is $15.")

# Use a conditional test in the while statement to stop the loop.
#prompt = "\nHow old are you?"
#prompt += "\nEnter 'quit' after you finished:"
#age = ""
#while age != 'quit':
#    age = int(input(prompt))
#    if age < 3:
#        print("You get in free!")
#    elif age < 13:
#        print("Your ticket is $10.")
#    else:
#        print("You ticket is $15.")

# Use an active variable (flag) to control how long the loop runs
prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' after you finished:"
active = True # program starts in active state
while active: 
    age = input(prompt)
    if age == 'quit':
        active = False
    age = int(input(prompt))

    if age < 3:
        print("Your get in free!")
    elif age < 13:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")


# Use a break statement to exit the loop when the user enter a 'quit' value
# the same as the original solution of 7-5
#while True:
#    age = input(prompt)
#    if age == 'quit':
#        break
#    age = int(age)
    
#    if age < 3:
#        print("You get in free!")
#    elif age < 13:
#        print("Your ticket is $10.")
#    else:
#        print("You ticket is $15.")
