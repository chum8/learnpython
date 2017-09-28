# Python Exercise 7. User Input and While Loops

num_1 = ''
num_2 = ''
while num_1[0:1].lower() !='q' and num_2[0:1].lower() !='q':
    print("You may type 'q' at any time to continue to the next phase, or type 'quit' to exit the program.\n")
    num_1 = input("Input a number: ")
    if num_1[0:1].lower() =='q':
        break
    num_2 = input("Input a second number: ")
    if num_2[0:1].lower() =='q':
        break
    remainder = int(num_1) % int(num_2)
    if remainder == 0:
        print("\n" + num_1 + " is divisible by " + num_2 + "!\n" + num_1 + " \ " + num_2 + " = " + str(int(num_1) / int(num_2))[:-2])
    else:
        print("\n" + num_1 + " is NOT divisible by " + num_2 + ". In fact, it leaves a remainder of " 
                + str(remainder) + ".\n")

if num_1.lower() == 'quit' or num_2.lower() == 'quit':
    quitting = True
else:
    quitting = False

if quitting == False:
    limit = 149
    num_1 = input("\nPhase 2. Input a number: ")
    if num_1 == 'q' or num_1 == 'quit':
        if num_1 == 'quit':
            quitting = True
    else:
        blank = input("Hit enter to start displaying multiples of " + num_1 + ". Type 'q' at any time to continue to the next phase, or type 'quit' to exit the program.")
        x = 1
        while x <= limit:
            blank = input(str(int(num_1) * x) + "\n")
            x += 1
            if blank == 'q' or blank == 'quit':
                break
            if x == limit:
                print("Hit limit, exiting.")

        if blank == 'quit':
            quitting = True

# Moving items to another list using a loop
if quitting == False:
    unconfirmed_users = ['ben', 'david', 'larry', 'jen', 'tom', 'grace']
    confirmed_users = []

    print("\nNow we will very some users and move them to a new list.")

    while unconfirmed_users:
        current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)
    
    print("\nThe following users have been confirmed:")
    for confirmed_user in sorted(confirmed_users):
        print(confirmed_user.title())
    
# Removing all instances of a specific item

if quitting == False:
    pets = ['mouse', 'hamster', 'fish', 'bird', 'fish', 'mouse', 'fish', 'dog']
    print("\nHere's the list before removing all the 'fish'.\n" + str(pets))

    while 'fish' in pets:
        pets.remove('fish')

    print("\nHere it is after removing all the 'fish'.\n" + str(pets))

# Filling a dictionary with user input

if quitting == False:
    polling_active = True
    responses = {}

    while polling_active:
        name = input("\nWhat's your name? ")
        response = input("\nWhat city would you like to live in one day? ")
        responses[name] = response

        repeat = input("Type 'yes' and hit enter to let another person respond, or anything else to quit. ")
        if repeat != 'yes':
            polling_active = False

    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + " would like to visit " + response + ".")
