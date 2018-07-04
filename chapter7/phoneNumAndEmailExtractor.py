#! python3
# phoneNumAndEmailExtractor.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Regex to search for phone numbers.
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# Area code.		Optional area code, so the area code group is followed by a quesiton mark. It can be 3 digits OR 3 digits in a parenthesis.
	(\s|-|\.)?					# Seperator.		A seperator can be a space, hyphen, or period.
	(\d{3})						# First 3 digits.	
	(\s|-|\.)					# Seperator.
	(\d{4})						# Last 4 digits.
	(\s*(ext|x|ext.)\s*(\d{2,5}))?			# Extension.		An optional extension made up of spaces followed by ext, x, or ext. Followed by two to five digits.
	)''', re.VERBOSE)				

# Regex to search for emails.
emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+				# Username.		One or more characters that can be any of the following: lowercase and uppercase lettersm numbers, a dot, and underscore, a percent sign, a plus sign, or a hyphen.
	@						# @ symbol.		Username and domain are seperated by a @ symbol.
	[a-zA-Z0-9.-]+					# Domain name.		One or more characters that can be any of the following: letters, numbers, periods, and hyphens.
	(\.[a-zA-Z]{2,4})				# Dot-something.	Between 2 and 4 characters long of letters.
	)''', re.VERBOSE)

# Find the matches in the clipboard text.
text = str(pyperclip.paste())
# Stores the matches in the list 'matches'.
matches = []

for groups in phoneRegex.findall(text):
	# The phoneNum variable contains a string built from groups 1, 3, 5, and 8 of the matched text. (These groups are the area code, first 3 digits, last 4 digits, and the extension.)
	phoneNum = '-'.join([groups[1], groups[2], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

# For email addresses, append group 0 (group 0 matches the entire regular expression) of each match.
for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy the results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to the clipboard: ')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')
