import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv  # take environment vars like API token from .env file
import asyncio

env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)

TOKEN = os.environ.get("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')  # print a message when the bot comes online

@client.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')  # let me know when the bot sees a message

async def send(message):
    await client.get_channel(1000612336593285174).send(message)


client.run(TOKEN)