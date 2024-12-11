intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
bot = commands.Bot(command_prefix='>', intents=intents, help_command=None)

bot.start(token)
