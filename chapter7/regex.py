# Import the regular expressions (regex) functions.
import re

# Create regex object and store it in phoneNumRegex variable.
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Searches the passed string for any matches to the regex. ('mo' -> Match Objects)
mo = phoneNumRegex.search('My number is 415-555-4242.')
# If the searched pattern is found, it will return a Match object. Match objects have a 'group()' method that will return the matched text.
print('Phone number found: ' + mo.group())