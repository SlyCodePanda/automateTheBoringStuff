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

	# Create the zip file.
	print('Creating %s...' % (zipFileName))
	backupZip = zipfile.ZipFile(zipFileName, 'w')

	# Walk the entire folder tree and compress the files in each folder.
	for foldername, subfolders, filenames in os.walk(folder) :
		print('Adding files in %s...' % (foldername))
		# Add the currrent folder to the ZIP file.
		backupZip.write(foldername)

		# Add all the files in this folder to the ZIP file.
		for filename in filenames :
			newBase = os.path.basename(folder) + '_'
			if filename.startswith(newBase) and filename.endswith('.zip') :
				continue	# Don't backup the backup ZIP files.
			backupZip.write(os.path.join(foldername, filename))
	backupZip.close()		
	print('Done.')

backupToZip('./backupToZipTestFolder/')