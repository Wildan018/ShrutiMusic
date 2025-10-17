# memastikan ada event loop default pada saat modul ini diimpor
import asyncio
import sys

# Jika uvloop tersedia, pasang policy dulu (harus sebelum membuat loop)
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    print("DEBUG: uvloop EventLoopPolicy set in async_fix", file=sys.stderr)
except Exception as e:
    print(f"DEBUG: uvloop not available or failed to set policy: {e}", file=sys.stderr)

def ensure_event_loop():
    try:
        # jika ada running loop, tidak lakukan apa-apa
        asyncio.get_running_loop()
    except RuntimeError:
        # tidak ada running loop -> buat dan set
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        print("DEBUG: new asyncio event loop created and set in async_fix", file=sys.stderr)

# jalankan saat diimpor agar proteksi berlaku seawal mungkin
ensure_event_loop()
print("DEBUG: ShrutiMusic.async_fix loaded and event loop ensured", file=sys.stderr)
