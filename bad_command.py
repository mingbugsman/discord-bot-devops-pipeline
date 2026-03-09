import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

# hardcoded token (security issue)
TOKEN = "1234567890abcdef"

# unused variables
a = 1
b = 2
c = 3
d = 4
e = 5


@bot.command()
async def bad(ctx, user_input=None):

    # duplicated code
    x = 1
    y = 2
    print(x+y)

    x = 1
    y = 2
    print(x+y)

    # command injection risk
    if user_input:
        os.system(user_input)

    # pointless loop
    for i in range(0,1000):
        pass

    # debug print
    print("this is debug message")

    await ctx.send("Bad command executed")

# extremely complex function
def terrible_function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):

    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            if g:
                                if h:
                                    if i:
                                        if j:
                                            print("too deep")