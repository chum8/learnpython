# Python Exercise 4. Working with Lists

states = ['colorado', 'north carolina', 'indiana', 'nebraska']

print("A list of states I've lived in, generated using a loop:\n")
for state in states:
    print(state.title())
    print("Thanks, " + state.title() + ", it was fun to live within your borders!\n")
print("I've lived in several states.")

print("\nHere are some square numbers.")
digits = []
for value in range(11, 31):
    print(str(value) + " squared is " + str(value**2))
    digits.append(value)

print("\nSome information about the numbers we just squared.")
print("The smallest number was: " + str(min(digits)))
print("The largest number was: " + str(max(digits)))
print("The sum of the digits is: " + str(sum(digits)))

# Using list comprehension

print("\nWe are now going to make a list using cubes of the numbers.")
cubes = [value**3 for value in range(11, 31)]
print(cubes)

print("\nLet's find some information about a list with over a million numbers.")
million_plus = [value for value in range(1, 1438595)]
# print(million_plus) # comment out if not wanting to see the output every time
print("The smallest number was: " + str(min(million_plus)))
print("The largest number was: " + str(max(million_plus)))
print("The sum of the digits is: " + str(sum(million_plus)))

# Using slices

relatives = ['wade', 'marjorie', 'keith', 'molly', 'mike', 'rhonda', 'emily', 'keith', 'alanna', 'louisa', 'laura', 'nathan', 'edmund', 'lavinia', 'rosamund', 'rafe']

print("\nA lot of my relatives.")
print(relatives)
print("\nSome of my relatives.")
print(relatives[6:9])
print("\nA different list of my relatives.")
print(relatives[:5])
print("\nA list of relatives containing only names of my kiddos.")
print(relatives[-4:])
print("\nAnd, the whole gang once again, formatted more nicely!")
for relative in relatives:
    print(relative.title())

# Copying a list to a new one

energy_drinks = ['monster rehab', 'monster java', 'full throttle', 'nos']
friend_drinks = energy_drinks # this points both variables to the same list
energy_drinks.append('nos low carb') # so this will end up on the friend list
print("\nMy friend's favorite energy drinks are")
for drink in friend_drinks:
    print(drink.title())
print("\nOops, mistake!")

energy_drinks = ['monster rehab', 'monster java', 'full throttle', 'nos']
friend_drinks = energy_drinks[:] # this slices friend_drinks to a fresh list
energy_drinks.append('nos low carb') # so now this change won't affect friend_drinks
print("\nMy friend's favorite energy drinks are")
for drink in friend_drinks:
    print(drink.title())
print("\nCorrect this time!")

# Tuples
primes = (1, 2, 3, 5, 7, 11, 13) # we never want this to change, so we put it in a tuple

# primes[2] = 4 # generates an error

print("\nHere are some prime numbers we've listed in a tuple.")
for prime in primes:
    print(prime)

primes = (4, 6, 8, 9, 10, 12, 14, 15, 16)
print("\nNow, we've re-written the tuple to show numbers that are not prime.")
for non_prime in primes:
    print(non_prime)


