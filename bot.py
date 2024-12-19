import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Set up bot with intents and prefix
intents = discord.Intents.default()
intents.messages = True  # Customize intents if needed
bot = commands.Bot(command_prefix=commands.when_mentioned,
              intents=intents,
              help_command=None)

# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f"Bot logged in as {bot.user}")
    await load_cogs()  # Call the load_cogs function

# Function: Automatically load all Cogs
async def load_cogs():
    for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
                print("----------------------------------")
                print(f"✔️ Loaded extension '{extension}'")
                print("----------------------------------")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"❌ Failed to load extension {extension}\n{exception}\n{e}")

# Run the bot
bot.run(TOKEN)