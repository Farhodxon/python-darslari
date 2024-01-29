# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 06:43:13 2024

@author: user
"""

cars = ["bmw", "nercedes benz", "volvo", "general motors", "tesla", "audi"]
cars.sort()
print(cars)
cars = ["bmw", "nercedes benz", "volvo", "general motors", "tesla", "audi"]
cars.sort(reverse = True)
print(cars)
mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
print("sorted() qaytargan ro'yxat: ", sorted(mehmonlar))
print("Asl ro'yxat: ", mehmonlar)
print(sorted(mehmonlar, reverse=True))
ages = [12, 98, 34, 65, 34, 76, 11]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))
fruits = ['pear','banana','apple','watermelon','lemon']
fruits.reverse()
print(fruits)
fruits = ['pear','banana','apple','watermelon','lemon']
print("Elementlar soni: ", len(fruits))
sonlar = list(range(0,10))
print(sonlar)
juft_sonlar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narx ", arzon, "eng qimmat narx ", qimmat, "Jami: ", jami)
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3]
print(my_cars)
print(cars[2:5])
print(cars[:4])
print(cars[2:])
sonlar = [1, 2, 3, 4, 5]
sonlar2 = sonlar
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati: ", sonlar)
print("Bu sonlar ro'yxati: ", sonlar2)
sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'yxati:", sonlar2)
tomonlar = (20, 30, 55.2)
print(tomonlar)
toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-1])
print(toys[2:5])
toys = ('bus','car','bear','dino','snake','lizard')
toys = list(toys)
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys)
print(toys)
# Amaliyot
davlatlar = ['Aqsh', 'Angliya', 'Rossiya', 'Xitoy', "Yaponiya", 'Janubiy Koreya']
print(davlatlar)
print("Ro'yxat uzunligi: ", len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
sonlar = list(range(120,1200,2))
print(sum(sonlar))
print(max(sonlar) - min(sonlar))
print(len(sonlar))
taomlar = ['osh','somsa','norin','shashlik','qozonkabob']
nonushta = taomlar[:]
nonushta.remove('norin')
nonushta.remove('shashlik')
nonushta.remove('qozonkabob')
nonushta.append('non va qaymoq')
nonushta.append('issiq non')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = "non va qaymoq"