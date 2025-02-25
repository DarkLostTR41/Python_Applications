def menu():
    global k_username,k_password
    islem1 = int(input("1- Giriş Yap \n2-kayıt Ol\n"))
    if islem1 == 1:
        l_username = input("Kullanıcı adınız giriniz:")
        l_password = input("şifrenizi giriniz:")
        if k_username == l_username:
            if k_password == l_password:
                print("Giriş başarılı, Hoşgeldiniz!")
            else:
                print("Hatalı şifre!!!")
        else:
            print("Hatalı kullanıcı adı!!!")

    elif islem1 == 2:
        k_username = input("kullanıcı adınızı giriniz: ")
        k_password = input("Şifre giriniz:")
        print("Kayıt başarılı!")
        return menu()
    else: 
        print("Hatalı Tuşlama!")
        return menu()
    
k_username = ""
k_password = ""
menu()