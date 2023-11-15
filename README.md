# Discord Image Webserver
This single Python file takes the most recent image (or GIF) attachment sent in a Discord channel and hosts it on a HTTP web server.
**NOTE: This is not a secure or good implementation. This was rushed in an hour or two for personal use for myself and a few friends on closed, trusted networks. It's bad practice to hardcode any API token in code, don't try this at home.**
## How to use
**Requirements:** Python 3.8, the `requests`, `discord.py` and `cherrypy` libraries, and a Discord bot user that has access to the channel you want to monitor.
**Instructions:** Edit the python file and change the variables at the top to your Discord bot user token and the channel ID variable to the ID of the channel you want to monitor. Then run the file. Going to that device's IP address on HTTP (port 80) opens the main page which has the last image of that channel centered on a black background. If you want just the raw image itself, go to the `/embedImage` page on the web server.
> I spent one thousand times longer typing the readme for this repo than I did considering the security of this webserver. Please don't publicly face this web server. I will cry.
