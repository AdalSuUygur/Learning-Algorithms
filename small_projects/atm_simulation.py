
#! Kendime not: edge caselere bakmadım, try except bloğuna eklemem kodlar var!
#todo Kapsamlı ATM Simülasyonu
#Kullanıcı adı ve şifre ile giriş, 3 kere hak var. Doğru girişte menüde 1- bakiye sorgula 2- para yatır, 3-para çek, 4-çıkış
#Bakiye başlangıçta belirlenir. para yatırılırsa bakiyeye eklenir, çekilirse çıkartılır.
#Para çekerken: Önemli! Çekilmek istenen tutar bakiyeden fazlaysa "Yetersiz bakiye" uyarısı verilmeli, işlem yapılmamalı.

users = {
    "ahmet_yilmaz": {
        "sifre": "1234",
        "bakiye": 5250.75
    },
    "ayse_kaya": {
        "sifre": "4321",
        "bakiye": 12800.00
    },
    "mehmet_demir": {
        "sifre": "9876",
        "bakiye": 450.50
    },
    "zeynep_can": {
        "sifre": "0000",
        "bakiye": 25600.20
    },
    "can_berk": {
        "sifre": "5555",
        "bakiye": 10.00
    }
}

def verify_login(username: str, password: str) -> bool:
    for user in users.keys():
        if username == user:
            if users[username]["sifre"] == password:
                return True
            return False
    return False
def currency_operations(username: str, operation_name: str):
    match operation_name:
        case "check":
            return check_currency(username=username)
        case "deposit":
            return deposit_currency(bakiye= users[username]["bakiye"])
        case "withdraw":
            return withdraw_currency(bakiye= users[username]["bakiye"])
def check_currency(username: str) -> float:
    return users[username]["bakiye"]
def deposit_currency(bakiye: float) -> float:
    addition = float(input("Yatırılacak para: "))
    return bakiye + addition
def withdraw_currency(bakiye: float) -> float | str:
    withdraw = float(input("Çekilecek para: "))
    if bakiye < withdraw:
        return "Yetersiz bakiye"
    else:
        return bakiye - withdraw

trying_count = 3
while trying_count > 0:
    user_name = input("username: ")
    pass_word = input("password: ")
    if verify_login(username=user_name, password=pass_word):
        while True:
            operation_name = input("Operation name: ")
            if operation_name not in ["check", "deposit", "withdraw"]:
                print("Programdan çıkılıyor.")
                trying_count = 0
                break
            else:
                print(currency_operations(user_name, operation_name))
    trying_count -= 1


#region First Solution:
# kullanici_adi = "adal"
# sifre = "1234"
# hak = 3
# bakiye = 0
# login_successful = False

# while hak >= 0:
#     if hak <= 0:
#         print("Hesabınız bloke edilmiştir.")
#         exit()
#     else:
#         username = input("İsminiz: ")
#         password = input("Şifreniz: ")
#         if username == kullanici_adi:
#             if password == sifre:
#                 print(f"Giriş başarılı, hoşgeldin {username}")
#                 while True:
#                     try:
#                         islem = int(input("Bakiye sorgulamak için 1\nPara yatırmak için 2\nPara çekmek için 3\nGüvenli çıkış için 4\nYapılması istenen işlemi giriniz = "))
#                         match islem:
#                             case 1:
#                                 print(f"Bakiyeniz = {bakiye}")
#                             case 2:
#                                 gelen_para = int(input("Yatırmak istenilen tutarı giriniz: "))
#                                 if gelen_para < 0:
#                                     print("Yatırılmak istenilen tutar geçerli değil.")
#                                 else:
#                                     bakiye += gelen_para
#                                     print(f"{gelen_para} hesabınıza yatırıldı, yeni tutar = {bakiye}")
#                             case 3:
#                                 giden_para = int(input("Çekilmek istenilen tutarı giriniz: "))
#                                 if giden_para > bakiye or giden_para < 0:
#                                     print("Çekilmek istenilen tutar geçerli değil.")
#                                 else:
#                                     bakiye -= giden_para
#                                     print(f"{giden_para} hesabınızdan çekildi, yeni tutar = {bakiye}")
#                             case 4:
#                                 print(f"Hoşçakal {username}!")
#                                 break
#                             case _:
#                                 print("Girilen işlem tanımlanamaz, tekrar deneyiniz.")
#                     except (TypeError, ValueError) as err:
#                         print(f"{err} hatası sebebiyle giriş kabul edilmedi, girişinizi kontrol ediniz.")
#             else:
#                 hak -= 1
#                 print(f"Giriş yanlış, kalan deneme hakkınız = {hak}")
#         else:
#             hak -= 1
#             print(f"Giriş yanlış, kalan deneme hakkınız = {hak}")
#endregion
