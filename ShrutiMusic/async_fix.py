# memastikan ada event loop default pada saat modul ini diimpor
import asyncio
import sys

def ensure_event_loop():
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

# jalankan saat diimpor agar proteksi berlaku seawal mungkin
ensure_event_loop()

# DEBUG: cetak agar terlihat di logs bahwa async_fix dieksekusi
print("async_fix loaded", file=sys.stderr)
