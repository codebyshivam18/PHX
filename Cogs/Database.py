import discord
from discord.ext import commands
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Setup
MONGO_URL = os.getenv("MONGO_URL")  # MongoDB URL from .env
cluster = MongoClient(MONGO_URL)

class Database(commands.Cog, name="Database"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Hybrid command to insert data into a MongoDB collection
    @commands.hybrid_command(name="add_data", description="Add data to a MongoDB database.")
    @commands.has_permissions(administrator=True)
    async def add_data(self, ctx, db_name: str, collection_name: str, key: str, value: str):
        """
        Command to create a database, collection, and insert data.
        Usage: /add_data <db_name> <collection_name> <key> <value>
        """
        # Create database and collection
        db = cluster[db_name]
        collection = db[collection_name]

        # Insert data
        data = {key: value}
        collection.insert_one(data)

        await ctx.send(f"✅ Data inserted into `{db_name}.{collection_name}`\n**Data:** `{data}`")

async def setup(bot):
    await bot.add_cog(Database(bot))