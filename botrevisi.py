from telegram import Update,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler, CallbackContext, filters,CallbackQueryHandler
from telegram.ext.filters import Regex
from fuzzywuzzy import fuzz
import string
import pywhatkit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re
import pywhatkit as kit
import pandas as pd

# Deklarasi variabel di awal fungsi
previous_mesage_id = None
previous_message1_id = None
previous_message2_id = None
previous_message3_id = None

# Daftar kata valid untuk typo detection
valid_words = ["halo", "hai", "selamat", "pagi", "siang", "malam", "start", "selesai", "terima kasih"]

# Fungsi untuk mendeteksi typo dan memberikan saran
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower().translate(str.maketrans('', '', string.punctuation))

    best_match = None
    highest_score = 0
    for word in valid_words:
        score = fuzz.ratio(text, word)
        if score > highest_score:
            highest_score = score
            best_match = word

    if best_match and highest_score > 10:
        await update.message.reply_text(f"Apakah yang Anda maksud '{best_match}'?")

# Fungsi untuk perintah /start
async def start(update: Update, context: CallbackContext) -> None:
    # await update.message.reply_text("Halo! Selamat datang di coffe_bot, ketik <b>lanjut</b> untuk melanjutkan",parse_mode='HTML')
    keyboard = [
        [
            InlineKeyboardButton("Pesan menu 1", callback_data="menu1"),
            InlineKeyboardButton("Pesan menu 2", callback_data="menu2")
        ],
        [
            InlineKeyboardButton("Pesan menu 1 & menu 2", callback_data="menu12")
        ],
        [
            InlineKeyboardButton("Privacy Policy", callback_data="privacy")      
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Halo, Selamat datang!!\nSilahkan pilih pesanan berikut:\n1. Milk Coffee Rp.5000\n2. Coffee with Strawberry Flavored Rp.6500\ntekan pesan untuk memesan", reply_markup = reply_markup)
async def button(update: Update, context: CallbackContext):
    global previous_message_id,previous_message1_id,previous_message2_id,previous_message3_id #untuk menyimpan ID sebelumnya
    query = update.callback_query
    await query.answer()  # Mengirimkan konfirmasi ke Telegram

    # Jika callback data adalah 'send_message', bot akan mengirimkan pesan ke chat pengguna
    if query.data == "menu1":
        keyboard = [
        [
            InlineKeyboardButton("Ya", callback_data="yes"),
            InlineKeyboardButton("Tidak", callback_data="no")
        ]
    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        sent_message = await query.message.reply_text("Apakah anda yakin ingin memesan Chocolate Coffe\nTotal pesanan anda adalah Rp 5000",reply_markup=reply_markup)
        previous_message_id = sent_message.message_id #simpan ID pesan terkirim
    elif query.data == "yes":
        await query.message.reply_text("Selamat datang di coffe_bot, silahkan isi format berikut")
        time.sleep(3)
        # Pengguna akan menerima pesan otomatis dari bot
        message = "Silahkan kirim pesan sesuai dengan format dibawah\n\u2757\u2757 Gunakan +62 \u2757\u2757\nContoh :"
        
        # Mengirimkan pesan ke pengguna
        await query.message.reply_text(message)
        
        await query.message.reply_text("nama : Kevin \nnomor wa : +62123456789\npesanan : Milk Coffe")
    elif query.data == "no":
        #Hapus pesan sebelemnya jika ada
        if previous_message_id:
            try:
                await context.bot.delete_message(chat_id=query.message.chat_id, message_id=previous_message_id)
                previous_message_id = None
            except Exception as e:
                print(f"Error saat menghapus pesan: {e}")
    elif query.data == "menu2":
        keyboard = [
        [
            InlineKeyboardButton("Ya", callback_data="yes"),
            InlineKeyboardButton("Tidak", callback_data="no")
        ]
    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        sent_message = await query.message.reply_text("Apakah anda yakin ingin memesan Strawberry Coffe\nTotal pesanan anda adalah Rp 6500",reply_markup=reply_markup)
        previous_message_id = sent_message.message_id #simpan ID pesan terkirim
    elif query.data == "menu12":
        keyboard = [
        [
            InlineKeyboardButton("Ya", callback_data="yes"),
            InlineKeyboardButton("Tidak", callback_data="no")
        ]
    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        sent_message = await query.message.reply_text("Apakah anda yakin ingin memesan Chocolate Coffe & Strawbery Coffe\nTotal pesanan anda adalah Rp 11500",reply_markup=reply_markup)
        previous_message_id = sent_message.message_id #simpan ID pesan terkirim
    elif query.data == "privacy":
        # Pengguna akan menerima informasi privasi
        message = "Selamat datang di coffe_bot, silahkan baca Kebijakan Privasi kami"

        home_message3 = await query.message.reply_text(message)
        time.sleep(3)

        home_message2 = await query.message.reply_text("Kebijakan Privasi  Coffee_Bot\n\n   1.Pendahuluan\n\nCoffe_Bot adalah chatbot yang dirancang untuk membantu pengguna dalam memesan kopi. Kebijakan Privasi ini menjelaskan bagaimana kami menggumpulkan, menggunakan, dan melindungi infprmasi anda saat Anda berinteraksi dengan bot kami\n\n   2.Data yang kami kumpulkan\n\nKetika anda menggunakan Coffe_Bot, kami dapat mengumpulkan data berikut:\n\n Nama : Seuai yang anda berikan saat berinteraksi\n\nNomor WhatsApp : Untuk konfirmasi dan memberitahu Anda tentang status pemesanan anda\n\n   3. Cara kami menggunakan data anda\n\nData yang digunakan hanya untuk tujuan berikut :\n\nMemberitahu Anda saat pesanan sedang diproses\n\n\nKami tidak menggunakan data anda untuk pemasaran, iklan, atau tujuan lain di luar layanan yang disediakan\n\n   4.Berbagi data\n\nKami tidak membagikan data anda kepada pihak ketiga kecuali jika diperlukan untuk mengoperasikan Coffe_Bot. ini termasuk platform pemrograman Python yang digunakan untuk fungsionalitas Bot.\n\n   5.Penyimpanan data\n\nCoffe_Bot tidak menyimpan data anda. Data seperti nama dan nomor WhatsApp diproses sementara melaluli pywhatkit untuk mengirim pemberitahuan dan tidak disimpan setelahnya.\n\n   6.Keamanan data\n\nkami mengambil langkan-langkah yang wajar untuk memastikan bahwa datta yang diproses selama interaksi ditangani dengan aman. Proses data dilakukak langsung tanpa penyimpanan jangka panjang\n\nNamun, Kami tidak dapan mmenjamin keamanan penuh ini terjadi pelnaggaran data diluar kendali kami, seperti penyalahgunaan oleh pihak ketiga atau kelemahan platform.\n\n   7.Batasan tanggung jawab\n\nCOffe_Bot hanya bertanggung jawab atas data yang diproses selama interaksi dengan bot. Kami tidak bertanggung jawab atas :\n\nPenyalahgunaan data oleh pihak ketiga\n\nMasalah keamanan yang berasal dari perangkat atau platform penggunaan.\n\n   8.Persetujuan pengguna\n\nDengan menggunakan Coffe_Bot, anda dianggap telah membaca, memahami, dan menyetujui Kebijakan Privasi ini.\n\n   9.Kebijakan pengguna bot\n\nPengguna dilarang menggunakan Coffe_Bot untuk :\n\nTindakan melanggar hukum\n\nKami berhak memblokir pengguna yang melanggar kebijakan ini.\n\n   10.Perubahan kebijakan ini\n\nKebijakan Privasi ini dapat diperbarui dari waktu ke waktu. Perubahan signifikan akan diberitahukan melalui bot.\n\n   11.Hubungi kami\n\nJika anda memiliki pertanyaan atau kehawatiran tentang Kebijakan Privasi ini, Silahkan hubungi kami melalui @malakulkabir di Telegram.\n\nTanggal Berlaku : 24 Desember 2024")
        keyboard = [
            [
                InlineKeyboardButton("home",callback_data="home")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        home_message1 = await query.message.reply_text("Tekan <b>home</b> untuk kembali ke menu sebelumnya", parse_mode='HTML',reply_markup=reply_markup)
        previous_message1_id = home_message1.message_id #simpan ID pesan terkirim
        previous_message2_id = home_message2.message_id #simpan ID pesan terkirim
        previous_message3_id = home_message3.message_id #simpan ID pesan terkirim
    elif query.data == "home":
        if previous_message1_id:
            try:
                await context.bot.delete_message(chat_id=query.message.chat_id, message_id=previous_message1_id)
            except Exception as e:
                print(f"Error saat menghapus pesan dengan ID {previous_message1_id}: {e}")
            finally:
                previous_message1_id = None
        if previous_message2_id:
            try:
                await context.bot.delete_message(chat_id=query.message.chat_id, message_id=previous_message2_id)
            except Exception as e:
                print(f"Error saat menghapus pesan dengan ID {previous_message2_id}: {e}")
            finally:
                previous_message2_id = None
        if previous_message3_id:
            try:
                await context.bot.delete_message(chat_id=query.message.chat_id, message_id=previous_message3_id)
            except Exception as e:
                print(f"Error saat menghapus pesan dengan ID {previous_message3_id}: {e}")
            finally:
                previous_message3_id = None
    elif query.data == "home_menu":
        # Mengirimkan pesan ke menu awal
        keyboard = [
        [
            InlineKeyboardButton("Pesan menu 1", callback_data="menu1"),
            InlineKeyboardButton("Pesan menu 2", callback_data="menu2")
        ],
        [
            InlineKeyboardButton("Pesan menu 1 & menu 2", callback_data="menu12")
        ],
        [
            InlineKeyboardButton("Privacy Policy", callback_data="privacy")      
        ]
    ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Halo, Selamat datang!!\nSilahkan pilih pesanan berikut:\n1. Milk Coffee Rp.5000\n2. Coffee with Strawberry Flavored Rp.6500\ntekan pesan untuk memesan", reply_markup = reply_markup)
    elif query.data == "confirm":
        # Mengirimkan pesan konfirmasi ke pengguna
        await query.message.reply_text("Terimakasih atas konfirmasi anda\U0001F604 ")
        keyboard = [
            [
                InlineKeyboardButton("Home", callback_data="home_menu")
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Tekan Home untuk kembali ke menu awal", reply_markup=reply_markup)
    elif query.data == "cancel":
        # Mengirimkan pesan batal ke pengguna
        await query.message.reply_text("SILAHKAN KIRIM ULANG FORMAT ANDA\nmohon maaf untuk ketidaknyamanannya\U0001F61E")
        await query.message.reply_text("kirim <b>home</b> untuk kembali ke menu awal", parse_mode='HTML')

# Fungsi untuk kembali ke menu awal
async def handle_menu(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Pesan menu 1", callback_data="menu1"),
             InlineKeyboardButton("Pesan menu 2", callback_data="menu2")
        ],
        [
            InlineKeyboardButton("Pesan menu 1 & menu 2", callback_data="menu12")
        ],
        [
            InlineKeyboardButton("Privacy Policy", callback_data="privacy")      
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)  # Ganti nama variabel menjadi reply_markup
    await update.message.reply_text(
        "Halo, Selamat datang!!\nSilahkan pilih pesanan berikut:\n1. Milk Coffee Rp.5000\n2. Coffee with Strawberry Flavored Rp.6500\ntekan pesan untuk memesan", 
        reply_markup=reply_markup  # Gunakan reply_markup disini
    )


DEFAULT_CONTACT = "+6285230070232"
# Fungsi untuk mendeteksi nomor telepon dalam pesan
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    contact = DEFAULT_CONTACT

    messagetwo = text
    name, order = extract_info(text) 
    phone_match = re.search(r'(\+62|62|0)[0-9]{9,13}', text)
    if phone_match:
        phone_number = phone_match.group()
        message = f"Terimakasih {name}\ndengan pesanan {order}\nMohon menunggu, pesanan anda sedang diproses!!\U0001F604\n\nPESAN INI OTOMATIS DIKIRIMKAN OLEH BOT KE NOMOR YANG ANDA MASUKKAN SAAT ANDA MENGISI FORMAT, TERIMAKASIH"
    
        await update.message.reply_text("Terimakasih untuk pesanan anda \U0001F604\nMohon tunggu sebentar ya")
        
        # Kirim pesan WhatsApp
        try:
            pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
            time.sleep (5)
            pywhatkit.sendwhatmsg_instantly(contact, messagetwo, wait_time=10)
            keyboard = [
                [
                    InlineKeyboardButton("Konfirmasi", callback_data="confirm"),
                    InlineKeyboardButton("Batal", callback_data="cancel")
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(f"Pesan berhasil dikirim ke {phone_number}.\nsilahkan cek WhatsApp anda")
            # await update.message.reply_text("kirim <b>home</b> untuk kembali ke menu awal", parse_mode='HTML')
            await update.message.reply_text("konfirmasi apakah anda telah menerima pesan di WhatsApp",reply_markup=reply_markup)
            # await query.answer(text="Pesanan berhasil dikirim", show_alert=True)
        except Exception as e:
            await update.message.reply_text(f"Gagal mengirim pesan: {e}\nSilahkan isi nomor telepon yang sesuai")
    else:
        await update.message.reply_text("Tidak ada nomor telepon yang valid dalam pesan\nSilahkan isi nomor telepon yang sesuai")

# async def function_menu(update: Update, context : CallbackContext) ->None:
#     keyboard = [
#         [
#             InlineKeyboardButton("Ya", callback_data="yes"),
#             InlineKeyboardButton("Tidak", callback_data="no")
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     await update.message.reply_text("Apakah anda yakin ingin memesan Chocholat Coffe\n  Total pesanan anda anda adalah Rp 50000",reply_markup=reply_markup)
# Fungsi untuk mengekstrak nama dan pesanan
def send_whatsapp_message(phone_number, message):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Jalankan di background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Kirim pesan WhatsApp
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10)
        time.sleep(5)  # Tunggu beberapa detik agar proses selesai
    finally:
        driver.quit()
# Fungsi untuk mengirim pesan menggunakan Selenium dan pywhatkit
def send_whatsapp_message(phone_number, message):
    # Setup Selenium untuk headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Headless mode
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Jalankan driver dengan opsi headless
    driver = webdriver.Chrome(options=chrome_options)

    # Kirim pesan WhatsApp menggunakan pywhatkit (browser tetap berjalan di background)
    pywhatkit.sendwhatmsg_instantly("+6285230070232", "Pesan default", wait_time=10)

    # Jangan lupa untuk menutup driver setelah selesai
    time.sleep(5)  # Tunggu beberapa detik sebelum menutup
    driver.quit()

def extract_info(text):
    # # Pola regex untuk nama, nomor WhatsApp, dan pesanan
    name_pattern = r"nama\s*:\s*(.+)"
    order_pattern = r"pesanan\s*:\s*(.+)"
    
    # Ekstraksi nama
    name_match = re.search(name_pattern, text, re.IGNORECASE)
    name = name_match.group(1).strip() if name_match else "Nama tidak ditemukan"
    
    # Ekstraksi pesanan
    order_match = re.search(order_pattern, text, re.IGNORECASE)
    order = order_match.group(1).strip() if order_match else "Pesanan tidak ditemukan"
    
    # Kembalikan nama, pesanan, dan nomor WhatsApp
    return name, order
    
    return name, order
def save_order_to_csv(name,order):
    data = {"Nama" : [name], "Pesanan" : [order], "Waktu" : [time.ctime()]}
    df = pd.DataFrame(data)
    df.to_csv("riwayatpesanan.csv",mode='a',header= False,index=False)
# Fungsi utama
def main():
    token = "7555000051:AAEWgXB-E9vFzEB_GqwqT7HrzmhBK_ZPo2A"
    application = Application.builder().token(token).build()

    # Tambahkan handler
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(Regex("^(home|Home)$"), handle_menu))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Jalankan bot
    application.run_polling()

if __name__ == "__main__":
    main()
