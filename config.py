from os import environ

API_ID = int(environ.get("API_ID", "20562331"))
API_HASH = environ.get("API_HASH", "9e3e4148e73756a85b95fc69980b678d")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002597848806"))
ADMINS = int(environ.get("ADMINS", "8181956369"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://bhanuchutia:7plotuyi@cluster0.su379.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "Cluster0")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
