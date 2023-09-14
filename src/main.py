import discord
from os import getenv
from dotenv import load_dotenv

BOT_PREFIX = "--"
TOKEN_ENV_VAR = "BOT_TOKEN"

def main():
    load_dotenv()

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    intents.message_content = True

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message: discord.Message):
        if message.author == client.user:
            return

        if message.content.startswith(BOT_PREFIX + "ping"):
            pong_embed = discord.Embed(
                title = "Pong!",
                description = "I'm alive"
            )
            await message.channel.send(embed=pong_embed)

    __token = getenv(TOKEN_ENV_VAR)
    assert __token is not None
    client.run(__token)

if __name__ == "__main__":
    main()
