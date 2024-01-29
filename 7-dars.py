# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 01:50:15 2024

@author: user
"""

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
narxlar = [12000, 18000, 10900, 22000]
sonlar = ['bir', 'ikki', 3, 4 , 5]
ismlar = []
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
print("birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())
print(narxlar[2] + narxlar[3])
car_models = ["Toyota", "GM", "Volvo", "BMW", "Hyundai", "Kia", "Volkswagen"]
print(car_models)
narxlar[0] = 13000
narxlar[2] = 11000
narxlar[3] = narxlar[3]+2000
print(narxlar)
mevalar.append("tarvuz")
print(mevalar)
cars = []
cars.append("Lacetti")
cars.append("Nexia 3")
cars.append("Cobalt")
print(cars)
cars.insert(0, "Malibu")
print(cars)
cars.insert(2, "Damas")
print(cars)
del mevalar[1]
print(mevalar)
mevalar.remove("shaftoli")
print(mevalar)
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk")
print(hayvonlar)
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan bozorliklar: ", bozorlik)
# Amaliyot
ismlar = ["Madaminxon", "Bekzod", "Farhodxo'ja"]
print("Salom ", ismlar[0], "bugun choyxona bormi?")
print(ismlar[1], "choyxonaga borasanmi?")
sonlar = [10, 15, -25, 40, 55, 70]
print(sonlar)
sonlar[0] = sonlar[0] + sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)
t_shaxslar = ["Amir Temur", "Adolf Gitler", "Muxammad al-Xorazmiy"]
z_shaxslar = ["Bill Geyts", "Ilon Mask", "Vladimir Putin"]
print(f" Men tarixiy shaxslardan {t_shaxslar.pop(0)}, bilan, Zamonaviy shaxslardan esa {z_shaxslar.pop(2)}, bulan suhbatlashishni xohlayman" )
friends = []
friends.append("Bekzod")
friends.append("Ali")
friends.append("Vali")
friends.append("G'ani")
friends.append("Olim")
print(friends)
friends.remove("Ali")
print(friends)
friends.insert(0, "Sohib")
friends.insert(2, "Alibek")
friends.insert(-1, "Ulug'bek")
print(friends)
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(-1))
print(f"Kelgan mehmonlar:", mehmonlar)