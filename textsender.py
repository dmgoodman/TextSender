import fbchat
import threading
from get_credentials import get_credentials

MYSELF = 100015764883289 # User id for Daniel Goodman
RECEIVER = MYSELF # User to receive messages
SENDER_EMAIL, SENDER_PASSWORD = get_credentials()
SHEET = ""

def send(message):
	client = fbchat.Client(SENDER_EMAIL, SENDER_PASSWORD)
	sent = client.sendMessage(message, thread_id=RECEIVER)
	if sent: 
		print("Message sent successfully!")
	else:
		print("Oh my lord, something went wrong.")

def handle_sheet(sheet):
	''' Return list of messages and delete corresponding rows in sheet if sheet not empty. Else return []. '''

	# Access sheet

	messages = []
	# Populate messages and delete from sheet

	return messages

def loop():
	threading.Timer(5.0, loop).start()

	messages = handle_sheet(SHEET)
	for message in messages:
		message = message.split("///", 3)
	
		message_string = message[1] if len(message[2]) == 0 else message[2]
		message_string += ": " + message[3]
		send(message_string) 

	print("looped")


if __name__ == "__main__":
	loop()
	