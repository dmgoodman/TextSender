# Introduction and rationale
**INCOMPLETE**

As human communication has moved into the electronic age, there has been an influx of new ways to communicate. People have greatly differing preferences as to which of these platforms is easiest, from standard SMS messaging, to WhatsApp, to Facebook Messenger, and plenty more. In the pastThis particular repository serves to solve a very specific set of preferences and conditions - those who use Android phones for sending and receiving SMS messages, but would prefer to receive them on Facebook Messenger. 

# Set-up
## You will need
* An Android device that receives SMS messages
* A Facebook account for use on Facebook Messenger (https://messenger.com/)
* An IFTTT account (https://ifttt.com)
* The IFTTT app installed on your Android device (https://play.google.com/store/apps/details?id=com.ifttt.ifttt)
* A Google account (https://accounts.google.com/)
* Python 3.8
	* https://www.python.org/downloads/, scroll down to "Looking for a specific release?"
	* 3.8.6 is guaranteed to work. Future or previous versions may work as well, but are not guaranteed.
* __Optional, but preferred:__ A second Facebook account. Facebook is known to lock accounts when there is suspicious activity (read: a chatbot sending messages on your behalf). To avoid this, it's best to have a second account.

## Steps
__Prepare IFTTT:__
* 

__Prepare Google:__
* 

__Prepare Facebook:__
* 

__Prepare Python:__
* In a command line, run the following commands to install the required Python packages:
	* If you have no experience with pip, try following the process on this page to install and test pip: https://www.w3schools.com/python/python_pip.asp
	* `pip install fbchat`
		* There is an odd bug with fbchat. After running this line, you'll need to navigate to the `\_state.py` file and change line 190 to: `revision = 1`. For me (a Windows user), this file is in the directory `C:\Users\Daniel Goodman\AppData\Local\Programs\Python\Python38\Lib\site-packages\fbchat\_state.py`. If you are a Windows user, it will likely be in the same place, but replace "Daniel Goodman" with your username. If you are a Mac user, try to find your Python directory and navigate through `Python38\Lib\site-packages\fbchat`.
	* `pip install oauth2client`
	* `pip install gspread`
* Open and fill in the default CREDENTIALS.txt file with the proper information as follows:
	* RECEIVER-ID: The numerical Facebook ID of the account where you want to receive the messages. Find this by pasting the link to your profile into this website: https://lookup-id.com/
	* SENDER-EMAIL: The email address of your secondary Facebook account - the one you likely just made, which will send the messages.
	* SENDER-PASSWORD: The password of your secondary Facebook account.
	* INBOX-SHEET: The full link to the "SMS Received" Google sheet. It should look something like this, but with different characters between `/spreadsheets/d/` and `/edit#gid=0`: https://docs.google.com/spreadsheets/d/1txvx4UaZZjVflTgjnqAFjuN0ioMzguw_JdX0Yy49b1w/edit#gid=0
	* OUTBOX-SHEET: The full link to the (not yet implemented) "SMS Sent" Google sheet.
* Finally, run the program textsender.py. On Windows, you can do this by simply double-clicking on the program, or by opening up the command line in the directory with textsender.py and entering `python textsender.py`. On Mac, you can go into the proper directory in the terminal and enter `./textsender.py`.



Make sure to download IFTTT, go to Sync options, and turn on "Run Location, Android Battery, and WiFi connections faster"

Make sure to share the spreadsheet with your Google Sheets API account address (likely something ending with gserviceaccount.com, such as myuser@myproject.iam.gserviceaccount.com)

# Known bugs, limitations, and future additions
* __Bug:__ When keeping the program running while disconnected from the internet, there will be a long list of exceptions printed to the terminal when the code is stopped. This can be solved by manually stopping and starting the code every time you disconnect and reconnect, but there is currently no built-in way to avoid this.
* __Limitation:__ Due to the limitations of IFTTT, this will currently not work with MMS messages. This is most noticeable in cases such as group chats, where Messenger notifications may not properly come through.
	* Potential solutions: It is possible to make IFTTT run when a notification is received from a specific app (such as your Android messaging app), but in my tests this would only work for the first notification in a series - that is, it would properly notify me of a single text, but it would not notify me of any more until I unlocked my phone and dismissed that notification. This could still potentially work if there is a messaging app that sends new notifications for every message, but I was not able to find one. Note that when I tested this, I was not using the faster sync option, so this could be something to try as well.
* __Limitation:__ There's no way around the fact that the current set-up is extensive and somewhat time-consuming. I've tried to document it as best as possible, and I hope to automate more of the steps in the future, but for now there is quite an onus on the end user.
* __Future addition:__ There is currently no way to respond to the SMS messages in Messenger, but there is currently a workflow set up for this to be added in the future. As previously described, there is an IFTTT applet set up for reading from the outbox sheet and sending those messages. The `handle_outbox` function in textsender.py has yet to be implemented, but this sending functionality should work once it is. The main barrier is coming up with an intuitive and user-friendly way to specify which person to reply to, since the Messenger bot is used for all incoming and outgoing SMS messages.

# Works cited
**INCOMPLETE**

These are the sources used for all code that was copied and/or adapted. While some snippets were directly copied from external sources, the application-level structure and logic of this program is original.
https://gspread.readthedocs.io/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column
https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds

Note that many more sources were referenced for finding syntax for specific methods (such as the `readline` function), debugging, researching error messages, and troubleshooting IFTTT/other relevant software. 

# Acknowledgements
This repo started as a project for AMS 343: Privacy, Publicity, and the Text Message - a Princeton University undergraduate course taught by Professor Grant Wythoff. Thank you, Prof. Wythoff for your enthusiasm and support throughout the semester!