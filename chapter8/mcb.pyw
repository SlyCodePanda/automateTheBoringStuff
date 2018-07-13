#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#		 py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# 		 Py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# ---Save clipboard content.---
# If the first command line argument (which will always be at index 1 of the sys.argv list) is 'save'.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save' :
	# The second command line argument is the keyword for the current content of the clipboard. THe keyword will be used as the key for mcbShelf, and the value will be the text currently on the clipboard.
	mcbShelf[sys.argv[2]] = pyperclip.paste()
# If there is only one command line argument, you will assume it is either 'list' or a keyword to load content onto the clipboard.
elif len(sys.argv) == 2 :
	# ---List keywords and load content.---
	# If there is only one command line argument, first check whether it's 'list'.
	if sys.argv[1].lower() == 'list' :
		# If it's 'list', a string representation of the list of shelf keys will be copied to the clipboard.
		pyperclip.copy(str(list(mcbShelf.keys())))
	# Otherwise, assume the command line argument is a keyword. If the keyword exists in the mcbShelf shelf as a key, you can load the value onto the clipboard.
	elif sys.argv[1] in mcbShelf :
		pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()