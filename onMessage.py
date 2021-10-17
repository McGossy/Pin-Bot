import discord
from discord.ext import commands, tasks

class OnMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.is_ready = False

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')
        self.is_ready = True

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Ignores self
        if message.author == self.bot.user:
            return

        # Ignores all bots
        if message.author.bot:
            return



        guild = message.guild
        channel = message.channel
        channel_id = str(message.channel.id)
        author = message.author
        msg = message.content.lower()
        approved = False

        # opens the ignore file and sees if the channel is in it or not
        approved_read = open("approved_channels.txt", "r")
        for line in approved_read.readlines():
            if channel_id in line:
                approved = True
        if approved == False:
            approved_read.close()
            return

        if message.attachments:
            await message.pin()
            print("There was an attachment. Message pinned")
        print(message.attachments)


def setup(bot: commands.Bot):
    bot.add_cog(OnMessage(bot))







