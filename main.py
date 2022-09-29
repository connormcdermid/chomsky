import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv  # take environment vars like API token from .env file
import asyncio
import random

env_path = join(dirname(__file__), '.env')
load_dotenv(env_path)

TOKEN = os.environ.get("TOKEN")
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

last_random_message = ""


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')  # print a message when the bot comes online


@bot.event
async def on_message(message):
    if message.content.startswith('c!'):
        await message.channel.send("Acknowledged.")


async def send(message):
    await bot.get_channel(1000612336593285174).send(message)


@bot.slash_command(name="test", guild_ids=[1000612336593285171])
async def test(ctx):
    await ctx.respond("ACK")


@bot.slash_command(name="msguessr", guild_ids=[1000612336593285171])
async def msguessr(ctx):
    await ctx.respond(f"Acknowledged. Give me a second to prepare...")
    print("Command received. Indexing...")
    messages = await ctx.channel.history(limit=None).flatten()
    random_message = random.choice(messages)
    global last_random_message
    last_random_message = random_message
    print("done.")
    await ctx.send(f"Who sent this message?: {random_message.content}")


@bot.slash_command(name="answer", guild_ids=[1000612336593285171])
async def answer(ctx):
    await ctx.respond(last_random_message.author)

bot.run(TOKEN)
