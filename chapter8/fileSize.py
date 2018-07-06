# fileSize.py - Finds the total size of a given directory.

#!python3

import os


print('Enter the directory that you want to see the size of:')
print(r" E.g C:\Program Files ")

# Get directory from user and error handling.
while True :
	try :
		givenDir = input()
		directory = os.listdir(givenDir)
		break
	except NameError : 
		print('Please enter a valid directory...')
	except FileNotFoundError :
		print('Please enter a valid directory...')
	except OSError :
		print('Please enter a valid directory...')

totalSize = 0

# Loops over each filename in the given directory, the totalSize variable is incremented by the size of each file.
for filename in directory :
	# Uses 'os.path.join()' to join the folder name with the current filename.
	totalSize = totalSize + os.path.getsize(os.path.join(givenDir, filename))

# Round up to 2 decimal places for Megabyte conversion.
mb = str(round(totalSize/1024/1024, 2))

print('Size of ' + givenDir + ' :')
print(str(totalSize) + ' bytes')
print(str(mb) + ' megabytes')