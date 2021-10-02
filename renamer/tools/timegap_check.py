import time
from ..config import Config
from .progress_bar import TimeFormatter

async def timegap_check(m):
    """Checking the time gap is completed or not 
    and checking the parallel process"""

    if m.from_user.id in Config.TIME_GAP_STORE:
        if int(time.time() - Config.TIME_GAP_STORE[m.from_user.id]) < Config.TIME_GAP:
            text = f"ഞാനും ഒരു മനുഷ്യനല്ലേ {TimeFormatter((int(Config.TIME_GAP_STORE[m.from_user.id]) + Config.TIME_GAP - int(time.time())) * 1000)}.ഒന്ന് Wait Cheyy🤧"
            await m.reply_text(
                text=text,
                parse_mode="markdown",
                quote=True
            )
            return True
        else:
            del Config.TIME_GAP_STORE[m.from_user.id]
            return False
    else:
        return False
