#!/usr/local/bin/python3

def check_credit_rating (name, postcode, dob):

	# Service simulation. The values returned by the service have to be input by the user.
	# These are NOT validated as this is simply a test program.

	nm = input (' Name: (' + name + ') ')
	pc= input ('postcode: ('+ postcode+') ')
	dob = str(input ('Date of birth '+ dob+' '))
	rating = input ('Credit rating: (0-600) ')
	errcode = input ('Error code: (0-2) ')
	CR = [nm, pc, dob, int(rating), int (errcode)]
	return CR


def do_normal_processing (cr):
	print ('Normal processing')

def do_exception_processing (cr, name, postcode, dob, request_ok):
	print ('Abnormal processing')
	if request_ok:
		print (' External service request failed with known error. Error code = ', cr [4])
	else:
		print ('External service request failed with unknown error.')
		print (cr)
		if (cr [3] < 0 or cr [3] > 600):
			print (cr[3])
			print ('Credit rating error')
		if (cr[4] < 0 or cr[4] > 2):
			print (cr[4])
			print ('Incorrect return code')
		if cr [0] != name:
			print ('Inconsistent names')
		if cr[1] != postcode:
			print ('inconsistent postcodes')
		if cr[2] != dob:
			print ('Inconsistent dobs ', cr [2], dob)

def credit_checker (name, postcode, dob):

	# Assume that the function check_credit_rating calls an external service 
	# to get a person's credit rating. It takes a name, postcode (zip code) and 
	# date of birth as parameters and returns a sequence with the database 
	# information (name, postcode, date of birth) plus a credit score between 0 and 600
	# The final element in the sequence is an error_code which may 
	# be 0 (successful completion), 1 or 2.


	NAME = 0
	POSTCODE = 1
	DOB = 2
	RATING = 3
	RETURNCODE = 4
	REQUEST_SUCCESS = True
	ASSERTION_ERROR = False

	cr = ['', '', '', -1, 2]

	# Check credit rating simulates call to external service

	cr = check_credit_rating (name, postcode, dob)

	try:
		assert cr [NAME] == name and cr [POSTCODE] == postcode and cr [DOB] == dob \
			and (cr [RATING] >= 0 and cr [RATING] <= 600) and \
			(cr[RETURNCODE] >= 0 and cr[RETURNCODE] <= 2)
		if cr[RETURNCODE] == 0:
			do_normal_processing (cr)
		else:
			do_exception_processing (cr, name, postcode, dob, REQUEST_SUCCESS)
	except AssertionError:
			do_exception_processing (cr, name, postcode, dob, ASSERTION_ERROR)
		

def main ():

	# Initial test data. 

	tests = [['Sommerville', 'eh74nh', '230781'],['Wilson', 'ml106lt', '200458'],['Ferguson', 'ab105nq', '020772']]

	for i in range (0, len(tests)):
		credit_checker (tests [i][0], tests [i][1], tests [i][2])

if __name__ == '__main__':
	main()
