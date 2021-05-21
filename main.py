import datetime
import discord
from discord.ext import commands
import array as arr

# create bot instance
client = commands.Bot(command_prefix='!')
client.message_counter = 0
firstWednesdayCount = 63

userRambo = 3
userKoth = 1
userJan = 0
userNano = 2
userJord = 0
userIan = 0

# bunScore = [f'Rambo: {userRambo}', f'Koth: {userKoth}', f'Tenbear: {userJan}', f'Nano: {userNano}', f'Jord: {userJord}',
#            f'DocBaker: {userIan}']

bunTest = [
    {"userName": 'Rambo', "score": {userRambo}}, {"userName": 'Koth', "score": {userKoth}},
    {"userName": 'Nano', "score": {userNano}}
]

# bunWeepers = ['Ramboknife#4029', 'Tenbear', 'DocBaker', 'Nanodecade', 'Kothkane#3974']


ramboScore = 22
kothScore = 5
nanoScore = 66
docScore = 53
tenScore = 1


# things to look in to adding: leaderboard, wednesday specific counters, and and overall counter.

# add event
@client.event
async def on_ready():
    print('Bun-Bot is ready.')


@client.event
async def on_reaction_add(reaction, user):
    # Arcade: '<:butwhy:719983036346663014>'
    if str(reaction) == '<:butwhy:719983036346663014>':
        print('Praise be to Bun!')
        print(reaction)
        print(user)
        # if user == 'Ramboknife#4029':
        # userRambo + 1
        # implement the message with the reaction stuff
        tears = arr.array('i', [9, 24, 49, 74, 99, 149, 199, 249, 299])
        if client.message_counter in tears:
            print('DING!')
            # Arcade: 114118637304020996
            channel = client.get_channel(114118637304020996)  # get channel from id
            embed = discord.Embed(title="Bun accepts yours tears, child.",
                                  description=f"{user} has given thanks to Bun! \nIn doing so, The Arcade has donated {client.message_counter + 1} buckets of tears!",
                                  color=0xb1f1c0)
            embed.set_footer(text="May your hands always be warm.")
            # await channel.send('message here')  # send message
            await channel.send(embed=embed)
            # call the message
        client.message_counter += 1
        # add this to the counter
    else:
        print('NO!')
        print(reaction)
        print(user)


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.event
async def on_message(message):
    user = message.author
    tears = arr.array('i', [9, 24, 49, 74, 99, 149, 199, 249, 299])
    # Arcade: butwhy
    if 'butwhy' in message.content:
        if client.message_counter in tears:
            embed = discord.Embed(title="Bun accepts yours tears, child.",
                                  description=f"{user} has given thanks to Bun! \nIn doing so, The Arcade has donated {client.message_counter + 1} buckets of tears!",
                                  color=0xb1f1c0)
            embed.set_footer(text="May your hands always be warm.")
            await message.channel.send(embed=embed)
        client.message_counter += 1
    await client.process_commands(message)


@client.command()
async def tears(ctx):
    embed = discord.Embed(title="Bun tear counter",
                          description="The Arcade has donated {} times to the pool of tears.".format(
                              ctx.bot.message_counter),
                          color=0xefe0b4)
    embed.set_thumbnail(
        url="https://pbs.twimg.com/profile_images/1192320244985061376/n7lxN_so_400x400.jpg")
    # embed.add_field(name="Conclusion", value="Test", inline=True)
    embed.set_footer(text="May your hands always be warm.")
    await ctx.send(embed=embed)


@client.command()
async def wednesday(ctx):
    if datetime.datetime.today().weekday() == 2:
        embed = discord.Embed(title="It is Wednesday",
                              description="Please weep accordingly, or suffer the wrath of Bun.".format(
                                  ctx.bot.message_counter),
                              color=0xefe0b4)
        embed.set_footer(text="May your hands always be warm.")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="It is not Wednesday",
                              description="Drink plenty of liquids in preparation of the Day of Weeps.".format(
                                  ctx.bot.message_counter),
                              color=0xefe0b4)
        embed.set_footer(text="May your hands always be warm.")
        await ctx.send(embed=embed)


@client.command()
async def howtopray(ctx):
    await ctx.send(f'You may give thanks using the following emote: "<:butwhy:719983036346663014>"')


@client.command()
async def buncommandments(ctx):
    await ctx.send(f'Here are the following valid commandments during the test: !wednesday, !howtopray, !tears')


class believers:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


list = [believers('Rambo', ramboScore), believers('Nano', nanoScore), believers('Koth', kothScore),
        believers('Tenbear', tenScore), believers('DocBaker', docScore)]

# appending instances to list

list.sort(key=lambda x: x.roll, reverse=True)


@client.command()
async def leader(ctx):
    for obj in list:
        #print(obj.name, obj.roll, sep=' ')
        await ctx.send(f'{obj.name}:  {obj.roll}')
        #await ctx.send()


@client.command()
async def leaderboard(ctx):
    embed = discord.Embed(title="Temple Bun’Quarik",
                          description=f"Weeping board:\n"
                                      f"{bunTest}".format(
                              ctx.bot.message_counter),
                          color=0xefe0b4)
    embed.set_footer(text="May your hands always be warm.")
    await ctx.send(embed=embed)


client.run('Nzk1NjczNjI4OTU5MzA5ODc1.X_My0A.RRuJmQGhNSNMM7IS_hbhoj__iE0')
