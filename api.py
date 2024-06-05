import requests
from hashlib import md5

url = "https://prepaid.iak.id/api/pricelist/pulsa/"
API_IAK = '58961aa59c6790ca'
USER_IAK = '085273359226'
temp_user = {}
headers = {'Content-Type': 'application/json'}

def AXIS(num):
    tujuan = url+"axis"
    MD5 = md5((USER_IAK+API_IAK+'pl').encode()).hexdigest()
    payload = '{"username": "'+USER_IAK+'","sign": "'+MD5+'","status": "active"}'
    res = requests.post(tujuan, data=payload, headers=headers)
    res = res.json()
    hasil = []
    teks = ""
    for i in res['data']['pricelist']:
        if i['product_nominal'].isdigit():
            hasil.append([i['product_code'],i['product_description'],i['product_nominal'],i['active_period']])
    if num == 1:
        teks += "_Daftar Harga_\n\n"
        for i in range(len(hasil)):
            teks += (f"{i+1}. Produk : *Pulsa {hasil[i][1]} {hasil[i][2]}*\nHarga : *Rp. {int(hasil[i][2])+2000}*\nMasa Aktif : *{hasil[i][3]} Hari*\n\n")
    else:
        teks += "_Pilihan yang tersedia_\n\n"
        for i in range(len(hasil)):
            teks += (f"*{i+1}. {hasil[i][1]} {hasil[i][2]} (Rp. {int(hasil[i][2])+2000})*\n")
    
    data = {"teks":teks, "data":hasil}
    return data
    
def INDOSAT(num):
    tujuan = url+"indosat"
    MD5 = md5((USER_IAK+API_IAK+'pl').encode()).hexdigest()
    payload = '{"username": "'+USER_IAK+'","sign": "'+MD5+'","status": "active"}'
    res = requests.post(tujuan, data=payload, headers=headers)
    res = res.json()
    hasil = []
    teks = ""
    for i in res['data']['pricelist']:
        if i['product_nominal'].isdigit():
            hasil.append([i['product_code'],i['product_description'],i['product_nominal'],i['active_period']])
    if num == 1:
        teks += "_Daftar Harga_\n\n"
        for i in range(len(hasil)):
            teks += (f"{i+1}. Produk : *Pulsa {hasil[i][1]} {hasil[i][2]}*\nHarga : *Rp. {int(hasil[i][2])+2000}*\nMasa Aktif : *{hasil[i][3]} Hari*\n\n")
    else:
        teks += "_Pilihan yang tersedia_\n\n"
        for i in range(len(hasil)):
            teks += (f"*{i+1}. {hasil[i][1]} {hasil[i][2]} (Rp. {int(hasil[i][2])+2000})*\n")
    
    data = {"teks":teks, "data":hasil}
    return data
    
def SMARTFREN(num):
    tujuan = url+"smart"
    MD5 = md5((USER_IAK+API_IAK+'pl').encode()).hexdigest()
    payload = '{"username": "'+USER_IAK+'","sign": "'+MD5+'","status": "active"}'
    res = requests.post(tujuan, data=payload, headers=headers)
    res = res.json()
    hasil = []
    teks = ""
    for i in res['data']['pricelist']:
        if i['product_nominal'].isdigit():
            hasil.append([i['product_code'],i['product_description'],i['product_nominal'],i['active_period']])
    if num == 1:
        teks += "_Daftar Harga_\n\n"
        for i in range(len(hasil)):
            teks += (f"{i+1}. Produk : *Pulsa {hasil[i][1]} {hasil[i][2]}*\nHarga : *Rp. {int(hasil[i][2])+2000}*\nMasa Aktif : *{hasil[i][3]} Hari*\n\n")
    else:
        teks += "_Pilihan yang tersedia_\n\n"
        for i in range(len(hasil)):
            teks += (f"*{i+1}. {hasil[i][1]} {hasil[i][2]} (Rp. {int(hasil[i][2])+2000})*\n")
    
    data = {"teks":teks, "data":hasil}
    return data

