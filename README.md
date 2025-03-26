📢 Forward Mesej Telegram Tanpa Bot
Script ini adalah untuk forward mesej dari satu channel atau group Telegram ke channel atau group lain tanpa menggunakan bot. Ia hanya menggunakan akaun Telegram biasa dengan login melalui nombor telefon.

🎯 Kegunaan:
Forward mesej dari channel/group A ke channel/group B secara automatik.

Sesuai untuk backup mesej, memantau saluran Telegram atau menyimpan salinan mesej penting.

⚠️ Nota: Pastikan dapat kebenaran dari admin channel/group asal sebelum guna.

🛠️ Keperluan:
Python 3.x

Library Telethon

API_ID dan API_HASH Telegram. Boleh dapatkan di sini: my.telegram.org

📥 Cara Pemasangan:
Muat turun atau clone repo ini:

bash
Copy
Edit
git clone https://github.com/username/reponame.git
cd reponame
Pasang library Telethon:

bash
Copy
Edit
pip install telethon
⚙️ Konfigurasi:
Edit bahagian berikut dalam script telegram_user_forwarder.py:

python
Copy
Edit
API_ID = 1234567                # Masukkan API ID anda
API_HASH = "your_api_hash_here"  # Masukkan API Hash anda
PHONE_NUMBER = "+60123456789"    # Nombor Telefon Telegram anda

SOURCE_CHAT = -1001234567890  # ID Channel/Group Asal
TARGET_CHAT = -1009876543210  # ID Channel/Group Tujuan
🔎 Cara Dapatkan ID Channel/Group:
Guna bot @username_to_id_bot untuk dapatkan ID.

Atau, guna kod ini untuk dapatkan senarai ID:

python
Copy
Edit
async for dialog in client.iter_dialogs():
    print(f"{dialog.name} - {dialog.id}")
🚀 Jalankan Script:
Pastikan konfigurasi sudah betul.

Run script:

bash
Copy
Edit
python telegram_user_forwarder.py
Masukkan kod pengesahan Telegram jika diminta.

⚠️ Penting:
Jangan salah guna! Forward hanya dari channel/group yang anda ada kebenaran.

Elakkan forward mesej dari channel/group sensitif atau tanpa izin.

Telegram boleh sekat akaun jika ada laporan penyalahgunaan.

