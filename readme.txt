Hi,

This project was thrown together in about 3 hours using a mix of content I've
found online and a little bit of socket code I made myself. This code should
NOT be used as a reference for how to properly use sockets, nor how to make a
proper Twitch Chat Bot, primarily because of how I go about using threads. I
personally haven't ran into any issues, but I can't say for sure how
thread-safe this code actually is, so be careful and use at your own risk.

Anyways, this project was intended as a way to guarantee people watching a
Twitch stream, where the game is a Jackbox game, a chance to play. How it
works is, while the bot is running, people in the Twitch chat can say "!play"
to be added to the queue. When the streamer wants to start a new game, they'll
have to make sure the people watching the stream can't see the room code. The
streamer then joins the room (since the first person to join a room becomes
the host) and then types the room code into the textbox in this application.
Pressing the "Setup Next Player" button will have the person at the front of
the line removed and will get the room code whispered to them.

Dylan J. Raub


# NOTES

 - I used python 2.7.8 for this project.
 - This hasn't been tested on any other OS besides Windows.
 - This project uses Tkinter for it's GUI.
 - This project cannot remove people from the queue (yet).