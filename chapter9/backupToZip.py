#! python3
# backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder) :
	# Backup the entire contents of "folder" into a zip file.

	folder = os.path.abspath(folder) # Make sure the folder is absolute.

	# Figure out the filename this code should use based on what files already exist.
	number = 1
	while True:
		zipFileName = os.path.basename(folder) + '_' + str(number) + '.zip'
		if not os.path.exists(zipFileName) :
			break
		number = number + 1

	# TODO: Create the zip file.

	# TODO: Walk the entire folder tree and compress the files in each folder.
	print('Done.')

backupToZip('D://backupToZipTestFolder')