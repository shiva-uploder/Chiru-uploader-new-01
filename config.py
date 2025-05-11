import os

# Retrieve API credentials and settings from environment variables
API_ID = os.environ.get("API_ID", "15816419")
API_HASH = os.environ.get("API_HASH", "626ed6dab78881858778d9663682962e")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
PASS_DB = int(os.environ.get("PASS_DB", "721"))

# Retrieve OWNER and ADMINS settings
OWNER = int(os.environ.get("OWNER", 2088265361))

# Initialize admins list
ADMINS = [2088265361]

# If the ADMINS environment variable is set, populate the list
try:
    admin_ids = os.environ.get("ADMINS", "2088265361").split()
    ADMINS.extend(int(x) for x in admin_ids)
except ValueError:
    raise Exception("Your Admins list does not contain valid integers.")
    
# Add OWNER to the ADMINS list
ADMINS.append(OWNER)

# Group or channel settings (you can uncomment and set these when needed)
# LOG = -1002359700029  # Log group ID
# UPDATE_GRP = <your_update_group_id>  # Bot updates group ID
# auth_chats = []  # List of authorized chat IDs for the bot

