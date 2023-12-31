# Modifying a list in a function
# Start with some designs that need to be printed.
# When passing a list to a function, the function can modify the list's contents
# Any changes made within the function body are permanent.
# A company that creates 3D printed models of designs that user submit
# Consider designs that need to be printed are stored in  a list, and after being printed they're moved to a separate list

# Program 1 doing this without a function:


unprinted_designs = ['phone case', 'root pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left. (use a while loop)
# Move each design to completed models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop() # pop each entry from the end from unprinted_designs, and store them in current_designs
    print(f"Printing model: {current_design}")
    completed_models.append(current_design) # Adds the design to the completed_model list

# Displays all completed models.
print("\nThe following models have been printed")
for completed_model in completed_models: # A for loop, will print each one alone not as a list
    print(completed_model)

print("\n")


# Solution 2: Restructuring/reorganizing this code using two predefined functions, easier to understand and easier to maintain

# First function will handle printing the design
# Second function will summarize the prints that have been made
# Use descriptive function names for ease of understanding

def print_models(unprinted_designs, completed_models): # Define a function with two parameters, a list of designs that need to be printed, and a list of completed models
    """simulate printing each design, until none are left. 
       Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop() # Emptying the list of unprinted_designs from end and fills current_designs, then adds/fills current_designs to completed_models 
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models): # define a function with one parameter: list of completed models
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)   # displays the name of each model that was printed

# This is the body of the program: 

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = [] # empty list that will hold the completed models

# Call two functions with the right arguments
print_models(unprinted_designs, completed_models) # Pass two lists when calling the function
show_completed_models(completed_models) # Pass one parameter when calling the function

# If we need to print more designs we simply call print_models() again

# In line 53, replace with line 60, if you don't want to empty the original unprinted_designs list and keep it for your record, then pass a copy of the list when you call it. This can be done using slicing notation [:] from beginning to end

# Print_models(unprinted_designs[:], completed_models)  # passing a copy using slicing, the original list will not be emptied or affected 
print(f"\n{unprinted_designs}") # to verify if the original list has been emptied [] if you use the line 53 command or if you replace line 53 with line 60, the list will be unchanged 

print(completed_models)

