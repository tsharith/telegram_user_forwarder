from telethon import TelegramClient, events, sync

# Config Telegram API
API_ID = 1234567  # Ganti dengan API ID anda
API_HASH = "your_api_hash_here"  # Ganti dengan API Hash anda
PHONE_NUMBER = "+60123456789"  # Nombor Telefon Telegram anda

# Group atau Channel Asal dan Tujuan
SOURCE_CHAT = -1001234567890  # ID Group/Channel Asal (gunakan nilai negatif untuk channel)
TARGET_CHAT = -1009876543210  # ID Group/Channel Tujuan (guna nilai negatif)

# Setup Client
client = TelegramClient("anon_session", API_ID, API_HASH)

# Login dengan SMS (hanya kali pertama)
async def main():
    await client.start(phone=PHONE_NUMBER)
    print("[INFO] Login berjaya!")

# Forward mesej dari SOURCE_CHAT ke TARGET_CHAT
@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def handler(event):
    try:
        await client.send_message(TARGET_CHAT, event.message)
        print("[INFO] Mesej berjaya dihantar!")
    except Exception as e:
        print(f"[ERROR] {e}")

with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
