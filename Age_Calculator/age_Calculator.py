from datetime import datetime

def age_calculator(birth_date):
    today = datetime.now()
    birth_date = datetime.strptime(birth_date,"%d/%m/%Y")
    age = today.year - birth_date.year
    
    if today.month< birth_date.month or (today.month == birth_date.month and today.day< birth_date.day):
        age -= 1
    return age

birth_date = input("Doğum tarihinizi gün/ay/yıl formtında giriniz: \n")
age = age_calculator(birth_date)
print(f"yaşınız : {age}")