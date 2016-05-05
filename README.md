# JackBox Bot
This project was thrown together in about 3 hours using a mix of content I've
found online and a little bit of socket code I made myself. This code should
NOT be used as a reference for how to properly use sockets, nor how to make a
proper Twitch Chat Bot, primarily because of how I go about using threads. I
personally haven't ran into any issues, but I can't say for sure how
thread-safe this code actually is, so be careful and use at your own risk.


## DEPENDENCIES/REQUIREMENTS
- Python 2.7.X
- Tkinter

## Usage
1. Fill out the cfg.py file with your info(Using a second account is recommeneded) 
2. Start main.py
3. Wait for it to load. If it loaded successfully loged in to the chat you will see **"JackBox Bot has successfully loaded!"** and a windows will open.
4. Tell your chat to type **"!play"** to join the que for the game(A reminder is sent out every 4 minutes).
5. When you are ready to send out the room code make sure its blocked so people who didin't que don't see it and then press "Setup Next Player". 
 **>>NOTE<<** Its sends out the code one at a time so you will need to press it for each person in the que.
6. ???
7. Profit.

## Other stuff
Anyways, this project was intended as a way to guarantee people watching a
Twitch stream, where the game is a Jackbox game, a chance to play. How it
works is, while the bot is running, people in the Twitch chat can say "!play"
to be added to the queue. When the streamer wants to start a new game, they'll
have to make sure the people watching the stream can't see the code. The
streamer then joins the room (since the first person to join a room becomes
the host) and then types the room code into the textbox in this application.
Pressing the "Setup Next Player" button will remove the person at the front of
the line and will get the room code whispered to them.

## Notes

 - This hasn't been tested on any other OS besides Windows.
 - This project cannot remove people from the queue (yet).