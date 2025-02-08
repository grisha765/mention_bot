import asyncio
from db.setting import get_setting
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, CallbackQuery
from config import logging_config
logging = logging_config.setup_logging(__name__)

async def is_all_access(_, client, message) -> bool:
    chat_id = message.chat.id
    user = message.from_user
    all_access = await get_setting(chat_id, "all_access")
    if not all_access:
        logging.debug(f"{chat_id}: Access to All is only for admins.")
        member = await client.get_chat_member(chat_id, user.id)
        if member.status not in (ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR):
            logging.debug(f"{chat_id}|{user.id}: The user is not an admin.")
            return False
    return True

async def is_admin(_, client, update) -> bool:
    if isinstance(update, Message):
        chat_id = update.chat.id
        user = update.from_user
    elif isinstance(update, CallbackQuery):
        chat_id = update.message.chat.id
        user = update.from_user
    else:
        logging.error("Instance not found.")
        return False

    member = await client.get_chat_member(chat_id, user.id)
    if member.status not in (ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR):
        msg_text = "Only admins can use this."
        if isinstance(update, CallbackQuery):
            await update.answer(msg_text)
        else:
            msg = await update.reply_text(msg_text)
            await asyncio.sleep(10)
            await msg.delete()
        logging.debug(f"{chat_id}|{user.id}: The user is not an admin.")
        return False

    return True

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
