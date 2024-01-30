# Exercise 8-9 messages: make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which print each text message

messages = ['I love you', 'Hello, how are you', 'I love Python']

def show_messages(messages):
    """Prints all text messages in a list."""
    for message in messages:
        print(message)

show_messages(messages) 

print("\n")

# Solution 2:
short_msgs = ['I love you', 'Hello, how are you?', 'I love Python']

def show_messages(short_msgs):
    """Displays all text messages in a list"""
    for msg in short_msgs:
        print(msg)

show_messages(short_msgs)

