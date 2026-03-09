import discord
from discord.ext import commands
from bad_command import calculate_sum
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# hardcoded password (Sonar sẽ cảnh báo security)
PASSWORD = "123456"

@bot.command()
async def test(ctx):
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10

    # code smell: unused variables
    result = a + b

    # debug print (Sonar cũng ghét)
    print("Debug result:", result)
    print(PASSWORD)

    await ctx.send("Sonar test command chạy!")

def test_calculate_sum():
    assert calculate_sum(1,2) == 3

# duplicate function để tạo code smell
def duplicate():
    x = 1
    y = 2
    print(x + y)

def duplicate():
    x = 1
    y = 2
    print(x + y)
