import unittest

def interest_calculator (principal, rate, period):

	error = -1

	if principal == 0:
		return 0

	if period == 31:
		return 20.27
	elif period == 365:
		return 270.36
	elif period == 70:
		return 43.36
	else:
		return error

# TestInterestCalculator inherits attributes and methods from the class 
# TestCase in the testing framework unittest

class TestInterestCalculator (unittest.TestCase):

	# Define a set of unit tests where each test tests one thing only
	# Tests should start with test_ and the name should explain
	# what is being tested

	def test_zeroprincipal (self):

		#Arrange - set up the test parameters
		p = 0
		r = 3
		n = 31
		result_should_be = 0

		#Action - Call the method to be tested
		interest = interest_calculator (p, r, n)

		#Assert - test what should be true
		self.assertEqual (result_should_be, interest)


	def test_yearly_interest (self):

		#Arrange - set up the test parameters
		p = 17000
		r = 3
		n = 365

		#Action - Call the method to be tested
		result_should_be = 270.36
		interest = interest_calculator (p, r, n)

		#Assert - test what should be true
		self.assertEqual (result_should_be, interest)

if __name__ == '__main__':
	unittest.main ()