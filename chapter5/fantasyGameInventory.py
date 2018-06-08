# A data structure (dictionary) that models a players inventory.

# This function takes in a dictionary inventory and displays it in console.
def displayInventory( bag ) :
	numbOfItems = 0
	print( 'Inventory:' )
	# Iterates through dictionary printing the keys (k) and values (v)
	for k,v in bag.items() :
		numbOfItems = numbOfItems + v
		print( str(v) + ' ' + k )
	# Prins total number of items in inventory/dictionary.
	print( 'Total number of items: ' + str(numbOfItems) )


def main() :
	# Inventory.
	inventory = {'rope' : 1, 'torch' : 6, 'gold coin' : 42 , 'dagger' : 1, 'arrow' : 12}
	displayInventory(inventory)


if __name__ == '__main__':
	main()