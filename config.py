import os
from dotenv import load_dotenv
load_dotenv()

settings = {
    'token': os.getenv('TOKEN'),
    'bot': 'Paimon Bot',
    'id': os.getenv('UID'),
    'prefix': '%',
    'bot_ver': '0.0.1-alpha',
    'guild_ids': os.getenv('SERVER_ID'),
    'chatroom': os.getenv('CHANNEL_ID')
}
