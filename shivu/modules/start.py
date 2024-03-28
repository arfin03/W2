import random
from html import escape 

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, CommandHandler

from shivu import application, PHOTO_URL, SUPPORT_CHAT, UPDATE_CHAT, BOT_USERNAME, db, GROUP_ID
from shivu import pm_users as collection 


async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    first_name = update.effective_user.first_name
    username = update.effective_user.username

    user_data = await collection.find_one({"_id": user_id})

    if user_data is None:
        
        await collection.insert_one({"_id": user_id, "first_name": first_name, "username": username})
        
        await context.bot.send_message(chat_id=GROUP_ID, 
                                       text=f"New user Started The Bot..\n User: <a href='tg://user?id={user_id}'>{escape(first_name)})</a>", 
                                       parse_mode='HTML')
    else:
        
        if user_data['first_name'] != first_name or user_data['username'] != username:
            
            await collection.update_one({"_id": user_id}, {"$set": {"first_name": first_name, "username": username}})

    

    if update.effective_chat.type== "private":
        
        
        caption = f"""
        ***👋Hᴇʏʏʏʏ...***

*** 😋I Aᴍ A Wᴀɪғᴜ Cᴀᴛᴄʜᴇʀ Bᴏᴛ..\n 😏I ᴡɪʟʟ sᴇɴᴅ Rᴀɴᴅᴏᴍ Wᴀɪғᴜ's   \n/grab ᴛᴏ.. Cᴏʟʟᴇᴄᴛ ᴛʜᴀᴛ Wᴀɪғᴜs ɪɴ Yᴏᴜʀ Cᴏʟʟᴇᴄᴛɪᴏɴ \nᴀɴᴅ 👀sᴇᴇ Cᴏʟʟᴇᴄᴛɪᴏɴ ʙʏ ᴜsɪɴɢ /harem... \n\n Sᴏ ᴀᴅᴅ ɪɴ Yᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ Cᴏʟʟᴇᴄᴛ Yᴏᴜʀ ʜᴀʀᴇᴍ🎉***
        """
        
        keyboard = [
            [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("HELP", callback_data='help')]     
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        photo_url = random.choice(PHOTO_URL)

        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption=caption, reply_markup=reply_markup, parse_mode='markdown')

    else:
        photo_url = random.choice(PHOTO_URL)
        keyboard = [
            [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("HELP", callback_data='help')]
        ]
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_photo(chat_id=update.effective_chat.id, photo=photo_url, caption="🎴Alive!?... \n connect to me in PM For more information ",reply_markup=reply_markup )

async def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'help':
        help_text = """
    ***Help Section:***
    
***/grab: To Grab character (only works in group)\n***
\n***/fav: Add Your fav\n***
\n***/trade : To trade Characters\n***
\n***/gift: Give any Character from Your Collection to another user.. (only works in groups)\n***
\n***/collection: To see Your Collection\n***
\n***/topgroups : See Top Groups.. Ppl Guesses Most in that Groups\n***
\n***/top: Too See Top Users\n***
\n***/ctop : Your ChatTop\n***
\n***/changetime: Change Character appear time (only works in Groups)\n***
   """
        help_keyboard = [[InlineKeyboardButton("⤾ Bᴀᴄᴋ", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(help_keyboard)
        
        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=help_text, reply_markup=reply_markup, parse_mode='markdown')

    elif query.data == 'back':

        caption = f"""
        ***👋Hᴇʏʏʏʏ...*** ✨

*** 😋I Aᴍ A Wᴀɪғᴜ Cᴀᴛᴄʜᴇʀ Bᴏᴛ..\n 😏I ᴡɪʟʟ sᴇɴᴅ Rᴀɴᴅᴏᴍ Wᴀɪғᴜ's   \n/grab ᴛᴏ.. Cᴏʟʟᴇᴄᴛ ᴛʜᴀᴛ Wᴀɪғᴜs ɪɴ Yᴏᴜʀ Cᴏʟʟᴇᴄᴛɪᴏɴ \nᴀɴᴅ 👀sᴇᴇ Cᴏʟʟᴇᴄᴛɪᴏɴ ʙʏ ᴜsɪɴɢ /harem... \n\n Sᴏ ᴀᴅᴅ ɪɴ Yᴏᴜʀ ɢʀᴏᴜᴘs ᴀɴᴅ Cᴏʟʟᴇᴄᴛ Yᴏᴜʀ ʜᴀʀᴇᴍ🎉***
        """

        
        keyboard = [
            [InlineKeyboardButton("ADD ME", url=f'http://t.me/{BOT_USERNAME}?startgroup=new')],
            [InlineKeyboardButton("SUPPORT", url=f'https://t.me/{SUPPORT_CHAT}'),
            InlineKeyboardButton("UPDATES", url=f'https://t.me/{UPDATE_CHAT}')],
            [InlineKeyboardButton("HELP", callback_data='help')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.edit_message_caption(chat_id=update.effective_chat.id, message_id=query.message.message_id, caption=caption, reply_markup=reply_markup, parse_mode='markdown')


application.add_handler(CallbackQueryHandler(button, pattern='^help$|^back$', block=False))
start_handler = CommandHandler('start', start, block=False)
application.add_handler(start_handler)
