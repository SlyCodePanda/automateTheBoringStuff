#! python3
# pw.py - An insecure password locker program.

# Dictionary that organizes your account and password data.
PASSWORDS = {'email' : 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
			 'blog' : 'VmALvQyKAxiVH5G8v01if1MLZF3sdt', 
			 'luggage' : '12345'}

import sys, pyperclip

# If the user does not add the command line argument, print usage information
if len(sys.argv) < 2 :
	print( 'Usage: python pw.py [account] - copy account password' )
	sys.exit()

# First comman line arg is the account name.
# The account name is stored in the variable 'account'.
account = sys.argv[1]

# Checks to see whether the account entered exists in the PASSWORDS deictionary as a key.
# If so, then copy the key's value to the clipboard using pyperclip module.
if account in PASSWORDS :
	pyperclip.copy(PASSWORDS[account])
	print( 'Password for ' + account + ' has been copied to clipboard.' )
	sys.exit()
else :
	print( 'There is no account names ' + account )