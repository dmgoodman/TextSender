import fbchat
import threading
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from get_credentials import get_credentials

MYSELF = 100015764883289 # User id for Daniel Goodman
RECEIVER = MYSELF # User to receive messages
SENDER_EMAIL, SENDER_PASSWORD = get_credentials()
RECEIVED_SHEET = "https://docs.google.com/spreadsheets/d/1pjOFuiHlovNNI4E_EELDpvy1BGpsueMTPnuxkh9oIs0/edit#gid=0"

def send(message):
	client = fbchat.Client(SENDER_EMAIL, SENDER_PASSWORD)
	sent = client.sendMessage(message, thread_id=RECEIVER)
	if sent: 
		print("Message sent successfully!")
	else:
		print("Oh my lord, something went wrong.")

def handle_sheet(sheet):
	''' Return list of messages and delete corresponding rows in sheet if sheet not empty. Else return []. '''

	# Access values in sheet
	messages = sheet.col_values(1)
	num = len(messages)

	# Remove empty messages
	for i in range(num):
		if messages[i] == "":
			messages.remove(i)

	# Delete all messages from sheet
	if num >= 1:
		sheet.update("A1", "")
	elif num > 1:
		sheet.delete_rows(2, num)

	return messages

def loop(sheet):
	threading.Timer(5.0, loop, args=[sheet]).start()

	messages = handle_sheet(sheet)
	for message in messages:
		message = message.split("///", 3)
	
		message_string = message[1] if len(message[2]) == 0 else message[2]
		message_string += ": " + message[3]
		send(message_string)


if __name__ == "__main__":
	# Use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('CLIENT-SECRET.json', scope)
	client = gspread.authorize(creds)

	# Find a workbook by number and open the first sheet
	sheet = client.open_by_url(RECEIVED_SHEET)
	sheet = sheet.get_worksheet(0)

	loop(sheet)
	