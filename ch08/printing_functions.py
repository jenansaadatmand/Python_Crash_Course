
def print_models(unprinted_designs, completed_models): # define function with two prameters, a list of designs that need to be printed, and a list of completed models
    """simulate printing each desing, until none are left. 
       Move each design to completed_models after printing.""" # description of the function is well-documented in a docstring
    while unprinted_designs:
        current_design = unprinted_designs.pop() # emptying the list of unprinted_designs from end and fills current_designs, then adds/fills current_designs to completed_models 
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models): # define a function with one parameter: list of completed models
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)   # displays the name of each model that was printed




