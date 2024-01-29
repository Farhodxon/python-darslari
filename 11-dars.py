# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 02:42:47 2024

@author: user
"""

yosh = int(input("Yoshingiz nechchida?"))
if yosh<=4:
    print("sizga kirish bepul.")
elif yosh<=12:
    print("Sizga kirish 5000 so'm.")
else:
    print("Sizga kirish 10000 so'm")
yosh = int(input("Yoshingiz nechchida?"))
if yosh <= 4:
    price = 0
elif yosh <=12:
    price = 5000
else:
    price = 10000
print(f"Sizga kirish {price} so'm")
yosh = int(input("Yoshingiz nechchida?"))
if yosh <= 4:
    price = 0
elif yosh <=12:
    price = 5000
elif yosh<65:
    price = 10000
else:
    price = 8000
print(f"Sizga kirish {price} so'm")
kun = input("Bugun nima kun?>>>")
if kun.lower() == 'shanba'  or kun.lower() == 'yakshanba':
    print("bugun dam olish kuni.")
else:
    print('bugun ish kuni.')
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower() == 'yakshanba'  and harorat >=30:
    print("Cho'milgani kettik.")
elif kun.lower() == 'yakshanba' and harorat.lower() <30:
    print("Uyda dam olamiz.")
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba')  and harorat >= 30:
    print("Cho'milgani kettik.")
elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
    print("uyda dam olamiz.")
narx = 15000
choy = True
salat = False
if choy and salat:
    narx = narx + 10000
elif choy or salat:
    narx = narx + 5000
print(f"Jami {narx} so'm")
narx = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False
if choy:
    print("Mijoz choy oldi.")
    narx = narx + 3000
if salat:
    print("Mijoz salat oldi.")
    narx = narx +5000
if non:
    print("Mijoz non oldi.")
    narx = narx + 2000
if kompot:
    print("Mijoz kompot oldi.")
    narx = narx + 5000
if assorti:
    print("Mijoz assorti oldi.")
    narx = narx + 15000
print(f"Jami {narx} so'm")
menu = ['osh', 'qozonkabob', 'manti', 'shashlik', 'norin', 'somsa']
menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input("Nima ovqat yeysiz?")
if ovqat.lower() in menu:
    print("Buyurtma qabul qilindi")
else:
    print('Afsuski bizda bunday ovqat yo\'q')
menu = ['osh','qazonkabob','shashlik','norin','somsa']
ovqat = input("Nima ovqat yeysiz?")
if ovqat.lower() not in menu:
    print("Afsuski bizda bunday ovqat yo'q.")
else:
    print("Buyurtma qabul qilindi.")
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]
for taom in buyurtmalar:
    if taom in menu:
        print(f"menuda {taom} bor.")
    else:
        print(f"Kechirasiz menuda {taom} yo'q.")
menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"menuda {taom} bor.")
        else:
            print(f"Kechirasiz menuda {taom} yo'q.")
else:
    print("Savatchangiz bo'sh!")
#  Amaliyot
son = int(input("Juft son kiriting:"))
if son%2:
    print("Bu juft son emas.") 
else:
    print("Raxmat!")            
yosh = int(input('Yoshingiz nechchida?>>>'))
if yosh <= 4 or yosh >= 60:
    price = 0
elif yosh < 18:
    price = 10000
else:
    price = 20000
print(f"Sizga kirish {price} so'm")
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print(f"{x}={y}")
elif x<y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")
mahsulotlar = ['olma', 'anor', 'anjir', 'xurmo', 'nok', 'qulupnay', 'shaftoli', 'gilos', 'banan', 'ananas']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing:"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Do'konomizda {mahsulot} bor.")
    else:
        print(f"Do'konimizda {mahsulot} yo'q.")
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
  print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
  for mahsulot in mavjud_emas:
    print(mahsulot)
else:
  print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
users = ['alisher','aziza','yasina','umar']

login = input("Yangi login tanlang: ")

if login in users:
    print('Login band, yangi login tanlang!')
else:
    print(f"Xush kelibsiz, {login.title()}!")
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")