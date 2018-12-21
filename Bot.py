import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="*")

bot.remove_command("help")


@bot.event
async def on_ready():
    print('Ready to go!')
    print(f"serving: {len(bot.guilds)} guilds.")
    await bot.change_presence(activity=discord.Game(name="Prefix *"))


@bot.command()
async def ping(ctx):
    ping1 = bot.latency
    ping2 = round(ping1 * 1000)
    await ctx.channel.send(f"Your ping is {ping2}ms")


bot.run("process.env.token")
