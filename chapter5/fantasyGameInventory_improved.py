# A data structure (dictionary) that models a players inventory.
# The user enters items and those items are added to the dictionary, if the user adds the same item multiple times,
# the value associated with that key item will get incremented.

# This function takes in a dictionary inventory and displays it in console.
def displayInventory( bag ) :
	numbOfItems = 0
	print( 'Inventory:' )
	# Iterates through dictionary printing the keys (k) and values (v)
	for k,v in bag.items() :
		numbOfItems = numbOfItems + v
		print( 'x' + str(v) + ' ' + k )
	# Prints total number of items in inventory/dictionary.
	print( 'Total number of items: ' + str(numbOfItems) )

# Adds the items given by user to the inventory ditionary.
def addItems( bag, item ) :
	# If item already exists, Increment the number of that item in the bag
	if item in bag :
		print( 'Adding another ' + item + ' to bag.')
		bag[item] += 1
	# If this is a new item not currently in the bag, add it.
	elif item not in bag :
		print( 'Adding new item to inventory...')
		bag[item] = 1

	return bag


def main() :
	# Inventory.
	inventory = {}

	while True :
		print( 'Please enter an item you would like to add to your inventory (blank to quit):' )
		items = raw_input()
		if items != '' :
			inventory = addItems(inventory, items)
		else :
			break

	displayInventory(inventory)

if __name__ == '__main__':
	main()