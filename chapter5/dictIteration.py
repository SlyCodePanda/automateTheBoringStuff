# The dictionary.
spam = {'color': 'red', 'age' : 42}

# Iterate over and pring out the values in the dictionary.
for v in spam.values() :
	print(v) # Will print: red 42


# Iterate over and print out the keys in the dictionary.
for k in spam.keys() :
	print(k) # Will print: color age


# Iterate over and print out both the keys and values (key-value pairs) in the dictionary.
for i in spam.items() :
	print(i) # Will print: ('color', 'red') ('age', 42)


# You can use the multiple assignment trick in a for loop to assign the key and value to seperate variables.
for k, v in spam.items() :
	print( 'Key: ' + k + ' Value: ' + str(v) )
	# this will print:
	#Key: age Value: 42
	#Key: color Value: red