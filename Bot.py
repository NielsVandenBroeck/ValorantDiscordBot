import discord
import RequestHandler

intents = discord.Intents.default()
intents.message_content = True

async def send_message(message):
    content = str(message.content)
    if str(message.channel) == "shop":
        response = RequestHandler.handle_shop(content)
    else:
        response = RequestHandler.handle_request(content)
    await message.reply(response)

def run_discord_bot():
    TOKEN = open('Token.txt', 'r').read()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running.')

    @client.event
    async def on_message(message):
        #skip messages from bot itself
        if message.author == client.user:
            return
        await send_message(message)

    client.run(TOKEN)