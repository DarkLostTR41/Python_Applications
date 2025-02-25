def topla():
    return say_1 + say_2
def cikar():
    return say_1 - say_2
def carp():
    return say_1 * say_2
def bol():
    return say_1 / say_2

say_1 = float(input("Birinci sayıyı giriniz:"))
say_2 = float(input("İkinci sayıyı giriniz:"))

islem = input("Yapmak istediğiniz işlemi seçiniz? \n 1-Topla \n 2-Çıkar \n 3-Çarp \n 4-Böl")
if ( islem == "1"):
    result = topla()
    
elif (islem == "2"):
    result = cikar()
elif ( islem == "3"):
    result = carp()
elif ( islem == "4"):
    result = bol()
else:
    print("Hatalı işlem seçimi !")    
print(result)