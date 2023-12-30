# Dream vacation: write a program that polls users about their dream vacation
# Write a prompt similar to if you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll

responses = {}
polling_active = True
while polling_active: 
    name = input("What is your name?")
    response = input("If you could visit one place in the world, where would you go?")

    responses[name] = response
    repeat = input("Would like to let another person respond? ")
    if repeat == 'no':
        polling_active = False
print("--- Polling Results ---")
for name, response in responses.items():
    print(f"{name} would like to visit {response} oneday.")
