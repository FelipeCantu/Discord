import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='!')

TOKEN = ''


@client.event
async def on_ready():

    print('Bot Ready')


@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')


@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')


@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')


@client.command(aliases=['meeseeks'])
async def _8ball(ctx, *, question):
    responses = ["I'm sorry, but it doesn't work like that. I'm Mr. Meeseeks. I have to fulfill my purpose so I can go away. Look at me.",
                 "Can do! I'm Mr. Meeseeks! Is he keeping his shoulders squared?",
                 "Would you just relax, All we got to do is find the treasure room, okay? It's nice and simple. You know, I'm sorry everything's going so smoothly and adventurously.",
                 " Okay, you got to just choke up on the club!",
                 " Uhh... Hey, you mind if we get back to the task at hand? Meeseeks don't usually have to exist this long. It's getting weird.",
                "We all want to die! We're Meeseeks! Why did you even rope me into this?",
                "I'm Mr. Meeseeks. Look at me. The only thing that's clear is that choking up is the one true solution.",
                "Your failures are your own, old man. I'm Mr. Meeseeks! Look at me. I say follow-through! Who's with me?! Follow-through!",
                " I'm Mr. Meeseeks! Look at me!",
                "Everybody sto-o-o-p! Look at me! My brothers, nothing will be accomplished by shedding Meeseeks blood. None of us can die until our job is done.",
                "Excuse me. I'm a bit of a stickler Meeseeks. What about your short game?",
                 ]
    await ctx.send(f'Question: {question}\nMr.Meeseeks Answer is: {random.choice(responses)}')
                

@client.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


client.run(TOKEN)
