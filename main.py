import discord
import os
import random
import time
import asyncio
import requests 
import json
from keep_alive import keep_alive
from replit import db
from discord.ext import commands

client = commands.Bot(command_prefix = ['dino ', '!'])

night = ['night', 'Night']
nightreplies = ['Goodnight sweetheart']
morning = ['morning', 'Morning']
morningreplies = ['Good morning master']
counting = ['counting']

ppreplies = ['sheesh you packin', 'you\'re definitely a virgin', '🍤', 'omg daddy 🥵', '😏', 'looks familiar', '\u200B', '\u200B', '\u200B', '\u200B', '\u200B', '\u200B', '\u200B']

global chanel

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

i = 25

author = ''

tammy = ['tammy']
kyan = ['pepperz']

hugs = ['https://media1.tenor.com/images/b7487d45af7950bfb3f7027c93aa49b1/tenor.gif', 'https://media1.tenor.com/images/7e30687977c5db417e8424979c0dfa99/tenor.gif', 'https://media1.tenor.com/images/6db54c4d6dad5f1f2863d878cfb2d8df/tenor.gif?', 'https://media1.tenor.com/images/552c49f523d61c01da04bb1128b42cbf/tenor.gif', 'https://cdn.discordapp.com/attachments/466743181434683392/825902901918433310/6be2cff474d08d68b39deb5c101d907b.gif']

kisses = ['https://media1.tenor.com/images/626cb1e13142bce7f228ab8e30e2519c/tenor.gif', 'https://media1.tenor.com/images/621ceac89636fc46ecaf81824f9fee0e/tenor.gif', 'https://media1.tenor.com/images/e00f3104927ae27d7d6a32393d163176/tenor.gif', 'https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/tenor.gif']

slaps = ['https://media1.tenor.com/images/af36628688f5f50f297c5e4bce61a35c/tenor.gif', 'https://media1.tenor.com/images/7437caf9fb0bea289a5bb163b90163c7/tenor.gif', 'https://media1.tenor.com/images/b7a844cc66ca1c6a4f06c266646d070f/tenor.gif', 'https://media1.tenor.com/images/d14969a21a96ec46f61770c50fccf24f/tenor.gif', 'https://media1.tenor.com/images/528ff731635b64037fab0ba6b76d8830/tenor.gif?itemid=17078255', 'https://i.giphy.com/media/Zau0yrl17uzdK/giphy', 'https://cdn.discordapp.com/attachments/466743181434683392/825903139793534976/original_12.gif', 'https://media1.tenor.com/images/4fcc4d199951cebdcf475e9f89336c73/tenor.gif']

grooms = ['https://media1.tenor.com/images/d3313eccf8c32223884e13dca250f6df/tenor.gif', 'https://media1.tenor.com/images/6d2f4893ba147ef0abcb8dba66627726/tenor.gif', 'https://media1.tenor.com/images/42b4296dd21035e8bd71a0c579c47fbb/tenor.gif', 'https://media1.tenor.com/images/f593c99d27527b690f97548bf5acdfe2/tenor.gif', 'https://media1.tenor.com/images/e5d4995a5177417243be9acfe82e6c77/tenor.gif', 'https://media1.tenor.com/images/938417ce2a8d57474aa5b8a589996969/tenor.gif', 'https://media1.tenor.com/images/7b1af84daaca132e33bffecf64d898f4/tenor.gif']

def str_append(s, n):
  output = ''
  i = 0
  while i < n:
    output += s
    i = i + 1
  return output

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game(name="in dinosaur universe"))

@client.event
async def on_message(message):

  for word in night:
    if word in message.content:
      if message.author == client.user:
        return
      else:
        await message.channel.send(random.choice(nightreplies) + " {0.author.mention}".format(message))
        #embed = discord.Embed(title='Goodnight sweetheart {}'.format(message.author.name), color=0x7de3e1)
        #await message.channel.send(embed=embed)
      
  for word in morning:
    if word in message.content:
      if message.author == client.user:
        return
      else:
        await message.channel.send(random.choice(morningreplies) + " {0.author.mention}".format(message))
        #embed = discord.Embed(title='Good morning master {}'.format(message.author.name), color=0x7de3e1)
        #await message.channel.send(embed=embed)

  for word in kyan:
    if word in message.content:
      if message.author == client.user:
        return
      else:
        reactions = ['🌶']
        for emoji in reactions: 
          await message.add_reaction(emoji)
          
  await client.process_commands(message)

