# memastikan ada event loop default pada saat modul ini diimpor
import asyncio
import sys

def ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

ensure_event_loop()
print("DEBUG: ShrutiMusic.async_fix loaded and event loop ensured", file=sys.stderr)
