# This program lets the user type in a pet name, checks to see whether the name is in a list of pets.
# If the name is not in the list, add it. If it's in the list, do nothing.
import sys

myPets = ['Zophie', 'Pooka', 'Fat-tail']

# Keep requesting to add pets until the user types 'n' when asked 'Would you like to continue?'.
while True :
	print( 'Enter a pet name: ')
	name = raw_input()

	if name not in myPets :
		print( 'This pet is not in the list, I shall add it now' )
		myPets.append(name)
		print( 'The number of pets in your list is ' + str(len(myPets)) )
		print('')

	else :
		print( 'The name ' + name + ' is already in the list.' )
		print( 'The number of pets in your list is ' + str(len(myPets)) )
		print('')

	print( 'Would you like to continue? (y or n)' )
	cont = raw_input()

	if cont == 'n' :
		print( 'The number of pets in your list is ' + str(len(myPets)) )
		print( 'The pets in your list are: ')
		for i in range(len(myPets)) :
			print( myPets[i] )
		sys.exit()