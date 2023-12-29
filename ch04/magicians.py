# for loop : to do the same action to each item within a list
magicians = ['alice', 'david', 'carolina']
# for every magician in the list of magicians, print the magician's name
for magician in magicians: # pull a name from the list and associate it to the variable magician or x
    print(magician.title()) # print the name that just been assigned to magician
print()
# less efficient solution 2:
print(magicians[0].title())
print(magicians[1].title())
print(magicians[2].title())
print()

# composing a message usinf f-string to each magician
for magician in magicians:
    print(f"{magician.title()}, that was a great trick !")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!") # This print() is outside of the loop

