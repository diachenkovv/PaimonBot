import os
from dotenv import load_dotenv
load_dotenv()

settings = {
    'token': os.getenv('TOKEN'),
    'bot': 'Paimon Bot',
    'id': os.getenv('UID'),
    'prefix': '%',
    'bot_ver': '0.0.1-alpha'
}