# I am using python3 for this program, therefore I am not using raw_input().
# As raw_input is no longer in included in Python3.

# This program will keep asking you to enter an age that is only numbers.
# And a password that consists of only letters or numbers (no symbols).

while True :
	print( 'Enter your age' )
	age = input()
	# If age is valid, break out of loop.
	if age.isdecimal() :
		break
	print( 'Please enter a number for your age.' )

while True :
	print( 'Select a new password (letters and numbers only):' )
	password = input()
	if password.isalnum() :
		break
	print( 'Passwords can only have letters and numbers.' )

