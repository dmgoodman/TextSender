# Introduction and rationale

As human communication has moved into the electronic age, there has been an influx of new ways to communicate. People have greatly differing preferences as to which of these platforms is easiest, from standard SMS messaging, to WhatsApp, to Facebook Messenger, and plenty more. With a motivation to get closer to the simpler times of letter writing when there were significantly less platforms to navigate, this project serves to condense two frequently used messaging platforms into one. This particular repository exists to help people with a specific set of conditions and preferences - those who use Android phones for sending and receiving SMS messages, but would prefer to receive them on Facebook Messenger. Instead of introducing yet another way to communicate with people, the goal of this project is to allow users to use a pre-existing platform to address multiple forms of communication.

In working on this project, I've also become acutely aware of the various incompatibilities and difficulties that occur when combining messaging applications in this way. Long-term, I would love to see this expanded to connect as many edges as possible (such as receiving Messenger messages as texts, or receiving Google Hangouts messages on WhatsApp). This project started as a way to help myself and people like me - I'm almost always on my computer, but I tend to check my phone only a couple times a day, which makes me quite bad at texting. However, I realize that there are other people who would like to condense their messaging platforms differently. In the far future, I hope people have the option to use whichever platform they prefer for all their messaging needs.

# Set-up
## You will need
* An Android device that receives SMS messages
* A Google account (https://accounts.google.com/)
* The IFTTT app installed on your Android device (https://play.google.com/store/apps/details?id=com.ifttt.ifttt)
* A Facebook account for use on Facebook Messenger (https://messenger.com/)
* Python 3.8
	* https://www.python.org/downloads/, scroll down to "Looking for a specific release?"
	* 3.8.6 is guaranteed to work. Future or previous versions may work as well, but are not guaranteed.
* __Optional, but preferred:__ A second Facebook account. Facebook is known to lock accounts when there is suspicious activity (read: a chatbot sending messages on your behalf). To avoid this, it's best to have a second account.

## Steps
__Prepare Google:__
* We will be following select steps from this tutorial, which you can keep open as a reference: https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/
* Note: If you want to be extra careful, you can create a separate Google account just for this project; that way, you can guarantee you won't accidentally overwrite any of your own Google Drive files. You can create a new Google account here: https://accounts.google.com/
* Once you're logged into the Google account you wish to use, open the Google Developer's Console: https://console.developers.google.com/
* If you have not used the platform before, agree to the Terms of Service and continue.
* Click "CREATE PROJECT".
* Name it whatever you'd like. I'd recommend something like "SMS-to-Messenger" or "Text Sender".
* Keep the Location as the default and click "CREATE".
* Next, click "ENABLE APIS AND SERVICES", search for "sheets" and select "Google Sheets API".
* Click "ENABLE"!
* We're almost there! Click "CREATE CREDENTIALS".
* Choose "Google Sheets API", then "Other non-UI (e.g. cron job, daemon)". Finally, choose "Application data", followed by "No, I'm not using them".
* Now click "What credentials do I need?"
* Choose whatever you'd like for "Service account name" and "Service account ID"; set the Role to "Owner" under the "Project" dropdown.
* Keep "JSON" selected, then click "Continue".
* Now, a file should be downloaded to your computer. Move the file to the same directory as this repository, and rename it "CLIENT-SECRET.json".
* In the same tab, you should see a long Email shown under the Service Accounts section (ending with iam.gserviceaccount.com). Copy that and hold onto it.
* Your credentials are complete! Now let's make a new Google Sheet. Open up Google Drive in the same Google account: https://drive.google.com/
* Choose "New", then "Google Sheets".
* Name this new Sheet "SMS received"
* Now click the "Share" button in the top right, and share this spreadsheet with your service account email. You may get an email saying there was an issue sharing it, but this can be ignored.
* Great job, let's move on!

__Prepare IFTTT:__
* Open up the IFTTT app, and log in/create an account with the same Google account you've been using.
* Before we begin, there's important setting you'll need to change to avoid a bug later on.
	* Tap your email address in the top right corner.
	* Tap Sync options.
	* Turn on "Run Location, Android Battery, and WiFi connections faster". Note: this will put a persistent notification on your phone telling you that IFTTT is running in the background.
	* You can keep "Use cellular data" on at your own risk - this applet should not be using much cellular data.
* Next, we'll need to create an applet that adds a row to a given Google Sheet every time you receive an SMS.
	* You can do this on the app.
	* First, tap Create, then tap If This.
	* Search for "SMS" and choose "Android SMS".
	* Choose "Any new SMS received".
	* Tap "Then That".
	* Search for "sheets" and choose "Google Sheets".
	* Choose "Add row to spreadsheet".
	* Set the "Formatted row" field to say: "{{OccurredAt}}///{{FromNumber}}///{{ContactName}}///{{Text}}".
		* Note: We are using "///" in place of "|||"; this keeps all the data in a single cell.
	* Make sure the Spreadsheet name is "SMS received" and delete everything from the Drive folder path field.
	* Press continue again.
	* Press Finish.
* __Optional:__ You can also create a second applet which will send a text when a cell in a different spreadsheet is updated. This feature has not been implemented into the code yet, but you can get a head-start now for when it eventually is. If you do not follow these steps, you will still be able to receive SMS messages on Messenger.
	* **INCOMPLETE** - These steps are not added yet.

__Prepare Facebook:__
* __Optional:__ Open an Incognito window in your browser to do this, so you don't have to switch between Facebook accounts.
* If you have created a second account, fbchat will not work until you've gone through the entire account creation process. When you log into your account, Facebook may ask you to fill in some details about yourself - it may take a few log-ins to skip this step. There is not a science to this, but if the final step is not working, I recommend troubleshooting by logging in and out of your new account a couple times until you're brought directly to your feed instead of some intermediate step.

__Prepare Python:__
* In a command line, run the following commands to install the required Python packages:
	* If you have no experience with pip, try following the process on this page to install and test pip: https://www.w3schools.com/python/python_pip.asp
	* `pip install fbchat`
		* There is an odd bug with fbchat. After running this line, you'll need to navigate to the `\_state.py` file and change line 190 to: `revision = 1`. For me (a Windows user), this file is in the directory `C:\Users\Daniel Goodman\AppData\Local\Programs\Python\Python38\Lib\site-packages\fbchat\_state.py`. If you are a Windows user, it will likely be in the same place, but replace "Daniel Goodman" with your username. If you are a Mac user, try to find your Python directory and navigate through `Python38\Lib\site-packages\fbchat`.
	* `pip install oauth2client`
	* `pip install gspread`
* Open and fill in the default CREDENTIALS.txt file with the proper information as follows (make sure to keep a single space after each colon):
	* RECEIVER-ID: The numerical Facebook ID of the account where you want to receive the messages. Find this by pasting the link to your profile into this website: https://lookup-id.com/
	* SENDER-EMAIL: The email address of your secondary Facebook account - the one you likely just made, which will send the messages.
	* SENDER-PASSWORD: The password of your secondary Facebook account.
	* INBOX-SHEET: The full link to the "SMS Received" Google sheet. It should look something like this, but with different characters between `/spreadsheets/d/` and `/edit#gid=0`: https://docs.google.com/spreadsheets/d/1txvx4UaZZjVflTgjnqAFjuN0ioMzguw_JdX0Yy49b1w/edit#gid=0
	* OUTBOX-SHEET: The full link to the (not yet implemented) "SMS Sent" Google sheet.
* Finally, run the program textsender.py. On Windows, you can do this by simply double-clicking on the program, or by opening up the command line in the directory with textsender.py and entering `python textsender.py`. On Mac, you can go into the proper directory in the terminal and enter `./textsender.py`.
* Amazing job! The software is now complete, and you can keep it running in the background. You'll get a message from your secondary Facebook account any time you get a new SMS!

# Known bugs, limitations, and future additions
* __Bug:__ When keeping the program running while disconnected from the internet, there will be a long list of exceptions printed to the terminal when the code is stopped. This can be solved by manually stopping and starting the code every time you disconnect and reconnect, but there is currently no built-in way to avoid this.
* __Limitation:__ Due to the limitations of IFTTT, this will currently not work with MMS messages. This is most noticeable in cases such as group chats or when pictures are received, where Messenger notifications may not properly come through.
	* Potential solutions: It is possible to make IFTTT run when a notification is received from a specific app (such as your Android messaging app), but in my tests this would only work for the first notification in a series - that is, it would properly notify me of a single text, but it would not notify me of any more until I unlocked my phone and dismissed that notification. This could still potentially work if there is a messaging app that sends new notifications for every message, but I was not able to find one. Note that when I tested this, I was not using the faster sync option, so this could be something to try as well.
* __Limitation:__ There's no way around the fact that the current set-up is extensive and somewhat time-consuming. I've tried to document it as best as possible, and I hope to automate more of the steps in the future, but for now there is quite an onus on the end user.
* __Limitation:__ The platform is not instant - in my testing I've always received messages in under a minute, but over a few seconds. Part of this lag is intentional so as not to overload the Google Sheets client (it only checks the spreadsheet every 5 seconds), but some of the lag is there because of the complexity of the process.
* __Future addition:__ There is currently no way to respond to the SMS messages in Messenger, but there is currently a workflow set up for this to be added in the future. As previously described, there is an IFTTT applet set up for reading from the outbox sheet and sending those messages. The `handle_outbox` function in textsender.py has yet to be implemented, but this sending functionality should work once it is. The main barrier is coming up with an intuitive and user-friendly way to specify which person to reply to, since the Messenger bot is used for all incoming and outgoing SMS messages.

# Works cited
**INCOMPLETE**

These are the sources used for all code that was copied and/or adapted. While some snippets were directly copied from external sources, the application-level structure and logic of this program is original.
https://www.geeksforgeeks.org/send-message-to-fb-friend-using-python/ - basis for `send()` function
https://gspread.readthedocs.io/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column
https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds
https://www.analyticsvidhya.com/blog/2020/07/read-and-update-google-spreadsheets-with-python/ - basis for `main()` function

Note that many more sources were referenced for finding syntax for specific functions or single lines of code (such as the `readline` and `open_by_url` functions), reading documentation, debugging, researching error messages, and troubleshooting IFTTT/other relevant software. These sources (on the order of hundreds) certainly deserve a mention, but I believe that the knowledge gained from them has been applied in such a way that explicit citations would be too verbose.

# Acknowledgements
This repo started as a project for AMS 343: Privacy, Publicity, and the Text Message - a Princeton University undergraduate course taught by Professor Grant Wythoff. Thank you, Prof. Wythoff for your enthusiasm and support throughout the semester!