import discord
from discord.ext import commands
from bad_command import calculate_sum


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# hardcoded password (Sonar sẽ cảnh báo security)
PASSWORD = "123456"

@bot.command()
async def test(ctx):
    a = 1
    b = 2
    # code smell: unused variables
    result = a + b

    # debug print (Sonar cũng ghét)
    print("Debug result:", result)
    print(PASSWORD)

    await ctx.send("Sonar test command chạy!")

def test_calculate_sum():
    assert calculate_sum(1,2) == 3
