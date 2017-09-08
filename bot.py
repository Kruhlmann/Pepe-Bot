import discord
import re
import urllib.request
import random

client = discord.Client()

def get_random_pepe_url():
	album_url = "http://imgur.com/a/U2dTR/layout/blog"

	# Check the URL is actually imgur:
	match = re.match("(https?)\:\/\/(www\.)?(?:m\.)?imgur\.com/(a|gallery)/([a-zA-Z0-9]+)(#[0-9]+)?", album_url)
	if not match:
		return "FeelsBadMan my pepe library is corrupted"

	try:
		response = urllib.request.urlopen(url=album_url)
		response_code = response.getcode()
	except Exception as e:
		response = False
		response_code = e.code 	

	if not response or response.getcode() != 200:
		return "FeelsBadMan error occurred"

	# Read in the images now so we can get stats and stuff:
	html = response.read().decode('utf-8')
	imageIDs = re.findall('.*?{"hash":"([a-zA-Z0-9]+)".*?"ext":"(\.[a-zA-Z0-9]+)".*?', html)
	id_ = random.choice(imageIDs)[0] + random.choice(imageIDs)[1]
	return "http://i.imgur.com/" + id_

@client.event
async def on_message(message):
	if message.content == "gib pepe pls":
		await client.send_message(message.channel, get_random_pepe_url())

@client.event
async def on_ready():
	print("Auth details:")
	print("\t" + client.user.name)
	print("\t" + client.user.id)

client.run("YOUR_TOKEN_HERE")
