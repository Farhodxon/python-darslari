# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 01:32:34 2024

@author: user
"""

avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())
ism = input("Ismingiz nima?\n>>>")
if ism.lower() != 'ali':
    print(f"Uzr,  {ism.title()} biz Alini kutyapmiz")
else:
    print("Salom, Ali")
javob = float(input("12x6 nechiga teng?>>>"))
if javob != 72:
    print("Javob xato")
yosh = int(input("Yoshingiz nechchida?>>>"))
if yosh >= 18:
    print("Xush kelibsiz")
else:
    print("Kirish mumkin emas!")
login = input("Yangi login tanlang:")
if len(login)<=5:
    print("Login 5  harfdan ko'p bo'lishi shart.")
yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2023-yil<18:
    print(f"Yoshingiz {2023-yil} da ekan.")
    print("Kirish mumkin emas!")
else:
    print("Xush kelibsiz.")
yosh = int(input("Yoshingiz nechchida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")
# Amaliyot
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == "gm":
        print(car.upper())
    else:
        print(car.title())
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != "gm":
        print(car.title())
    else:
        print(car.upper())
login = input("Loginni kiriting?>>>")
if login.lower() == 'admin':
    print("Xush kelibsiz Admin, foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    print("Xush kelibsiz {login.title()}")
x = float(input("Birinchi sonni kiriting:"))
y = float(input("Ikkinchi sonni kiriting:"))
if x == y:
    print("Sonlar teng: {x}={y}")
x = float(input("Istalgan sonni kiriting:>>>"))
if x < 0:
    print("manfiy son")
else:
    print("musbat son")
son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')