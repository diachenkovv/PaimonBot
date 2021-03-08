import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils import manage_commands
from config import settings

bot = commands.Bot(
    command_prefix=settings['prefix'], intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)
guild_ids = [settings['guild_ids']]
# Не передаём аргумент pass_context, так как он был нужен в старых версиях.


@slash.slash(name="test")
async def _test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])


@bot.event
async def on_ready():
    print("On Air!")


@slash.slash(
    name="test",
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


@slash.slash(name="test")
async def test(ctx):
    await ctx.respond()
    await ctx.send('test')


@slash.slash(name="invite")
async def invite(ctx):
    await ctx.respond()
    await ctx.send("Эй!\nЕсли хочешь добавить меня на свой сервер, то вот ссылка: [Paimon Bot](https://discordapp.com/oauth2/authorize?&client_id=818187894891610182&scope=bot&permissions=8)")


@slash.slash(name="hello")
async def hello(ctx):  # Создаём функцию и передаём аргумент ctx.
    # Объявляем переменную author и записываем туда информацию об авторе.
    author = ctx.message.author
    await ctx.respond()
    # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
    await ctx.send(f'Hello, {author.mention}!')

# Обращаемся к словарю settings с ключом token, для получения токена
bot.run(settings['token'])
