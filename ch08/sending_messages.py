# Sending messages: start with a copy of your program from exercise 8-9
# Write a function called send_messages() that prints each text message 
# And moves each message to a new list called sent_messages as it's printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.

#messages = ['I love you', 'how are you?', 'I like Python']
#sent_messages = []

#def show_messages(messages):
#    """Prints all text message in a list"""
#    for message in messages:
#        print(message)


#def send_messages(messages, sent_messages):
#    """Prints and moves each text message to a sent_messages."""
#    print(f"\nSending all messages: ")
#    while messages: # while contains messages
#        for message in messages: # loop through each item
#            
#            current_message = messages.pop() # empties original list from the end
#            print(current_message) # prints each messages 
#            sent_messages.append(current_message) # moves and fills messages into printed_messages new list

#print("\nShowing all messages: ")
#show_messages(messages)


#send_messages(messages, sent_messages) 
#print("\n")

# Printing the list of the messages
#print("\nFinal lists:")
#print("- Messages list:", end=' ') # Don't want your next string to be on a new line. Here's an example: print("Hello there!", end = '')
#print(messages) # prints emptied list
#print("- Sent_messages list:", end=' ')
#print(sent_messages) # prints populated list
#print("\n")


# Printing each message on a different line

#print("\nFinal messages:")
#show_messages(messages) # Because the list is empty, there are no messages to be printed
#show_messages(sent_messages) # All messages should be moved to this list

# Solution 2 book
def show_messages(messages):
    """Prints all messages in the list."""
    print("Showing all messages: ")
    for message in messages:
        print(message) # note, we don't want this, if you make this messages plural, you will print 3 lists of all messages!


def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages: ")
    while messages:
        current_message = messages.pop()
        print(current_message) # prints the current_message variable full list before emptying it
        sent_messages.append(current_message)

messages = ['hello there', 'how are you', ':)']
show_messages(messages)
sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)