def TELKOMSEL(num):
    tujuan = url+"telkomsel"
    MD5 = md5((USER_IAK+API_IAK+'pl').encode()).hexdigest()
    payload = '{"username": "'+USER_IAK+'","sign": "'+MD5+'","status": "active"}'
    res = requests.post(tujuan, data=payload, headers=headers)
    res = res.json()
    hasil = []
    teks = ""
    for i in res['data']['pricelist']:
        if i['product_nominal'].isdigit():
            hasil.append([i['product_code'],i['product_description'],i['product_nominal'],i['active_period']])
    if num == 1:
        teks += "_Daftar Harga_\n\n"
        for i in range(len(hasil)):
            teks += (f"{i+1}. Produk : *Pulsa {hasil[i][1]} {hasil[i][2]}*\nHarga : *Rp. {int(hasil[i][2])+2000}*\nMasa Aktif : *{hasil[i][3]} Hari*\n\n")
    else:
        teks += "_Pilihan yang tersedia_\n\n"
        for i in range(len(hasil)):
            teks += (f"*{i+1}. {hasil[i][1]} {hasil[i][2]} (Rp. {int(hasil[i][2])+2000})*\n")
    
    data = {"teks":teks, "data":hasil}
    return data

    
def TRI(num):
    tujuan = url+"three"
    MD5 = md5((USER_IAK+API_IAK+'pl').encode()).hexdigest()
    payload = '{"username": "'+USER_IAK+'","sign": "'+MD5+'","status": "active"}'
    res = requests.post(tujuan, data=payload, headers=headers)
    res = res.json()
    hasil = []
    teks = ""
    for i in res['data']['pricelist']:
        if i['product_nominal'].isdigit():
            hasil.append([i['product_code'],i['product_description'],i['product_nominal'],i['active_period']])
    if num == 1:
        teks += "_Daftar Harga_\n\n"
        for i in range(len(hasil)):
            teks += (f"{i+1}. Produk : *Pulsa {hasil[i][1]} {hasil[i][2]}*\nHarga : *Rp. {int(hasil[i][2])+2000}*\nMasa Aktif : *{hasil[i][3]} Hari*\n\n")
    else:
        teks += "_Pilihan yang tersedia_\n\n"
        for i in range(len(hasil)):
            teks += (f"*{i+1}. {hasil[i][1]} {hasil[i][2]} (Rp. {int(hasil[i][2])+2000})*\n")
    
    data = {"teks":teks, "data":hasil}
    return data

    
def XL(num):
    try:
        tujuan = url+"xl"
        MD5 = md5((USER_IAK+API_IAK+'pl').encode()).hexdigest()
        payload = '{"username": "'+USER_IAK+'","sign": "'+MD5+'","status": "active"}'
        res = requests.post(tujuan, data=payload, headers=headers)
        res = res.json()
        hasil = []
        teks = ""
        for i in res['data']['pricelist']:
            if i['product_nominal'].isdigit():
                hasil.append([i['product_code'],i['product_description'],i['product_nominal'],i['active_period']])
        if num == 1:
            teks += "_Daftar Harga_\n\n"
            for i in range(len(hasil)):
                teks += (f"{i+1}. Produk : *Pulsa {hasil[i][1]} {hasil[i][2]}*\nHarga : *Rp. {int(hasil[i][2])+2000}*\nMasa Aktif : *{hasil[i][3]} Hari*\n\n")
        else:
            teks += "_Pilihan yang tersedia_\n\n"
            for i in range(len(hasil)):
                teks += (f"*{i+1}. {hasil[i][1]} {hasil[i][2]} (Rp. {int(hasil[i][2])+2000})*\n")
        data = {"teks":teks, "data":hasil}
        return data
    except Exception as e:
        print(e)