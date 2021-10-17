import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure


class TextCommands(commands.Cog):
    """A few simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                print(end='')
        # was going to try to get this to auto find the welcome channel
        sys_flags = discord.SystemChannelFlags
        print(sys_flags)

    @has_permissions(manage_messages=True)
    @commands.command(name="start")
    async def start_channel(self, ctx: commands.Context):
        """I will start pinning in the channel I see this in."""
        approved_read = open("approved_channels.txt", "r")
        approved_write = open("approved_channels.txt", "a")
        c_id = str(ctx.channel.id)
        already_approved = False
        for line in approved_read.readlines():
            if c_id in line:
                already_approved = True
        if already_approved == False:
            approved_write.write(c_id + "\n")
            await ctx.send("Got it.")

        else:
            await ctx.send("I'm already pinning here.")

        approved_read.close()
        approved_write.close()

    @start_channel.error
    async def ignore_channel_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            await ctx.send("You can't do that")

    @has_permissions(manage_messages=True)
    @commands.command(name="stop")
    async def stop_channel(self, ctx: commands.Context):
        """I will stop pinning the channel this is in."""
        approved_read = open("approved_channels.txt", "r")
        c_id = str(ctx.channel.id)
        already_approved = False
        approved_file_lines = approved_read.readlines()
        for line in approved_file_lines:
            if c_id in line:
                approved_file_lines.remove(line)
                already_approved = True
                break
        if already_approved == True:
            approved_write = open("approved_channels.txt", "w")
            for line in approved_file_lines:
                approved_write.write(line)
            approved_write.close()
            await ctx.send("I'll stop pinning here.")
        else:
            await ctx.send("I wasn't doing it anyway.")

        approved_read.close()

    @stop_channel.error
    async def stop_channel_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            msg = "No"
            await ctx.send(msg)




# Now, we need to set up this cog somehow, and we do that by making a setup function:
def setup(bot: commands.Bot):
    bot.add_cog(TextCommands(bot))