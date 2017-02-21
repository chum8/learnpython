# Python Exercise 5. If Statements

# Nested ifs using comparison operator

age = input("What's your age? ")
if int(age) < 21:
    if int(age) < 18:
        print("Sorry, no smokes or drinks for you yet. You have to wait " + str(18 - int(age)) + " more year(s) to smoke, and " + str(21 - int(age)) + " more year(s) to purchase liquor.")
    else:
        print("You may smoke, but no drinking for " + str(21 - int(age)) + " more year(s)!")
else:
    print("Hey, guess what -- you can smoke and drink!")

# Checking user input against a list

sundae_flavors = ['strawberry', 'hot fudge', 'chocolate', 'butterscotch', 'caramel', 'vanilla', 'blueberry', 'raspberry']

flavor = input("\nWhat flavor of sundae would you like? ")
if flavor.lower() in sundae_flavors:
    print("Congratulations, we have a " + flavor.title() + " Sundae for you.")
else:
    print("Sorry, that flavor is unavailable here.  Try Dairy Queen!")

# Using elif, and also error catching

income = input("\nEnter your annual income: ")
try:
    user_income = int(income)
except:
    print("Please enter a number!")
else:
    if int(income) > 249999:
        print("You'll be paying the highest tax bracket.")
    elif int(income) > 69999:
        print("You'll be paying the medium tax bracket.")
    elif int(income) > 29999:
        print("You'll be paying the lowest tax bracket.")
    else:
        print("You'll likely owe no tax this year.")

# Comparing two lists to each other

my_states = ['CO', 'WA', 'TN', 'IN', 'NM', 'NY']
favorite_states = []
new_state = input("\nEnter your favorite state to live in, using two letter codes (i.e. 'NE' for Nebraska.): ")
favorite_states.append(new_state)

for i in range(1, 6):
    new_state = input("Enter another favorite state: ")
    favorite_states.append(new_state)
print("\n")

matches = 0
misses = 0
for favorite_state in favorite_states:
    if favorite_state.upper() in my_states:
        print(favorite_state.upper() + " is one of my favorites, too!")
        matches = matches + 1
    else:
        print(favorite_state.upper() + " is not one of my favorite states. Sorry!")
        misses = misses + 1 
print("\nWe have " + str(matches) + " match(es) and " + str(misses) + " mismatch(es) between our favorite state selections!")

# More elif

number = input("\nEnter a whole number: ")

try:
    error_catch_number = int(number)
except:
    print("You failed to enter a whole number for the last time. Good bye!")
else:
    if number[-1] == "1":
        ordinal = number + "st"
    elif number[-1] == "2":
        ordinal = number + "nd"
    elif number[-1] == "3":
        ordinal = number + "rd"
    else:
        ordinal = number + "th"
    print("The ordinal of " + number + " is " + ordinal + ".")
print("\nThis is the end of the program.")
