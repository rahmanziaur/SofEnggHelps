#!/usr/local/bin/python3

import os, time
test_root = "/users/iansommerville/Dropbox/Python/Engineering Software Book/"


def encrypt_workfile (wf, encf):
	# Encryt the workfile and write the encrypted file to encf
	print ('encrypting workfile')

def do_normal_processing (wf, ef):
	# Normal processing here. Code below simulates exceptions
	# rather than normal processing
	try:
		wf.write ('line 1\n')
		ef.write ('encrypted line 1')
		wf.write ('line 2\n')
		wf.close()

		print ('Force exception by trying to open non-existent file')
		tst = open (test_root+'nofile')
	except IOError as e:
		print ('I/O exception has occurred')
		raise e


def main ():

	wf = open (test_root+'workfile.txt', 'w')
	ef = open(test_root+'encrypted.txt', 'w')

	try:
		do_normal_processing (wf, ef)

	except Exception:
		# If the modification time of the unencrypted work file is later than
		# the modification time of the encrypted file then
		# encrypt and write the workfile

		print ('Secure shutdown')

		wf_modtime = os.path.getmtime(test_root+'workfile.txt')
		ef_modtime = os.path.getmtime(test_root+'encrypted.txt')

		if wf_modtime > ef_modtime:
			encrypt_workfile (wf, ef)
		else:
			print ('Workfile modified before encrypted')

		wf.close()
		ef.close()

		print ('Deleting the workfile')
		os.remove (test_root+'workfile.txt')

		print ('Secure shutdown complete')
	

if __name__ == '__main__':
	main()
