# in & as Hardwork
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/SearchBoxPrashant'>Search Box </a> is The Best Movie Search Group.

    PrashantLinks: 
        <a href='https://t.me/Sparrow6606'>❤️ PrashantLinks ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/SearchBoxPrashant'>Search Box</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Backup Channel: <a href='https://t.me/Prime6Backup'>Prashant Backup</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Owner : <a href='https://t.me/Sparrow6606'>PrashantLinks</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

Wellcome To Movie & Series Search Bot 🎥. Sent Me Any Movie & Series Name !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

I Will Sent You The Series & Movie Watch/ Download Link.

»»» <b>Happy Searching</b> «««

🔺Thank You <a href='https://t.me/Sparrow6606'>Prashant Links</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

Wellcome To Movie & Series Search Bot 🎥. Sent Me Any Movie & Series Name !!

 I Will Sent You The Series & Movie Watch/ Download Link.</b>

   »»»» <b>Happy Searching</b> ««««
"""

