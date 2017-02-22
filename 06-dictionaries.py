# Exercise 6. Dictionaries

my_families = {'father': 'michael', 'mother': 'rhonda', 'self': 'douglas', 'spouse': 'laura', 'firstborn': 'edmund', 'secondborn': 'lavinia', 'thirdborn': 'rosamund', 'youngest': 'rafe'}

print("My father is " + my_families['father'].title() + ".")
print("My third eldest child is " + my_families['thirdborn'].title() + ".")
my_families['self'] = input("\nWitness protection program!  Change your name to something else: ")
print("\nYour name is now " + my_families['self'].title())
print("\nHere is your current family.")
print(my_families)
print("\nLet's backtrack to last February, before the youngest was born.")
del my_families['youngest']
print("\nHere is the family in February 2016.")
print(my_families)
print("\nNow, let's print it using a loop so we get nice formatting.")
for key, value in my_families.items():
    print("Key: " + key +
            "  Value: " + value.title())

# Making a dictionary with new lines in the code

wife_families = {
        'father': 'david',
        'mother': 'karen',
        'brother': 'nathan',
        'sister_in_law': 'chandra',
        'aunt': 'joanna',
        'niece': 'cora',
        'nephew': 'james',        
        }

# Sorting output

print("\nHere is some of my wife's family:\n")
for key, value in sorted(wife_families.items()):
    print(key.title() + ": " + value.title())

# Selecting specific keys while looping through a dictionary

younger_relatives = ['sister_in_law', 'niece', 'nephew']
print("\nHere are the relatives who are younger:\n")
for relative, name in wife_families.items():
    if relative in younger_relatives:
        print(relative.title() + " " + name.title() +
                " is younger.")

# Checking if a key exists

key_to_check = input("\nInput a value to see if a key of that name exists: ")
if key_to_check in wife_families.keys():
    print("Key " + key_to_check + " exists!")
else:
    print("Key " + key_to_check + " does NOT exist.")

# Using set to avoid repetitious data

favorite_numbers = {
        'craig': 2,
        'douglas': 8,
        'alanna': 3,
        'laura': 2,
        'thomas': 14,
        'dad': 5,
        'uncle_tom': 8,
        'aunt_linda': 9,
        'cassandra': 2,
        }

print("\nHere are some favorite numbers of various people. Duplicates are eliminated.\n")
for number in set(favorite_numbers.values()):
    print(number)

# Using nesting: Dictionaries inside of lists

composers = []

for composer_number in range(0, 13):
    new_composer = {
            'name': 'default',
            'dob': 'default',
            'opus': 'default',
            }
    composers.append(new_composer)

print("\nWe've generated a blank list of " + str(len(composers)) + " composers. Here's the first four.")
for composer in composers[:4]:
    print(composer)

print("...")

# Now, nesting with a list inside a dictionary

favorite_numbers = {
        'craig': [2, 0, 9],
        'douglas': [8, 3, 38, 11],
        'alanna': [3, 6],
        'laura': [2],
        'thomas': [14, 19],
        'dad': [5],
        'uncle_tom': [8],
        'aunt_linda': [9],
        'cassandra': [2, 5, 6, 10, 12],
        }
print("\nBack to some numbers!")
for name, number in sorted(favorite_numbers.items()):
    print("\n" + name.title() +
            "'s favorite number(s)")
    for num in sorted(number):
        print(str(num))

# Finally, nesting a dictionary inside a dictionary

my_families = {
    'father': {
        'name': ['michael'],
        'dob': ['06-10-53'],
        'numbers': ['unknown'],
        },
    'mother': {
        'name': ['rhonda', 'singer'],
        'dob': ['05-25-55'],
        'numbers': [5, 7, 55],
        },
    'self': {
        'name': ['douglas'],
        'dob': ['03-08-82'],
        'numbers': [11, 8, 3, 38, 82, 83],
        },
    'spouse': {
        'name': ['laura'],
        'dob': ['06-19-83'],
        'numbers': ['unknown'],
        },
    }

print("\nFinally, we're back to the first list of families. Here's the info we've got.")

for identities, keys in sorted(my_families.items()):
    print("\n" + identities.title())
    for key, value in sorted(keys.items()):
        print("    " + key.title())
        for v in sorted(value):
            print("        " + str(v).title())



