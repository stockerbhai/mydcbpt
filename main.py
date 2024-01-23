import discord
from discord.ext import commands

token = 'MTE5OTAyNzgxMDM4NDIyNDI3Ng.GflzaM.5ejTqDega4VJQktwhNrME9424-iXpeW5SXG46A'

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')
    await bot.change_presence(activity=discord.Game(name='Protecting 2k+ servers...'), status=discord.Status.dnd)


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! I am alive')

@bot.command(name='autosetup')
async def autosetup(ctx):
    await ctx.send(f"<:emote_true:1176144283913429035> Now no one can touch your server . Just up my role for security reasons")
@bot.command(name='help')
async def help(ctx):
    await ctx.send(
        f"**Radium Help Menu**\n"
        f"> Just Run !autosetup command this command will automatically complete all setup"
    )

if __name__ == '__main__':
    bot.run(token)
