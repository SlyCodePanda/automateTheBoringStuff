# Takes in a list value as an argument and returns a string with all the items seperated by a comma and a space, with 'and' inserted before the last item.

def comma( items ) :
	# Iterate through the list and add a comma inbetween each item.
	length = len(items)
	sentence = ''

	# Stores the item as a string seperated by commas.
	for item in range(len(items)) :
		# Checks if this is the last item, if so instead of a comma add 'and' then the last time and a fullstop.
		# Then break from the loop.
		if item == length - 1 :
			sentence += 'and ' + items[item] + '.'
			break
		sentence += items[item] + ', '

	return sentence 


def main() :
	myItems = ['cup', 'pencils', 'phone', 'notebooks', 'cat']
	myList = comma(myItems)

	print( myList)

if __name__ == "__main__":
  main()