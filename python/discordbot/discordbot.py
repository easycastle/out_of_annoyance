import discord
import os
from discord.ext import commands

token = ""

bot = commands.Bot(command_prefix="", intents=discord.Intents.all())

bot.remove_command("help")

startup_extensions = ['cogs.'+file[:-3] for file in os.listdir('cogs') if file.endswith('.py')] # cogs 폴더에 익스텐션들이 있는걸루

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print("cannot be loaded {}\n{}".format(extension, e))

@bot.event()
async def on_ready():
    print("====================")
    print(bot.user.name)
    print(bot.user.id)
    print("====================")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(token)
