# strongPasswordDetection.py - uses regular expressions to make sure the password string it passes is strong. A strong password must have at least 8 characters long, contains both uppercase and lowercase letters, and have at least one digit.

#!python3
import re

password = input()
# password = "tfgsYiop1"
print("password = " + password)

# Regex that detects whether the password is strong.
passRegex = re.compile(r'''(
	^
	(?=.*[A-Z])		# Has at least one uppercase letter
	(?=.*[a-z])		# Has at least one lowercase letter
	(?=.*\d)		# Has as least one digit
	.{8,}			# Is at least 8 characters long
	$
	)''', re.VERBOSE)

# If mo is returned for each of these regexes, the password is strong.
mo = passRegex.search(password)

if not mo :
	print(password + " is not a strong enough password.")
	print("Must have upper and lower case, and must be 8 characters long.")
else:
	print(password + " is a strong password!")