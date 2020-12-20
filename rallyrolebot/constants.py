from discord import Color
# TODO: Place holder for now - can use __init__.py once dependencies such as 
# data.ROLE_MAPPINGS_TABLE and rally_api.BASE_URL have been removed

"""
 Constants useful for data module
"""
ROLE_MAPPINGS_TABLE = "mappings"
CHANNEL_MAPPINGS_TABLE = "channel_mappings"
RALLY_CONNECTIONS_TABLE = "rally_connections"
CONFIG_TABLE = "config"

GUILD_ID_KEY = "guildId"
COIN_KIND_KEY = "coinKind"
REQUIRED_BALANCE_KEY = "requiredBalance"
ROLE_NAME_KEY = "roleName"
CHANNEL_NAME_KEY = "channel"
DISCORD_ID_KEY = "discordId"
RALLY_ID_KEY = "rallyId"
CONFIG_NAME_KEY = "configName"
PURCHASE_MESSAGE_KEY = "purchaseMessage"
DONATE_MESSAGE_KEY = "donateMessage"

"""
 Constants useful for  rally_api module
"""

COIN_KIND_KEY = "coinKind"
COIN_BALANCE_KEY = "coinBalance"

BASE_URL = "https://api.rally.io/v1"


"""
    Constants useful for update_cog module
"""
UPDATE_WAIT_TIME = 600

"""
    Miscellaneous constants
"""

ERROR_COLOR =  Color(0xFF0000)
SUCCESS_COLOR = Color(0x0000FF)
WARNING_COLOR = Color(0xFFFF00)

DEFAULT_DONATE_MESSAGE = "You can donate to by going to - Your donation helps grow and support the community and creator - Plus, there are 10 tiers of Donation badges to earn to show off your support!"
DEFAULT_PURCHASE_MESSAGE = "You can purchase at by using a Credit/Debit card or a number of different Crypto Currencies! Buying earns rewards, supports the community, and you can even get VIP Status! (hint: there’s a secret VIP room for users who hold over X # of ;)"