# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 00:41:23 2024

@author: user
"""

mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(mehmon)
    print(f"Hurmatli {mehmon}, sizni 5-avgust kuni nahorga oshga taklif qilamiz.")
    print("Hurmat bilan Polotovlar oilasi")
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son}ning kvadrati {son**2} ga teng ")
sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)
dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)
# Amaliyot
ismlar =  ["Ali", "Vali", "G'ani", "Lali", "Lili"] 
for ism in ismlar:
    print(f"Salom {ism}")
print("Kod 5 marta takrorlandi.")
sonlar = list(range(11,100,2))
for son in sonlar:
    print(son**3)
kinolar = []
print("5 ta sevimli kinoyingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino:"))
print(kinolar)
n_people = int(input("Bugun nechta odam bilan suhbat qildingiz:?>>>"))
ismlar  = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)