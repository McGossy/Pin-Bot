

def read_token():
    with open('token.txt', 'r') as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True


bot = commands.Bot(
    command_prefix='!pin ',
    allowed_mentions=discord.AllowedMentions(
        users=False,  # Whether to ping individual user @mentions
        everyone=False,  # Whether to ping @everyone or @here mentions
        roles=False,  # Whether to ping role @mentions
        replied_user=False,  # Whether to ping on replies to messages
    ),
)


bot.load_extension("textCommands")
bot.load_extension("onMessage")


try:
    print('sys_flags')
    #sys_flags = discord.SystemChannelFlags
    #print(sys_flags)
except:
    print("That shit didn't work")




bot.run(token)
