class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6253265083"
    SUDO_USERS = "6253265083", "5382284735", "5297949798","6338745050"
    GROUP_ID = "-1002096627846"
    TOKEN = "6511494597:AAEVP5QbpkZYEcXbbu5Eom9Qir31G4Z2kGk"
    MONGO_URL = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/2322cb937757a22a2a39d.jpg", "https://telegra.ph/file/2322cb937757a22a2a39d.jpg"]
    SUPPORT_CHAT = "WAIFU_GRABBERS"
    UPDATE_CHAT = "WH_ubdates"
    BOT_USERNAME = "Grab_waifus_bot"
    CHARA_CHANNEL_ID = "-1002043886349"
    API_ID = 26516344
    API_HASH = "7a3f7d55d89476a15a62b4dd39062556"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
