import re
import os
from os import environ, getenv
from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


SESSION = environ.get('SESSION', 'media_search')
API_ID = int(environ.get('API_ID', '26010287'))
API_HASH = environ.get('API_HASH', 'aac3af06e0eab941e0fb18efb84791ab')
BOT_TOKEN = environ.get('BOT_TOKEN', "")

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://ibb.co/chvj3FYs https://ibb.co/yB7fkJFj https://ibb.co/yFT9ztsD https://ibb.co/DfXsL3Z7 https://ibb.co/Fbp8KVJv https://ibb.co/C3cMcnZ9 https://ibb.co/gZz60vFT https://ibb.co/Y4Hcy18C https://ibb.co/CKHWWq7B https://ibb.co/Vc18HRLp https://ibb.co/JRncWbSB https://ibb.co/7NxQkLVj https://ibb.co/NnScDWBp https://ibb.co/b5197Kv5 https://ibb.co/Pv8wLPq6 https://ibb.co/KcGPdWqK https://ibb.co/q3sz31wd')).split() 
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/62efbcc4e7580b76530ba.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/4073ba3f8086757c0ac29.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/3dacdcead375a33fc0697.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://telegra.ph/file/f983d857f3ce40795e4b8.jpg'))
FSUB_IMG = (environ.get('FSUB_IMG', 'https://i.ibb.co/cShkPjcZ/x.jpg')).split() 

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7983671882 1368186248 6456879892').split()]  #Admin Id
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002334615923').split()] #Movie Database Channel Id
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002144072367'))  #Log Channel Id
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '-1002144072367'))  #Streming Log Channel Id
MOVIE_UPDATE_CHANNEL = int(environ.get('MOVIE_UPDATE_CHANNEL', '-1001935648115'))  #Movie Update Channel Id
PREMIUM_LOGS = int(environ.get('PREMIUM_LOGS', '-1002144072367')) #Premium Subscription Log Channel Id
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002144072367') #Movie Request Channel Id
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1002260763858') #Support Chat Id
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Aamiya:Aamiya@cluster0.4dwdd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") #MongoDB Url
DATABASE_NAME = environ.get('DATABASE_NAME', "AamiyaBot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'MovieFiles')

# If MULTIPLE_DB Is True Then Fill DATABASE_URI2 Value Else You Will Get Error.
MULTIPLE_DB = is_enabled(os.environ.get('MULTIPLE_DB', "False"), False) # Type True For Turn On MULTIPLE DB FUNTION 
DATABASE_URI2 = environ.get('DATABASE_URI2', "")

GRP_LNK = environ.get('GRP_LNK', 'https://t.me/MoviePalace_Off')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/TeamMoviePalace')
OWNER_LNK = environ.get('OWNER_LNK', 'https://t.me/LegPieceOff')
UPDATE_CHANNEL_LNK = environ.get('UPDATE_CHANNEL_LNK', 'https://t.me/+uEDa74LQv945N2E1')

#Force Subscription Channel (Put Same Channel Id In Both Veriables)
AUTH_CHANNEL = int(environ.get('AUTH_CHANNEL', '-1001805073152')) 
AUTH_REQ_CHANNEL = int(environ.get('AUTH_REQ_CHANNEL', '-1002144072367'))

IS_VERIFY = is_enabled('IS_VERIFY', False)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002595419106')) #Verification Channel Id 
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', '-1002595419106')) #If Anyone Set Your Bot In Any Group And Set Shortner In That Group Then In This Channel The All Details Come
VERIFY_IMG = environ.get("VERIFY_IMG", "https://telegra.ph/file/9ecc5d6e4df5b83424896.jpg")

TUTORIAL = environ.get("TUTORIAL", "https://t.me/MoviePalace_Off")
TUTORIAL_2 = environ.get("TUTORIAL_2", "https://t.me/MoviePalace_Off")
TUTORIAL_3 = environ.get("TUTORIAL_3", "https://t.me/MoviePalace_Off")

# Verification (Must Fill All Veriables. Else You Got Error
SHORTENER_API = environ.get("SHORTENER_API", "")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "")

SHORTENER_API2 = environ.get("SHORTENER_API2", "")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "")

SHORTENER_API3 = environ.get("SHORTENER_API3", "")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "")

TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "1200"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "54000"))

#Othes
TMDB_API = environ.get("TMDB_API", "6abcb6bb99fb77f33c37016a28866ed2")
MOVIE_UPDATE_NOTIFICATION = bool(environ.get("MOVIE_UPDATE_NOTIFICATION", False))
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', 'Lots of Love from Team MOVIEPALACE ❤︎')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/MoviePalaceSupport') #Support Chat Link
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
DELETE_TIME = int(environ.get("DELETE_TIME", "300"))  
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "False")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)
PM_SEARCH = bool(environ.get('PM_SEARCH', True)) 
EMOJI_MODE = bool(environ.get('EMOJI_MODE', True)) 

LANGUAGES = ["malayalam", "mal", "tamil", "tam", "english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan", "gujarati", "guj", "marathi", "mar", "punjabi", "koeran", "chinese", ""]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]
SEASONS = ["s01" , "s02" , "s03" , "s04", "s05" , "s06" , "s07" , "s08" , "s09" , "s10"]

STREAM_MODE = bool(environ.get('STREAM_MODE', True))

#Dont Make Any Changes Here. Creat A Veriable Name "FQDN" In Your Deploying Plartform And Put App Url
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LegPieceBotz'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LegPiece'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))
else:
    ON_HEROKU = False
HAS_SSL = bool(getenv('HAS_SSL', True))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "http://{}/".format(FQDN)


REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]


Bot_cmds = {
    "start": "ꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ",
    "trendlist": "ɢᴇᴛ ᴛᴏᴘ ꜱᴇᴀʀᴄʜ ʟɪꜱᴛ",
    "myplan" : "ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ",
    "plan" :"ᴄʜᴇᴄᴋ ᴘʀᴇᴍɪᴜᴍ ᴘʀɪᴄᴇ",
    "settings": "ᴄʜᴀɴɢᴇ sᴇᴛᴛɪɴɢs",
    "group_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "admin_cmd": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "details": "ꜱᴇᴇ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ",
    "reset_group": "ʀᴇꜱᴇᴛ ɢʀᴏᴜᴘ ꜱᴇᴛᴛɪɴɢꜱ", 
    "stats": "ᴄʜᴇᴄᴋ ʙᴏᴛ ꜱᴛᴀᴛᴜꜱ.",
    "delete": "ᴅᴇʟᴇᴛᴇ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ꜰɪʟᴇ ꜰʀᴏᴍ ᴅʙ.",
    "movie_update": "ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "pm_search": "ᴘᴍ sᴇᴀʀᴄʜ ᴏɴ ᴏғғ ᴀᴄᴄᴏʀᴅɪɴɢ ʏᴏᴜʀ ɴᴇᴇᴅᴇᴅ...",
    "restart": "ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ."
}

#Don't Change Anything Here
if MULTIPLE_DB == False:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI
else:
    DATABASE_URI = DATABASE_URI
    DATABASE_URI2 = DATABASE_URI2
