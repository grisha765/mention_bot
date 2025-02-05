from config.config import Config
from pyrogram import Client, filters, enums #type: ignore

from config import logging_config
logging = logging_config.setup_logging(__name__)

app = Client("bot", api_id=Config.tg_id, api_hash=Config.tg_hash, bot_token=Config.tg_token)

@app.on_message(filters.command("all", prefixes=["/", "@", "#"]))
async def handle_all(client, message):
    chat_id = message.chat.id
    members = client.get_chat_members(chat_id)
    text = "Members:\n"
    async for member in members:
        user = member.user
        if user.username:
            text += f"@{user.username}\n"
        elif user.first_name:
            text += f"{user.first_name}\n"
        else:
            text += f"Unknown\n"
    await client.send_message(text=text, chat_id=chat_id)

@app.on_message(filters.command("admins", prefixes=["/", "@", "#"]))
async def handle_admin(client, message):
    chat_id = message.chat.id
    admins = client.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
    
    text = "Admins:\n"
    async for member in admins:
        user = member.user
        if user.username:
            text += f"@{user.username}\n"
        elif user.first_name:
            text += f"{user.first_name}\n"
        else:
            text += "Unknown\n"
    
    await client.send_message(text=text, chat_id=chat_id)

async def start_bot():
    logging.info("Launching the bot...")
    await app.start()
    logging.info("Bot is running!")

async def stop_bot():
    logging.info("Stopping the bot...")
    await app.stop()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")

