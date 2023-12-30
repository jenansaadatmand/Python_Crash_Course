# programming poll: write a while loop that asks people why they like programming
# Each time someone enters a reason
# add their reason to a file that stores all the responses

#prompt = 'Why do you like programming? '
#prompt += "Please enter 'quit' when you are finished."

#filename = 'text_files/responses.txt'
#response = input(prompt)
#while True:
#    if response == 'quit':
#        break
#    else:
#        print("Thank you! your response have been recorded.")
#    with open(filename, 'a') as object_file:
#        object_file.write(f"\n{response}")
#        break


# solution 2
filename = 'text_files/responses.txt'
responses = []
while True:
    response = input("\nWhy do you like programming? ")
    responses.append(response)
    
    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break
    with open(filename, 'a') as file_object:
        for response in responses:
            file_object.write(f"\n{response}")

