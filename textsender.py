import fbchat

MYSELF = 100015764883289 # User id for Daniel Goodman

RECEIVER = MYSELF # User to receive messages

# Include a CREDENTIALS.txt file containing two lines
# The first must contain the sender's email
# The second must contain the sender's password
CREDENTIALS = open("CREDENTIALS.txt", "r")

SENDER_EMAIL = CREDENTIALS.readline().strip()
SENDER_PASSWORD = CREDENTIALS.readline().strip()
CREDENTIALS.close()

def send(message):
	client = fbchat.Client(SENDER_EMAIL, SENDER_PASSWORD)
	sent = client.sendMessage(message, thread_id=RECEIVER)
	if sent: 
		print("Message sent successfully!")
	else:
		print("Oh my lord, something went wrong.")

send("What in the world is the date?")