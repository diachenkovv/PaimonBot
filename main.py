import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils import manage_commands
from config import settings

bot = commands.Bot(
    command_prefix=settings['prefix'], intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)
guild_ids = [settings['guild_ids']]

# инициализация бота


@bot.event
async def on_ready():
    print("On Air!")

# текст формата embed


@slash.slash(name="embed", guild_ids=guild_ids)
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])

# отправка введенного аргумента


@slash.slash(
    name="repeat",
    description="this returns the bot latency",
    options=[manage_commands.create_option(
        name="argone",
        description="description of first argument",
        option_type=3,
        required=True
    )],
    guild_ids=guild_ids
)
async def _test(ctx, argone: str):
    await ctx.respond()
    await ctx.send(f"You responded with {argone}.")

# отправка текста "test"


@slash.slash(name="text", guild_ids=guild_ids)
async def test(ctx):
    await ctx.respond()
    await ctx.send('test')

# отправка invite ссылки


@slash.slash(name="invite", guild_ids=guild_ids)
async def invite(ctx):
    await ctx.send("Эй!\nЕсли хочешь добавить меня на свой сервер, то вот ссылка: [Paimon Bot](https://discordapp.com/oauth2/authorize?&client_id=818187894891610182&scope=bot&permissions=8)")

# отправка сообщения "Hello, {имя учасника с упоминанием}"


@slash.slash(name="hello", guild_ids=guild_ids)
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    # Объявляем переменную author и записываем туда информацию об авторе.
    author = ctx.message.author
    # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    await ctx.send(f'Hello, {author.mention}!')

# Обращаемся к словарю settings с ключом token, для получения токена
bot.run(settings['token'])

# разработка слеш команд временно приостановлена в связи с нестабильной работой библиотеки
