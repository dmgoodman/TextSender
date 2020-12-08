import sys

def check_credentials(filepath):
	''' Asserts that credentials file is correctly formatted. 
		Exits with error message if improper formatting.
	'''

	c = open(filepath, "r")
	lines = ["RECEIVER-ID", "SENDER-EMAIL", "SENDER-PASSWORD", "INBOX-SHEET", "OUTBOX-SHEET"]

	for i in range(len(lines)):
		try:
			c.readline().strip().split(": ", 1)[1]
		except Exception as e:
			error_msg = "Error in " + filepath + ". " + lines[i] + " line incorrectly formatted."
			sys.exit(error_msg)


def get_credentials(filepath="CREDENTIALS.txt"):
	''' Extracts credentials from a credentials file - default is
		CREDENTIALS.txt. File must contain five lines in format:
		RECEIVER-ID: facebook-id
		SENDER-EMAIL: email-address
		SENDER-PASSWORD: facebook-password
		INBOX-SHEET: full-google-sheet-url
		OUTBOX-SHEET: full-google-sheet-url
	'''

	check_credentials(filepath)

	c = open(filepath, "r")
	receiver = c.readline().strip().split(": ", 1)[1]
	email = c.readline().strip().split(": ", 1)[1]
	password = c.readline().strip().split(": ", 1)[1]
	inbox = c.readline().strip().split(": ", 1)[1]
	outbox = c.readline().strip().split(": ", 1)[1]
	c.close()
	return receiver, email, password, inbox, outbox
