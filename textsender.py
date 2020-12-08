import fbchat
import threading
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from get_credentials import get_credentials
from time import sleep

SENDER_EMAIL, SENDER_PASSWORD, RECEIVER, INBOX_SHEET, OUTBOX_SHEET = get_credentials()

def send(message):
	client = fbchat.Client(SENDER_EMAIL, SENDER_PASSWORD)
	sent = client.sendMessage(message, thread_id=RECEIVER)
	if sent: 
		print("Message sent successfully!")
	else:
		print("Oh my lord, something went wrong.")

def handle_sheet(sheet):
	''' Return list of messages and delete corresponding rows in sheet
		if sheet not empty. Else return []. '''

	# Access values in sheet
	all_messages = sheet.col_values(1)
	num = len(all_messages)

	messages = []
	# Remove empty messages
	for i in range(num):
		message = all_messages[i]
		if len(message) > 0:
			messages.append(message)

	# Delete all messages from sheet
	if num >= 1:
		sheet.update("A1", "")
	if num > 1:
		sheet.delete_rows(2, num)

	return messages

def handle_outbox(sheet):
	pass

def loop(sheet_in, sheet_out):
	''' Called every 5 seconds to handle input and output sheets.
		If sheet_in contains values, send those values via Messenger.
		If Messenger contains new messages, add those to sheet_out. '''

	threading.Timer(5.0, loop, args=[sheet_in, sheet_out]).start()

	try:
		messages = handle_sheet(sheet_in)
		for message in messages:
			message = message.split("///", 3)
		
			message_string = message[1] if len(message[2]) == 0 else message[2]
			message_string += ": " + message[3]
			send(message_string)

		outbox = handle_outbox(sheet_out)
	except Exception as e:
		pass


def main():
	try:
		# Use credentials to create a client to interact with the Google Sheets API
		scope = ['https://spreadsheets.google.com/feeds']
		creds = ServiceAccountCredentials.from_json_keyfile_name('CLIENT-SECRET.json', scope)
		client = gspread.authorize(creds)

		# Open Google Sheet by URL and get first worksheet
		sheet_in = client.open_by_url(INBOX_SHEET)
		sheet_in = sheet_in.get_worksheet(0)

		sheet_out = client.open_by_url(OUTBOX_SHEET)
		sheet_out = sheet_out.get_worksheet(0)

		loop(sheet_in, sheet_out)
	
	except Exception as e:
		print("h")
		sleep(5)
		main()


if __name__ == "__main__":
	main()