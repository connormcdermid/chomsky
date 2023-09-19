import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv  # take environment vars like API token from .env file
import asyncio
import random
import time

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
    if message.content.startswith('noam, '):
        await message.channel.send("Acknowledged.")


@bot.slash_command(name="test", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534])
async def test(ctx):
    await ctx.respond("ACK")


@bot.slash_command(name="msguessr", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534])
async def msguessr(ctx):
    await ctx.respond(f"Acknowledged. Give me a second to prepare...")
    print("Command received. Indexing...")
    messages = await ctx.channel.history(limit=None).flatten()
    random_message = random.choice(messages)
    global last_random_message
    last_random_message = random_message
    print("done.")
    await ctx.send(f"Who sent this message?: {random_message.content}")


@bot.slash_command(name="answer", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534])
async def answer(ctx):
    await ctx.respond(last_random_message.author)


@bot.slash_command(name="version", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534])
async def answer(ctx):
    await ctx.respond("Noam Chompsky v0.2", ephemeral=True)


@bot.slash_command(name="timestamp", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534])
async def answer(ctx, relative, epoch):
   if relative:
       await ctx.respond(f"<t:{epoch}:R>")
   else:
       await ctx.respond(f"<t:{epoch}:F")


@bot.slash_command(name="poke", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534])
async def poke(ctx, userid):
    user = await bot.fetch_user(userid)
    print(userid)
    user = await bot.fetch_user(userid)
    await user.send(f"Ping! You're being poked!")
    await ctx.respond(f"The user was poked in DMs.", ephemeral=True)


@bot.slash_command(name="ping", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534], description="Returns latency time")
async def ping(ctx):
    await ctx.respond(f"Pong! Latency is {bot.latency}.")

@bot.slash_command(name="embed", guild_ids=[1000612336593285171, 697911717467783258, 1149480757472018534], description="Embed a Spotify song.")
async def embed(ctx, song_url):
    embed=discord.Embed(title="Test Embed", url=song_url, description="An embedded Spotify song", color=discord.Color.green())
    await ctx.send(embed)



bot.run(TOKEN)
