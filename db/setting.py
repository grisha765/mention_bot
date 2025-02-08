from tortoise.exceptions import DoesNotExist
from db.models import Settings
from typing import Optional

async def set_setting(chat_id: int, option: str, parametr: Optional[bool] = None) -> bool:
    try:
        existing_setting = await Settings.get_or_none(chat_id=chat_id, option=option)
        
        if parametr is None:
            if existing_setting:
                parametr = not existing_setting.parametr
            else:
                parametr = True
        
        if existing_setting:
            existing_setting.parametr = parametr
            await existing_setting.save()
        else:
            await Settings.create(chat_id=chat_id, option=option, parametr=parametr)
        
        return True
    except Exception:
        return False

async def get_setting(chat_id: int, option: str) -> bool:
    try:
        setting = await Settings.get(chat_id=chat_id, option=option)
        return setting.parametr
    except DoesNotExist:
        return False
    except Exception:
        return False

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
