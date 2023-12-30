# Archived messages:
# start with your work from exercise 8-10
# call the function send_messages() with a copy of the list of messages.
# after calling the function, print both your lists to show that the original list has retained its messages.

def show_messages(messages):
    """Prints all messages in a list."""
    print("Showing all messages: ")
    for message in messages:
        print(message) 


def send_messages(messages, sent_messages):
    """Prints each message and then moves it to sent_messages."""
    print("\nSending all messages: ")
    while messages:
        current_message = messages.pop()
        print(current_message) 
        sent_messages.append(current_message)


messages = ['hello there', 'how are you', ':)']
show_messages(messages)
sent_messages = []
send_messages(messages[:], sent_messages) # call the function with a copy of the list of messages

print("\nFinal lists: ")
print(messages) # prints the original list which shows that it retained its messages
print(sent_messages)
print(messages[:]) # prints the copy of original list