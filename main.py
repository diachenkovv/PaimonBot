import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(
    command_prefix=settings['prefix'], intents=discord.Intents.all())

# Не передаём аргумент pass_context, так как он был нужен в старых версиях.

# Отображение статуса бота в консоли


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

# вывести написанное сообщение (эхо)


@bot.command()
async def welcome(ctx, *, message):
    if message == 'none':
        await ctx.send('test')
    else:
        await ctx.send(message)

# Отправка пригласительного сообщения когда учасник присоединяется


@bot.event
async def on_member_join(member):
    ment = member.mention
    id_channel = int(settings['chatroom'])
    await bot.get_channel(id_channel).send(f"Добро пожаловать в наш город, {ment} :wave:\nВыбрать роли можешь тут: <#743813246355767318>\nНадеемся тебе понравиться у нас :heart:")
    print(f"{member} has joined the server.")

# Отправка сообщения когда учасник покидает сервер


@bot.event
async def on_member_remove(member):
    id_channel = int(settings['chatroom'])
    await bot.get_channel(id_channel).send(f"Только что покинул нас {member} :broken_heart:")
    print(f"{member} has left the server.")

# Отправка текста test


@bot.command()
async def test(ctx):
    await ctx.send('test')

# Ссылка на бот


@bot.command()
async def invite(ctx):
    await ctx.send("Эй!\nЕсли хочешь добавить меня на свой сервер, то вот ссылка: [Paimon Bot](https://discordapp.com/oauth2/authorize?&client_id=818187894891610182&scope=bot&permissions=8)")

# Приветствие учасника


@bot.command()
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    # Объявляем переменную author и записываем туда информацию об авторе.
    author = ctx.message.author

    # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    await ctx.send(f'Hello, {author.mention}!')

# Обращаемся к словарю settings с ключом token, для получения токена
bot.run(settings['token'])
