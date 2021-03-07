import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from config import settings

bot = commands.Bot(
    command_prefix=settings['prefix'], intents=discord.Intents.all())
slash = SlashCommand(bot)

# Не передаём аргумент pass_context, так как он был нужен в старых версиях.


@bot.command()
async def test(ctx):
    await ctx.send('test')


@bot.command()
async def invite(ctx):
    await ctx.send("Эй!\nЕсли хочешь добавить меня на свой сервер, то вот ссылка: [Paimon Bot](https://discordapp.com/oauth2/authorize?&client_id=818187894891610182&scope=bot&permissions=8)")


@bot.command()
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    # Объявляем переменную author и записываем туда информацию об авторе.
    author = ctx.message.author

    # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    await ctx.send(f'Hello, {author.mention}!')

# Обращаемся к словарю settings с ключом token, для получения токена
bot.run(settings['token'])
