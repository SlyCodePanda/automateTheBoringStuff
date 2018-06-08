# This program counts the number of occurrences of each letter in a string.

print('Enter a word or sentence you would like to count: ')
message = raw_input()

# Empty dictionary.
count = {}

# Loops over each character in the message string, counting how often each character appears.
for character in message:
	# setdefault method call ensures that the key is in the count dictionary.
	count.setdefault(character, 0)
	# Increments the value associated with that key by one.
	# Access the associated value using square-braces.
	count[character] = count[character] + 1

print(count)