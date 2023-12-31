# Printing models: Put the functions for the example printing_models.py in a separate file called printing_functions.py
# Write an import statement at the top of printing_models_p155.py, 
# And modify the file to use the imported functions

import printing_functions as pf # Using as to give a module an alias, shorter name


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = [] # empty list that will hold the completed models

# Call two functions with the right arguments from the imported module

pf.print_models(unprinted_designs, completed_models) # Pass two lists when calling the function
pf.show_completed_models(completed_models) # Pass one parameter when calling the function


# In line 53, replace with line 60, if you don't want to empty the original unprinted_designs list and keep it for your record, then pass a copy of the list when you call it. This can be done using slicing notation [:] from begining to end

# Print_models(unprinted_designs[:], completed_models)  # Passing a copy using slicing, the original list will not be emptied or affected 
print(f"\n{unprinted_designs}") # To verify if the original list has been emptied [] if you use line 53 command or if you replace line 53 by line 60, list will be unchanged 
print(completed_models)


