# Looping is important to automate repetitive tasks
# Iteration with a for loop: (instead of retrieving or accessing each name one by one using index magicians[0] etc)
# For every magician in the list of magicians, print the magician's name

magicians = ["alice", "david", "carolina" ] # defining a list
print(magicians)

for magician in magicians:  # Defining a for loop, pull a name from the list and associate it with a temporary variable magician then title it
    print(magician.title()) # print the names associated with the variable magician 
    
# Python will repeat the last two lines, iterating through the list

for magician in magicians: # add as many repetitive tasks under the for loop
    print(f"\n{magician.title()}, that was a great trick!")
    print(f"I can't wait for your next trick {magician.title()}.\n") # \n adds a new line after each pass through the loop creating  as set of neatly grouped messages 
print("Thank you, everyone. That was a great magic show!")

print()
# solution 2: replace magician with i or any letter x etc

for i in magicians: # define a for loop, pull a name from list and associate it with temporary variable i  
    print(i.title()) # print the names associated with i  
# python will repeat the last two lines, iterating through the list 
