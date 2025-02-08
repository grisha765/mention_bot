from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from db.setting import get_setting, set_setting

async def settings_msg(message, chat_id, use_edit: bool = False):
    all_access = await get_setting(chat_id, "all_access")
    if all_access:
        typee = "Members"
    else:
        typee = "Admins"

    keyboard=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(f"@all access - {typee}", callback_data=f"all_access")]
        ]
    )

    if use_edit:
        await message.edit_text("Settings:", reply_markup=keyboard)
    else:
        await message.reply_text("Settings:", reply_markup=keyboard)

async def settings_func(message, chat_id, option):
    await set_setting(chat_id, option)
    await settings_msg(message, chat_id, use_edit=True)

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
