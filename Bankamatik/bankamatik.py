# Bankamatik Uygulaması


hesaplar = [
    {
        "ad": "User 1",
        "hesap_no": "1551527",
        "bakiye": 90000,
        "ek_hesap": 5000,
        "username": "userone",
        "password": "12345678"
    },
    {
        "ad": "User 2",
        "hesap_no": "1623672",
        "bakiye": 10000,
        "ek_hesap": 6000,
        "username": "usersecond",
        "password": "87654321"
    }
]

def menu(hesap):
    print("\n")
    print(f"Merhaba, {hesap['ad']}")

    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")

    islem = input("Yapmak istediğiniz işlemi tuşlayınız: ")

    if islem == "1":
        bakiye_sorgula(hesap)

    elif islem == "2":
        para_cekme(hesap)

    elif islem == "3":
        para_yatirma(hesap)

    else:
        print("Hatalı İşlem Tuşladınız!!!")

    menu(hesap)

def bakiye_sorgula(hesap):
    print(f"Hesap bakiyesi = {hesap['bakiye']}")
    print(f"Ek hesap bakiyesi = {hesap['ek_hesap']}")

def para_yatirma(hesap):
    yatan_para = float(input("Yatırmak istediğiniz para miktarını giriniz: "))
    print("Parayı göze yerleştiriniz")
    hesap['bakiye'] += yatan_para
    print("İşlem Başarılı!")

def para_cekme(hesap):
    miktar = float(input("Çekmek istediğiniz miktarı giriniz: "))
    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print("Paranızı alınız!")
    else:
        toplam = hesap['bakiye'] + hesap['ek_hesap']

        if toplam >= miktar:
            ek_hesap_kullanim_izni = input("Ek hesap kullanılsın mı? (E/H) ")
            if ek_hesap_kullanim_izni == "E":
                kullanilacak_miktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ek_hesap'] -= kullanilacak_miktar
                print("Paranızı alabilirsiniz!")
            else:
                print("Üzgünüz, bakiye yetersiz!")
        else:
            print("Üzgünüz, bakiye yetersiz!")

def login():
    username = input("Username: ")
    password = input("Password: ")

    is_logged_in = False

    for hesap in hesaplar:
        if hesap['username'] == username and hesap['password'] == password:
            is_logged_in = True
            menu(hesap)
            break

    if not is_logged_in:
        print("Hatalı username ya da password!!!")
    
    
    login()

login()