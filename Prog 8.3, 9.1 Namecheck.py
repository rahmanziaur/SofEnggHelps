import re

def namecheck (s):

	# checks that a name only includes alphabetic characters, -, or single quote
	# names must be between 2 and 40 characters long
	# quoted strings and -- are disallowed

	namex = r"^[a-zA-Z][a-zA-Z-']{1,39}$"
	if re.match (namex, s):
		print ('name matched ok')
		if re.search ("'.*'", s) or re.search ("--", s):
			return False
		else:
			return True
	else:
			return False

def main ():
	matchstring = ''
	#print ('Regular expression is: ', regex)
	while matchstring != 'end':
		matchstring = input ('input string to match: ')
		print ('string input: ', matchstring)
		valid = namecheck (matchstring)
		if valid:
			print ('input is valid')
		else:
			print ('no match input is invalid')

if __name__ == '__main__':
	main()