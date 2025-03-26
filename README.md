Forward Mesej Telegram Tanpa Bot
Script ini direka untuk memindahkan mesej dari satu channel atau group Telegram ke channel atau group lain tanpa menggunakan bot. Ia hanya menggunakan akaun Telegram biasa dengan login melalui nombor telefon.

Kegunaan:

Memindahkan mesej dari channel/group A ke channel/group B secara automatik.

Sesuai untuk membuat salinan sandaran mesej, memantau saluran Telegram, atau menyimpan mesej penting.

Nota: Pastikan anda mendapat kebenaran daripada admin channel/group asal sebelum menggunakannya.

Keperluan:

Python 3.x

Pustaka Telethon

API_ID dan API_HASH Telegram. Boleh dapatkan di my.telegram.org

Cara Pemasangan:

Muat turun atau clone repositori ini

Pasang pustaka Telethon: pip install telethon

Konfigurasi: Edit bahagian berikut dalam script telegram_user_forwarder.py:

API_ID = 1234567 # Masukkan API ID anda API_HASH = "your_api_hash_here" # Masukkan API Hash anda PHONE_NUMBER = "+60123456789" # Nombor Telefon Telegram anda SOURCE_CHAT = -1001234567890 # ID Channel/Group Asal TARGET_CHAT = -1009876543210 # ID Channel/Group Tujuan

Cara Mendapatkan ID Channel/Group:

Guna bot @username_to_id_bot untuk mendapatkan ID.

Atau, gunakan kod ini untuk mendapatkan senarai ID channel/group yang anda sertai:

async for dialog in client.iter_dialogs(): print(f"{dialog.name} - {dialog.id}")

Cara Menjalankan Script:

Pastikan semua konfigurasi telah diubah suai dengan betul.

Jalankan script dengan arahan berikut: python telegram_user_forwarder.py

Masukkan kod pengesahan Telegram jika diminta.
