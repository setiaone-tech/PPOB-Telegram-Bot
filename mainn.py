import telebot, requests, random, string
from menu import *
from api import *
from pembayaran import *
import mysql.connector


API_BOT = '' #APIKEY Telegram Bot
API_IAK = '' #APIKEY IAK Account
USER_IAK = '' #Username IAK Account

bot = telebot.TeleBot(API_BOT)
ses = requests.session()
temp_user = {}

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "tokopulsa"
)
mycursor = mydb.cursor()

@bot.message_handler(commands=['start'])
def send_start(message):
	bot.reply_to(message, 'Selamat datang di toko DC, Kami menyediakan segala kebutuhan top up pulsa. Ketik /menu untuk melihat menu')

@bot.message_handler(commands=['menu'])
def send_menu(message):
    chat_id = message.chat.id
    bot.reply_to(message, Menu(), parse_mode='Markdown')
    ran = random.randint(0, 1)
    if ran == 0:
        bot.send_message(chat_id, 'Ingin berdonasi? langsung klik <a href="https://saweria.co/scriptkiddiez">disini</a>', parse_mode='HTML')

@bot.message_handler(commands=['daftarlayanan'])
def send_layanan(message):
    chat_id = message.chat.id
    msg = bot.reply_to(message, Layanan(), parse_mode='Markdown')
    bot.register_next_step_handler(msg, pilihan_layanan)

def pilihan_layanan(message):
    try:
        chat_id = message.chat.id
        mess = message.text
        pesan = ""
        if mess == "1":
            pesan = AXIS()
        elif mess == "2":
            pesan = INDOSAT()
        elif mess == "3":
            pesan = SMARTFREN()
        elif mess == "4":
            pesan = TELKOMSEL()
        elif mess == "5":
            pesan = TRI()
        elif mess == "6":
            pesan = XL()
        else:
            bot.reply_to(message, "*HARAP PILIH SESUAI DENGAN PILIHAN YANG ADA!*", parse_mode='Markdown')
        fixpesan = pesan['teks']
        bot.reply_to(message, fixpesan, parse_mode='Markdown')
    except Exception as e:
        print(e)

@bot.message_handler(commands=['pembelian'])
def send_beli(message):
    chat_id = message.chat.id
    temp_user[chat_id] = {}
    msg = bot.reply_to(message, Layanan(), parse_mode='Markdown')
    bot.register_next_step_handler(msg, pilihan_beli)

def pilihan_beli(message):
    try:
        chat_id = message.chat.id
        mess = message.text
        pesan = ""
        if mess == "1":
            pesan = AXIS()
        elif mess == "2":
            pesan = INDOSAT()
        elif mess == "3":
            pesan = SMARTFREN()
        elif mess == "4":
            pesan = TELKOMSEL()
        elif mess == "5":
            pesan = TRI()
        elif mess == "6":
            pesan = XL()
        else:
            bot.reply_to(message, "*HARAP PILIH SESUAI DENGAN PILIHAN YANG ADA!*", parse_mode='Markdown')
        fixpesan = pesan['teks']
        msg = bot.reply_to(message, fixpesan, parse_mode='Markdown')
        bot.register_next_step_handler(msg, tampil_beli, pesan['data'])
    except Exception as e:
        bot.reply_to(message, e)

def tampil_beli(message, data):
    try:
        chat_id = message.chat.id
        pesan = message.text
        pesan = int(pesan)
        harga = int(data[pesan-1][2])+2000
        pilih_id = data[pesan-1][0]
        temp_user[chat_id]['pilih1'] = f'Pulsa {data[pesan-1][1]}'
        temp_user[chat_id]['pilih2'] = f'{data[pesan-1][2]}(Rp. {harga})'
        teks =f'''
        Apakah anda yakin ingin membeli
        Produk      : Pulsa {data[pesan-1][1]} {data[pesan-1][2]} 
        Harga       : (Rp. {harga})
        Masa Aktif  : {data[pesan-1][3]} hari
        '''
        markup = telebot.types.InlineKeyboardMarkup()
        id1 = telebot.types.InlineKeyboardButton(text="Ya", callback_data=f"/order {pilih_id} {harga}")
        id2 = telebot.types.InlineKeyboardButton(text="Tidak", callback_data="/menu ")
        markup.row(id1,id2)
        bot.send_message(chat_id, teks, reply_markup = markup)
    except Exception as e:
        bot.reply_to(message, e)
        
@bot.callback_query_handler(func=lambda call: True)
def handler(call):
    cari = call.data
    bagi = cari.split(" ")
    if bagi[0] == "/order":
        uid = bagi[1]
        harga = bagi[2]
        msg = bot.send_message(call.from_user.id, 'Masukan Nomer HP Anda (08) : ')
        bot.register_next_step_handler(msg, order_beli, uid, harga)
    elif bagi[0] == "/fixorder":
        user = call.from_user.id
        nomer = temp_user[call.from_user.id]['nomer']
        uid = bagi[1]
        harga = bagi[2]
        uname = call.from_user.username
        order_id = ''.join(random.choices(string.ascii_lowercase+string.ascii_uppercase, k = 5))
        order_id = str(user)+order_id
        order = BAYAR(order_id, harga, uname)
        status = 'pending'
        sql = "INSERT INTO transaksi (order_id, product_id, user_id, nomer, status) VALUES (%s, %s, %s, %s, %s)"
        val = (order_id, uid, user, nomer, status)
        mycursor.execute(sql, val)
        mydb.commit()
        teks = f"<a href='{order['redirect_url']}'>Klik Disini</a> Untuk Menyelesaikan Pembayaran Anda."
        bot.send_message(user, teks, parse_mode='html')
    else:
        send_menu(call['from_user']['id'])

def order_beli(message, uid, harga):
    try:
        chat_id = message.chat.id
        nomer = message.text
        temp_user[chat_id]['nomer'] = nomer
        teks = f"__Apakah data dibawah ini sudah benar?__\n\nProduk = **{temp_user[chat_id]['pilih1']}**\nNominal(Harga) = **{temp_user[chat_id]['pilih2']}**\nNomer = **{temp_user[chat_id]['nomer']}**"
        markup = telebot.types.InlineKeyboardMarkup()
        id1 = telebot.types.InlineKeyboardButton(text="Ya", callback_data=f"/fixorder {uid} {harga}")
        id2 = telebot.types.InlineKeyboardButton(text="Tidak", callback_data="/menu ")
        markup.row(id1,id2)
        bot.send_message(chat_id, teks, reply_markup = markup, parse_mode='Markdown')
    except Exception as e:
        print(e)


@bot.message_handler(commands=['cek'])
def send_cek(message):
    chat_id = message.chat.id
    print(chat_id)
        

print(' ==> Bot Running....')
bot.remove_webhook()
bot.polling()
