def get_credentials(filepath="CREDENTIALS.txt"):
	''' Extracts credentials from a credentials file - default is
		CREDENTIALS.txt. The file must contain two lines: one with
		the sender's email and the second with the sender's password.
	'''

	c = open(filepath, "r")
	email = c.readline().strip()
	password = c.readline().strip()
	c.close()
	return email, password