import discord 
from discord.ext import commands 

client = commands.Bot(command_prefix='!')

TOKEN = 'NzU4NDk2NTUzMTg2NDkyNDE2.X2vy9g.gBvDj-56lYbNrcWgBu5mqJo-pw0'

@client.event
async def on_ready():

    print('Bot Ready')


@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')


client.run(TOKEN)