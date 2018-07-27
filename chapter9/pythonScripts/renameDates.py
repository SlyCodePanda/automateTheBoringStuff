#! python3
#renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re 

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) 	# all text before the date
((0|1)?\d)- 							# one or two digits for the month
((0|1|2|3)?\d)- 						# one or two digits for the day
((19|20)\d\d) 							# four digits for the year
(.*?)$ 									# all text after the date
""", re.VERBOSE)						# VERBOSE allows whitespace and comments in the regex string to make it more readable.

# The directory that we are searching through.
searchDir = os.listdir('.\\renameDatesTestFiles')
print('Searching ' + str(searchDir))

# Loop over the files in the working directory.
for amerFilename in searchDir :
	mo = datePattern.search(amerFilename)

	# Skip files without a date.
	if mo == None :
		continue	# Skip the rest of the loop and move on to the next filename.

	# Get the different parts of the filename.
	beforePart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

	# Form the European-style filename.
	euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

	# Get the full, absolute file paths.
	absDir = os.path.abspath('.\\renameDatesTestFiles')
	amerFilename = os.path.join(absDir, amerFilename)
	euroFilename = os.path.join(absDir, euroFilename)

	# Rename the files.
	print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
	shutil.move(amerFilename, euroFilename)	# uncomment after testing.