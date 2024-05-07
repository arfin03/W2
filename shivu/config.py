class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6995317382"
    sudo_users = "6995317382", "5382284735", "5297949798", "6338745050", "1466012993", "5348552949"
    GROUP_ID = "-1002096627846"
    TOKEN = "6992015243:AAEw0sazm80dQLcgYUeufjwtaagp5HqqYZM"
    mongo_url = "mongodb+srv://BrandedSupportGroup:BRANDED_WORLD@cluster0.v4odcq9.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/7565b6a25a480d4dad36e.jpg", "https://telegra.ph/file/f7da678981007299d5a0e.jpg"]
    SUPPORT_CHAT = "WAIFU_GRABBERS"
    UPDATE_CHAT = "WH_ubdates"
    BOT_USERNAME = "Grab_waifus_bot"
    CHARA_CHANNEL_ID = "-1002043886349"
    api_id = 26516344
    api_hash = "7a3f7d55d89476a15a62b4dd39062556"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
