# A for loop

magicians = ["alice", "david", "carolina"]
print(f"\n{magicians}\n")

for magician in magicians: # Add as many repetitive tasks under the for loop
    print(f"{magician.title()}, that was a great trick!. ")
    print(f"I can't wait for your next trick, {magician.title()}.\n") # \n adds a new line after each pass through the loop creating  as set of neatly grouped messages 


print()


# Solution 2 longer repetitive way using an if statement
for i in magicians:
    if i == "alice":
        print(f"{magicians[0].title()}, that was a great trick!.")
    elif i == "david":
        print(f"{magicians[1].title()}, that was a great trick!.")
    else: 
        print(f"{magicians[2].title()}, that was a great trick!.\n")

