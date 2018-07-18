# This method takes in a dictionary of info and uses center(), ljust(), and rjust() to display that information
# in a neatly aligned table-like format.
def printPicnic( itemsDict, leftWidth, rightWidth ) :
	print( 'PICNIC ITEMS'.center(leftWidth + rightWidth, '-') )
	for k, v in itemsDict.items() :
		print( k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches' : 4, 'apples' : 12, 'cups' : 4, 'cookies' : 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

''' Will print something that looks like this :
---PICNIC ITEMS--
sandwiches..    4
cookies..... 8000
apples......   12
cups........    4
-------PICNIC ITEMS-------
sandwiches..........     4
cookies.............  8000
apples..............    12
cups................     4
'''