@client.command()
async def counting(ctx, count: str):
  if count == 'true':
    counting = True
    await ctx.send("Auto counting is Enabled")
  else:
    counting = False
    await ctx.send("Auto counting is Disabled")

@client.command()
async def channel(ctx, chan: str):
  chanel = chan
  await ctx.send("channel is set to " + chanel)

@client.command()
async def quote(ctx, member : discord.Member):
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q']
  embed = discord.Embed(title="{}'s words of wisdom".format(member.name), description="\"{}\" - *{}*".format(quote, member.name), color=0x7de3e1)
  embed.set_author(name=member.name, icon_url=member.avatar_url)
  await ctx.send(embed=embed)

@client.command()
async def purge(ctx, amount: int):
  if ctx.author.guild_permissions.administrator:
    await ctx.channel.purge(limit=amount+1)
    await ctx.send("I deleted {} messages for {}".format(amount, ctx.author.mention))
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)
  else:
    await ctx.send("you can't do that")
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=1)

@client.command(name='join')
async def join(ctx):
  if not ctx.message.author.voice:
    await ctx.send("You are not connected to a voice channel")
    return
    
  else:
    channel = ctx.message.author.voice.channel
    await channel.connect()
    await ctx.send("whats up?(≧▽≦)")

@client.command(name='leave')
async def leave(ctx):
  voice_client = ctx.message.guild.voice_client
  await voice_client.disconnect()
  await ctx.send("bye (´._.`)")

@client.command()
async def hug(ctx,member : discord.Member):
  embed = discord.Embed(description="**{}** hugs **{}**".format(ctx.author.name, member.name), color=0x7de3e1)
  randomlink = random.choice(hugs)
  embed.set_image(url = randomlink)
  await ctx.send(embed=embed)

@client.command()
async def kiss(ctx,member : discord.Member):
  embed = discord.Embed(description="**{}** kisses **{}**".format(ctx.author.name, member.name), color=0x7de3e1)
  randomlink = random.choice(kisses)
  embed.set_image(url = randomlink)
  await ctx.send(embed=embed)

@client.command()
async def slap(ctx,member : discord.Member):
  embed = discord.Embed(description="**{}** slaps **{}**".format(ctx.author.name, member.name), color=0x7de3e1)
  randomlink = random.choice(slaps)
  embed.set_image(url = randomlink)
  await ctx.send(embed=embed)

@client.command()
async def groom(ctx,member : discord.Member):
  embed = discord.Embed(description="**{}** grooms **{}**".format(ctx.author.name, member.name), color=0x7de3e1)
  randomlink = random.choice(grooms)
  embed.set_image(url = randomlink)
  await ctx.send(embed=embed)

@client.command()
async def pp(ctx,member : discord.Member):
  pp = random.randint(0,20)
  pp2 = str_append('=', pp)
  embed = discord.Embed(description="{}'s pp".format(member.name), color=0x7de3e1)
  embed.add_field(name="{}".format(random.choice(ppreplies)), value="8{}D".format(pp2))
  await ctx.send(embed=embed)

@client.command()
async def whois(ctx,member : discord.Member):
  created = member.created_at.strftime("%b %d, %Y")
  joined = member.joined_at.strftime("%b %d %Y")
  embed = discord.Embed(title="ID: <{}>".format(member.id), color=0x7de3e1)
  embed.add_field(name="Created:", value=created, inline=True)
  embed.add_field(name="Joined:", value=joined, inline=True)
  embed.set_author(name=member.name, icon_url=member.avatar_url)
  embed.set_image(url = member.avatar_url)
  await ctx.send(embed=embed)

@client.command()
async def commands(ctx):
  embed = discord.Embed(title="Commands", description="prefixes: 'ivy or !'", color=0x7de3e1)
  embed.add_field(name="!join/leave", value="joins/leaves your vc", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="!news <topic>", value="get the latest news", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="!hug <member>", value="hug somone!", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="!kiss <member>", value="kiss someone!", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="!slap <member>", value="slap somone!", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="!groom <member>", value="groom someone!", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="!whois <member>", value="about member", inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="!purge <amount>", value="mass delete messages", inline=True)
  await ctx.send(embed=embed)

keep_alive()
client.run(os.environ['TOKEN'])
