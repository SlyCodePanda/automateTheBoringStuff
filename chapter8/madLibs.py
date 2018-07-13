#! python3

# madLibs.py - Reads in text files and lets the user add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re

# Open file.
readFile =  open("madLibs-ReadText.txt", "r")

# The new text to save to a new file.
newFile = ""

# Loops through the lines in the text file, breaking each line up into individual words.
with readFile as file:
	for line in file :
		# Finds all punctuation in the text, and breaks it apart from the word it is next to. So you don't get something like word = "VERB."
		line = re.findall(r"[\w']+|[.,!?;]", line)
		for word in line :
			# If while looping through the text, you find ADJECTIVE, NOUN, ADVERB, or VERB, ask the user to enter in their own word for and replace the text with it.
			if word == "ADJECTIVE" :
				print("Please enter an adjective:")
				adj = input()
				newFile += adj + " "
			elif word == "NOUN" :
				print("Please enter a noun:")
				noun = input()
				newFile += noun + " "
			elif word == "ADVERB" :
				print("Please enter an adverb:")
				adV = input()
				newFile += adV + " "
			elif word == "VERB" :
				print("Please enter a verb:")
				ver = input()
				newFile += ver + " "
			else: 
				newFile += word + " "



# Print out the new text file.
print('\n' + newFile)

# Write the newFile to a new text file.
createFile = open("madLibs-WriteText.txt", "w")
createFile.write(newFile)
createFile.close()


readFile.close()