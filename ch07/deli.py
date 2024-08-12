# Deli: make a list called sandwich_orders and fill it with the names of various sandwiches
# Then make an empty list called finished_sandwiches
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich
# As each sandwich is made, move it to the list of finished sandwiches 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich.title())
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich.title()} sandwich.")
# Extra step to verify what is inside the finished_sandwiches list    
print(finished_sandwiches)

