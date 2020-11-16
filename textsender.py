import fbchat
from get_credentials import get_credentials

MYSELF = 100015764883289 # User id for Daniel Goodman
RECEIVER = MYSELF # User to receive messages
SENDER_EMAIL, SENDER_PASSWORD = get_credentials()

def send(message):
	client = fbchat.Client(SENDER_EMAIL, SENDER_PASSWORD)
	sent = client.sendMessage(message, thread_id=RECEIVER)
	if sent: 
		print("Message sent successfully!")
	else:
		print("Oh my lord, something went wrong.")

def check_sheet():
	return "What in the world is the date?"

if __name__ == "__main__":
	message = check_sheet()
	send(message)