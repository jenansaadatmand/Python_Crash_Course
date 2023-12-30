# Handling exceptions: exceptions are special objects to manage errors that arise during a program's execution
# Whenever an error occurs that makes Python unsure of what to do next, it creates an exception object
# If you write a code that handles the exception, the program will continue to run, otherwise, it will halt and show a traceback of the exception that was raised
# try-except block is used to handle exceptions, it asks Python to do something, but it also tells Python what to do if an exception is raised
# Instead of traceback, users will see a friendly error message and your program will continue to run

# Handling the zeroDivisionError exception
# simple error that causes Python to raise an exception
# It is impossible to divide a number by zero, but let's ask Python to do it anyway

#print(5/0)
# The error ZeroDivisionError reported in the traceback is an exception object
# use this information to modify our program by telling Python what to do when this kind of exception occurs
# using try-except blocks for handling ZerroDivisionError exception 

try: # Put the line that caused the error inside a try block
    print(5/0)  # If the code in a try block works, python skips over the except block
except ZeroDivisionError:  # if the code in the try block causes an error, tell Python what to do, python looks for an except block whose error matches the one that was raised and runs the code in that block
    print("You can't divide by zero!") # the user sees a friendly error message on the screen instead of a traceback
# If more code is added after the try-except block, the program continues running because we told python how to handle the error
    print("program is still active!")    
