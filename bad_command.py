import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents  )

# lấy token từ environment variable (an toàn hơn)
TOKEN = os.getenv("DISCORD_TOKEN")


@bot.command()
async def good(ctx, message: str = "Hello"):
    """
    Simple command to demonstrate clean code.
    """

    result = calculate_sum(1, 2)

    await ctx.send(f"{message}! Result = {result}")


def calculate_sum(x: int, y: int) -> int:
    """
    Return the sum of two numbers.
    """
    return x + y