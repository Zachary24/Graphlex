# Installation
* For Mac, Open Terminal, then run "cd 'Location of Graphlex'/Graphlex" next, run "pip install -r Requirements.txt"
* For Windows, Open CMD, then run "cd 'Location of Graphlex'/Graphlex" next, run "pip install -r Requirements.txt"

# Explanation
Graphlex requires packages, such as PlexAPI or Flask to run properly, thus, you must install them on your machine, if you don't Graphlex will throw out erros, such as "can't import flask as ..."

# Setting up/Connecting to Plex Account
* Go into metaGrabber.py, In there you'll see a few variables, baseurl, token, movies, shows, etc.
Baseurl should be the url you access plex on, I.E. The IP of the server:The port plex remotely runs on.
Plex tells how to get your token here https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

Movies & Shows should be the names of your libraries.

# Explanation
Instead of using your username and password to access your Plex account, Graphlex uses a very secure token instead, even though Graphlex has zero connection outside of your local network, more secure = better.

# How to Run/Launch Graphlex
* To start Graphlex go into Terminal(Mac), or CMD(Windows), and type "cd 'Location of Graphlex'/Graphlex/app.py"
The shell should return something like
Serving Flask app "app" (lazy loading)
Environment: production
WARNING: Do not use the development server in a production environment.
Use a production WSGI server instead.
Debug mode: off
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Open a browser, go to localhost:5000
* Graphlex should start running!
