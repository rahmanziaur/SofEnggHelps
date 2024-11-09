import unittest
from RE_checker import namecheck

# Run with testrunner so needs to be in file test_
# File is test_alltests_namechecker

class TestNameCheck (unittest.TestCase):

	def test_alphaname (self):
		self.assertFalse (namecheck ('Sommerville'))

	def test_namewithquote (self):
		self.assertFalse (namecheck ("O'Reilly"))

	def test_namewithhyphen (self):
		self.assertFalse (namecheck ('Washington-Wilson'))

	def test_shortname (self):
		self.assertFalse ('Sx')

	def test_namewithdigit (self):
		self.assertTrue (namecheck('C-3PO'))

	def test_namewithinvalidchar (self):
		self.assertTrue (namecheck('Sommer_ville'))

	def test_nametooshort (self):
		self.assertTrue (namecheck ('S'))

	def test_nametoolong (self):
		self.assertTrue (namecheck ('Thisisalongstringwithmorethen40charactersfrombeginningtoend'))

	def test_doublequote (self):
		self.assertTrue (namecheck ("Thisis'maliciouscode'"))

	def test_namewithdoublehyphen (self):
		self.assertTrue (namecheck ('--badcode'))

	def test_namewithspaces (self):
		self.assertTrue (namecheck ('Washington Wilson'))

	def test_namestartswithhyphen (self):
		self.assertTrue (namecheck ('-Sommerville'))

	def test_namestartswithquote (self):
		self.assertTrue (namecheck ("'Reilly"))