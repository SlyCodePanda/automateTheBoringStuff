#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard.

import pyperclip
# Paste text from the clipboard.
text = pyperclip.paste()

# Seperate lines and add stars.
lines = text.split('\n')
# Loop through all the indexes in the 'lines' list.
for i in range(len(lines)):
	# Add star to each string in the 'lines' list.
	lines[i] = '* ' + lines[i]
# Make the list of lines into a single line of text.
text = '/n'.join(lines)

# Copy the new text to the clipboard.
pyperclip.copy(text)