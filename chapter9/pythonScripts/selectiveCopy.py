#! python3

# selectiveCopy.py - Walks through a folder tree and searches for files with a certain file extension. Then copies and pastes these files to a new location/folder.

import os, shutil

# TODO: Get the folder you want to search through.
def selectiveCopy(folder) :

	folder = os.path.abspath(folder) # Make sure the folder is absolute.
	# Search for files with this extension.
	extension = '.py'
	# Destination of where to copy the found files.
	dest = folder + '/pythonScripts/'

	# Check if pythonScripts folder already exists. If it doesn't, create it.
	if not os.path.exists(dest) :
		os.makedirs(os.path.dirname(dest))
		print('Creating scripts file here: %s' % dest ) 

	# Walk the given folder structure to find the files with the extension.
	for foldername, subfolders, filenames in os.walk(folder) :
		print('Currently looking at folder: %s' % foldername)
		print('Found subfolders: %s' % subfolders)

		for filename in filenames :
			# If a file with the given extension is found, copy it to pythonScripts folder.
			if filename.endswith(extension) :
				print('Python script found! : %s' % filename)
				# TODO: Copy those files, and paste them into a new folder.
				copyTo = dest + filename
				shutil.copy(filename, copyTo)


# Currently set to search through the current directory.
selectiveCopy('.')