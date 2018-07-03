# Checks whether a string matches the pattern of a phone number, returning 'true' or 'false'. e.g '415-555-4242' is a valid phone number.

def isPhoneNumber( text ) :
	# Check that the string is exactly 12 characters long.
	if len(text) != 12 :
		return False
	# Then checks that the area code(first 3 chars) consists of only numeric characters.
	for i in range(0, 3) :
		if not text[i].isdecimal() :
			return False
		# The number must have the first hyphen after the area code. 
		if text[3] != '-' :
			return False
		for i in range(4, 7) :
			# Three more numeric characters.
			if not text[i].isdecimal() :
				return False
		# Then another hyphen.
		if text[7] != '-' :
			return False
		for i in range(8, 12) :
			# And finally four more numbers.
			if not text[i].isdecimal():
				return False
		# If the program execution manages to get past all the checks, it returns True.
		return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)) :
	# On each loop, a new chunk of 12 characters from 'message' is assigned to the variable 'chunk'.
	chunk = message[i:i+12]
	#print('checking: ' + chunk + '...')
	# Pass the chunk to the function to check if that chunk is a phone number.
	if isPhoneNumber(chunk) :
		print('Phone number found: ' + chunk)
print('Done')