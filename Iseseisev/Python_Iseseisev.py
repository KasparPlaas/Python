import math
import random

# 1. Korrutamise kontrollimine
'''
def korrutamine():
    kord = 0
    while kord < 10:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        arva = int(input("Mis on " + str(num1) + "x" + str(num2) + "?: "))
        vastus = int(num1*num2)
        oige = arva == vastus
        if arva == vastus:
            print("Õige vastus!")
        else:
            print ("Kahjuks oli see vale vastus, õige vastus on ",vastus,)
        
korrutamine()
'''

# 2. Vanused
'''
vanused = [10,60,40,30,20,25,35]

def vanuste_stat(vanused):
    print(max(vanused))
    print(min(vanused))
    print(sum(vanused))
    average=float(sum(vanused))/float(len(vanused))
    print(round(average))

vanuste_stat(vanused)
'''

# 3. Positiivsed ja negatiivsed
'''
pos = [1,2,3,4,5]
neg = [-1,-2,-3,-4,-5]

def pos_neg():
    for i in range(5):
        num = int(input("Sisesta arv: "))
        if num > 0:
            pos.append(num)
        elif num < 0:
            neg.append(num)
        else:
            print("Nulli ei lisata")
    print(pos)
    print(neg)
pos_neg()
'''

# 4. List less than ten
'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def vaiksem_kui_viis(a):
    uus_list = []
    for i in a: uus_list.append(i) if i < 10 else None
    print(uus_list)
print(a)
lisa = int(input("Sisesta arv, mida soovite lisada tabelisse: "))
a.append(lisa)
vaiksem_kui_viis(a)
'''

# 5. Shopping list
'''
poe_list = []
def poe_listi():
    while True:
        toode = input("Sisesta toode: ")
        print("Kui soovite lõpetada, vajutage enterit.")
        if toode == "":
            break
        else:
            poe_list.append(toode)
    print(poe_list)
poe_listi()

'''

# 6. paaris või paaritu
'''

# def paaris_paaritu():
#     print("Kas teie sisestatud arv on paaris või paaritu?")
#     arv = input("Sisesta arv: ")
#     if arv == "":
#         print("Te ei sisestanud midagi")
#     elif int(arv) == 0:
#         print("Null on paaris arv")
#     elif int(arv) % 2 == 0:
#         print("Arv on paaris")
#     else:
#         print("Arv on paaritu")
# paaris_paaritu()
'''

# 7. Eurokalkulaator

'''
# def Eurokalkulaator():
#     print("Tere tulemast eurokalkulaatorisse!")
#     print("Kas soovite teisendada EUR->EEK siis EUR või EEK->EUR siis EEK?")
#     valik = input("Sisestage oma valik : ")
#     if valik == "EUR":
#         summa = int(input("Sisestage summa eurodes: "))
#         print(summa*15.6466)
#     elif valik == "EEK":
#         summa = int(input("Sisestage summa kroonides: "))
#         print(summa/15.6466)
#     else:
#         print("Vale valik!")
#         Eurokalkulaator()
# Eurokalkulaator()
'''

# 8.Täringu mäng
'''
def taringumang():
    print("Tere tulemast täringumängu!")
    panus = int(input("Palun sisestage oma panus: "))
    print("Teie panus on ", panus, " eurot")
    print("arvuti viskab täringuid...")
    ab = random.randint(1,6)
    ac = random.randint(1,6)
    taring = ab+ac
    vastus = int(input("Arvake ära mitu tärni arvuti viskas: "))
    raha = panus*2
    if taring==vastus:
        print("Teie võitsite! Te võitsite ", raha, " eurot")
    else:
        print("Arvuti võitis, õige vastus oli", taring, "! Te kaotasite ", panus, " eurot")

taringumang()
'''

# 9. emaili kontroll

'''
def email():
    email = input("Sisesta email: ")
    if "@" in email:
        print("Tere " + email.split("@")[0].split(".")[0] + ", sinu email on serveris " + email.split("@")[1].split(".")[0] + " ja domeeniks on sul " + email.split("@")[1].split(".")[1])
    else:
        print("Vale email!")
email()
'''

# 10. kaugushüpe

'''
# def kaugushupe():
#     tulemused = []
#     for i in range(3):
#         tulemus = float(input("Sisesta kaugushüppe tulemus: "))
#         tulemused.append(tulemus)
#     print("Parim tulemus on ", max(tulemused), "m")
#     print("Keskmine tulemus on ", sum(tulemused)/len(tulemused), "m")
# kaugushupe()
'''

# 11. Salakeel
# 	sinu programm küsib kasutajalt, kas ta soovib salakeelt luua või tõlkida - 1p
# 	kasutaja sisestab tavalise sĆµna, mis muudetakse salakeeleks - 1p
# 	kasutaja sisestab salakeeles sõna, mis teisendatakse jälle normaalseks - 1p
# 	kood kommenteeritud - 1p

def salakeel():
    print("Kas soovite salakeelt luua või tõlkida?")
    valik = input("Sisestage oma valik: ")
    if valik == "luua":
        sona = input("Sisestage sõna, mida soovite salakeelde muuta: ")
        print(sona)
    elif valik == "tolkida":
        sona = input("Sisestage sõna, mida soovite tõlkida: ")
        print(sona)
    else:
        print("Vale valik!")
        salakeel()
salakeel()
        