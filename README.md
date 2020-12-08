# Introduction and rationale
**INCOMPLETE**
As human communication has moved into the electronic age, there has been an influx of new ways to communicate. People have greatly differing preferences as to which of these platforms is easiest, from standard SMS messaging, to WhatsApp, to Facebook Messenger, and plenty more. In the pastThis particular repository serves to solve a very specific set of preferences and conditions - those who use Android phones for sending and receiving SMS messages, but would prefer to receive them on Facebook Messenger. 

# Set-up
**INCOMPLETE**
After running pip install fbchat, change line 190 in C:\Users\Daniel Goodman\AppData\Local\Programs\Python\Python38\Lib\site-packages\fbchat\_state.py to:
revision = 1

Make sure to download IFTTT, go to Sync options, and turn on "Run Location, Android Battery, and WiFi connections faster"

Make sure to share the spreadsheet with your Google Sheets API account address (likely something ending with gserviceaccount.com, such as myuser@myproject.iam.gserviceaccount.com)

# Known bugs, limitations, and future additions
* __Bug:__ When keeping the program running while disconnected from the internet, there will be a long list of exceptions printed to the terminal when the code is stopped. This can be solved by manually stopping and starting the code every time you disconnect and reconnect, but there is currently no built-in way to avoid this.
* __Limitation:__ Due to the limitations of IFTTT, this will currently not work with MMS messages. This is most noticeable in cases such as group chats, where Messenger notifications may not properly come through.
	* Potential solutions: It is possible to make IFTTT run when a notification is received from a specific app (such as your Android messaging app), but in my tests this would only work for the first notification in a series - that is, it would properly notify me of a single text, but it would not notify me of any more until I unlocked my phone and dismissed that notification. This could still potentially work if there is a messaging app that sends new notifications for every message, but I was not able to find one. Note that when I tested this, I was not using the faster sync option, so this could be something to try as well.
* __Future addition:__ There is currently no way to respond to the SMS messages in Messenger, but there is currently a workflow set up for this to be added in the future. As previously described, there is an IFTTT applet set up for reading from the outbox sheet and sending those messages. The `handle_outbox` function in textsender.py has yet to be implemented, but this sending functionality should work once it is. The main barrier is coming up with an intuitive and user-friendly way to specify which person to reply to, since the Messenger bot is used for all incoming and outgoing SMS messages.

# Works cited
**INCOMPLETE**
https://gspread.readthedocs.io/en/latest/user-guide.html#getting-all-values-from-a-row-or-a-column
https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds