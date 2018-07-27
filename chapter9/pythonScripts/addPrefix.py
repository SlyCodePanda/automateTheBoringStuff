#! python3
# addPrefix.py - Lets you add a prefix to all files in a given directory (Only currently tested on Windows). 

import os, shutil

# Get the directory that we want to search through from the user. 
print('Please enter the directory that you would like to access:')
print(r"E.g C:\Program Files\ ")

# Check to make sure the directory entered exists.
while True :
	try :
		givenDir = input()
		directory = os.listdir(givenDir)
		print('Found directory...')
		break
	except NameError : 
		print('Please enter a valid directory...')
	except FileNotFoundError :
		print('Please enter a valid directory...')
	except OSError :
		print('Please enter a valid directory...')

# Get the prefix that we want to add to the files.
print('What prefix would you like to add to the files in "%s"?' % givenDir)
prefix = input() + '_'

print('Adding "%s" to file names...' % prefix)

# Loop over the files in the directory given.
for fileName in directory :
	print('Found "%s" in %s' % (fileName, givenDir))

	# New name to give the file found.
	newName = prefix + fileName

	# Get the full, absolute file paths for the original name and what we are changing it to.
	oldName = os.path.join(givenDir, fileName)
	newName = os.path.join(givenDir, newName)

	# Rename each of the files so that they all have the given prefix at the start.
	print('Changing %s to %s' % (oldName,newName))
	shutil.move(oldName, newName)

