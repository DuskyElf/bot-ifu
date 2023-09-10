import discord
from os import getenv
from dotenv import load_dotenv

TOKEN_ENV_VAR = "BOT_TOKEN"

def main():
    load_dotenv()

    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    __token = getenv(TOKEN_ENV_VAR)
    assert __token is not None
    client.run(__token)

if __name__ == "__main__":
    main()
