# Python Exercise 3. Introducing Lists

composers = ['j.s. bach', 'handel', 'haydn', 'mozart', 'beethoven', 'mendelssohn']
print("\nSome composers in our list:")
print(composers[0].title())
print(composers[3].title())
print(composers[-1].title()) #Python's special way of referencing the final index
print(composers[-4].title()) #return the item four from end of list
message = "\nSome argue that " + composers[1].title() + " was more gifted than " + composers[-1].title() + ".\n"
print(message)

# Adding and removing elements from a list

american_autos = ['ford', 'chevrolet', 'plymouth', 'chrysler']
print("Our list of American Autos so far:")
print(american_autos)
print("Since " + american_autos[2].title() + " no longer exists, we will replace that list item with Buick.\n")
print("The list after performing replacement:")
american_autos[2] = 'buick'
print(american_autos)
print("\nLet's add some more and see what we've got now:")
american_autos.append('toyota')
american_autos.append('lincoln')
american_autos.append('ferrari')
american_autos.append('tesla')
american_autos.append('jaguar')
print(american_autos)
print("\nSome of these items do not belong on a list of American Autos.  Let's reomve them, resulting in:")

# Three different ways to remove an element

american_autos.pop()
del american_autos[-4]
american_autos.remove('ferrari') # but this only removes the first instance, so be careful
print(american_autos)

print("\nLastly, we'll insert a new value right into the middle.")
american_autos.insert(3, 'pontiac')
print(american_autos)

# Sorting lists

print("\nNow let's put the list in both alphabetical and reverse alphabetical order:")
american_autos.sort()
print(american_autos)
american_autos.sort(reverse=True)
print(american_autos)

soft_drinks = ['coke', 'diet coke', 'pepsi', 'dr. pepper', 'sierra mist', 'mountain dew', 'cheerwine', 'fanta orange', 'fanta strawberry', 'fanta grape', '7up']
print("\nHere's a new list -- of soft drinks this time.")
print(soft_drinks)
print("\nNow, we will print them in alphabetical and reverse alphabetical order without actually sorting them.")
print(sorted(soft_drinks))
print(sorted(soft_drinks, reverse=True))
print("\nHere's the original for proof that it's still the same!")
print(soft_drinks)
print("\nBut just for fun, let's reverse it:")
soft_drinks.reverse()
print(soft_drinks)
print("\nBy the way, in case you're curious, we offer " + str(len(soft_drinks)) + " kinds of soft drinks.")

# forcing an index error on purpose.  Commented out after testing.

#print(soft_drinks[11])
