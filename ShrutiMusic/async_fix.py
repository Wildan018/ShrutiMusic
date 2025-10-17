# memastikan ada event loop default pada saat modul ini diimpor
import asyncio

def ensure_event_loop():
    try:
        # jika ada running loop, tidak lakukan apa-apa
        asyncio.get_running_loop()
    except RuntimeError:
        # tidak ada running loop -> buat dan set
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

# jalankan saat diimpor agar proteksi berlaku seawal mungkin
ensure_event_loop()
