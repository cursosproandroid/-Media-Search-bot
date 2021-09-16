# Cursos Pro Android by Skueletor ©️ 2021
# Información del bot
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 12345
API_HASH = '0123456789abcdef0123456789abcdef'
BOT_TOKEN = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'

# Ajustes del bot
MAX_RESULTS = 10
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Administradores, canales y usuarios
ADMINS = [12345789, 'admin123', 806200981]
CHANNELS = [-10012345678, -100987654321, 'channelusername']
AUTH_USERS = []

# Información sobre MongoBD
DATABASE_URI = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb]?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

# Mensajes
START_MSG = """
**Hola, soy el bot de búsqueda de canales, creados por Pro Android :D**
Aquí puede buscar archivos en inline mode. Simplemente presione los siguientes botones y comience a buscar archivos subidos al canal.
**Bot hecho con ❤️ por Skueletor**
"""

SHARE_BUTTON_TEXT = 'Revisa {username} para buscar archivos en forma **inline** :D'
