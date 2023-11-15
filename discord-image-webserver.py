import discord
import cherrypy
import threading
import requests
import io

# Configure these
discordToken = "Your bot token here"
discordChannelID = 1234567890111213141
defaultImageURL = "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
imageData = "silly place holder :) changing this does nothing"
htmlPage = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="30">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body, html {
  background-color: black;
  height: 100%;
  margin: 0;
}

.bg {
  /* The image used */
  background-image: url("embedImage");

  /* Full height */
  height: 100%; 

  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: contain;
}
</style>
</head>
<body>

<div class="bg"></div>

</body>
</html>
"""

def saveImage(link):
    global imageData
    r = requests.get(link)
    imageData = r.content

def loadImage():
    global imageData
    return imageData

class discordBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.channel.id == discordChannelID:
            if len(message.attachments) == 1:
                saveImage(message.attachments[0].url)
                print(defaultImageURL)
                await message.channel.send("<@" + str(message.author.id) + ">: Image displayed")
            else:
                await message.channel.send("<@" + str(message.author.id) + ">: Attachment error")

class webServer(object):
    @cherrypy.expose
    def index(self):
        return htmlPage
    @cherrypy.expose
    def embedImage(self):
        cherrypy.response.headers['Content-Type'] = "image/png"
        buffer = io.BytesIO()
        buffer.write(loadImage())
        return buffer.getvalue()

def dis():
    saveImage(imageURL)
    intents = discord.Intents.default()
    intents.message_content = True
    client = discordBot(intents=intents)
    client.run(discordToken)

def web():
    cherrypy.config.update({'server.socket_port': 80})
    cherrypy.config.update({'server.socket_host': '0.0.0.0'} ) 
    cherrypy.quickstart(webServer())

if __name__ == "__main__":
    t1 = threading.Thread(target=dis)
    t2 = threading.Thread(target=web)
    t2.start()
    t1.start()
