# import math
# import random

# # 1. Korrutamise kontrollimine

# # def korrutamine():
# #     kord = 0
# #     while kord < 10:
# #         num1 = random.randint(1,10)
# #         num2 = random.randint(1,10)
# #         arva = int(input("Mis on " + str(num1) + "x" + str(num2) + "?: "))
# #         vastus = int(num1*num2)
# #         oige = arva == vastus
# #         if arva == vastus:
# #             print("Õige vastus!")
# #         else:
# #             print ("Kahjuks oli see vale vastus, õige vastus on ",vastus,)
        
# # korrutamine()


# # 2. Vanused

# # vanused = [10,60,40,30,20,25,35]

# # def vanuste_stat(vanused):
# #     print(max(vanused))
# #     print(min(vanused))
# #     print(sum(vanused))
# #     average=float(sum(vanused))/float(len(vanused))
# #     print(round(average))

# # vanuste_stat(vanused)


# # 3. Positiivsed ja negatiivsed

# pos = [1,2,3,4,5]
# neg = [-1,-2,-3,-4,-5]

# def pos_neg():
#     for i in range(5):
#         num = int(input("Sisesta arv: "))
#         if num > 0:
#             pos.append(num)
#         elif num < 0:
#             neg.append(num)
#         else:
#             print("Nulli ei lisata")
#     print(pos)
#     print(neg)
# pos_neg()


# # 4. List less than ten


# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# def vaiksem_kui_viis(a):
#     uus_list = []
#     for i in a: uus_list.append(i) if i < 10 else None
#     print(uus_list)
# print(a)
# lisa = int(input("Sisesta arv, mida soovite lisada tabelisse: "))
# a.append(lisa)
# vaiksem_kui_viis(a)


# # 5. Shopping list

# poe_list = []
# def poe_listi():
#     while True:
#         toode = input("Sisesta toode: ")
#         print("Kui soovite lõpetada, vajutage enterit.")
#         if toode == "":
#             break
#         else:
#             poe_list.append(toode)
#     print(poe_list)
# poe_listi()



# # 6. paaris või paaritu


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


# # 7. Eurokalkulaator


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


# # 8.Täringu mäng

# def taringumang():
#     print("Tere tulemast täringumängu!")
#     panus = int(input("Palun sisestage oma panus: "))
#     print("Teie panus on ", panus, " eurot")
#     print("arvuti viskab täringuid...")
#     ab = random.randint(1,6)
#     ac = random.randint(1,6)
#     taring = ab+ac
#     vastus = int(input("Arvake ära mitu tärni arvuti viskas: "))
#     raha = panus*2
#     if taring==vastus:
#         print("Teie võitsite! Te võitsite ", raha, " eurot")
#     else:
#         print("Arvuti võitis, õige vastus oli", taring, "! Te kaotasite ", panus, " eurot")

# taringumang()


# # 9. emaili kontroll


# def email():
#     email = input("Sisesta email: ")
#     if "@" in email:
#         print("Tere " + email.split("@")[0].split(".")[0] + ", sinu email on serveris " + email.split("@")[1].split(".")[0] + " ja domeeniks on sul " + email.split("@")[1].split(".")[1])
#     else:
#         print("Vale email!")
# email()


# # 10. kaugushüpe


# def kaugushupe():
#     tulemused = []
#     for i in range(3):
#         tulemus = float(input("Sisesta kaugushüppe tulemus: "))
#         tulemused.append(tulemus)
#     print("Parim tulemus on ", max(tulemused), "m")
#     print("Keskmine tulemus on ", sum(tulemused)/len(tulemused), "m")
# kaugushupe()


# # 11. Salakeel

# def salakeel():
#     keel = {"a": "e", "b": "t", "c": "u", "d": "i", "e": "o", "f": "a", "g": "s", "h": "d", "i": "h", "j": "n", "k": "r", "l": "k", "m": "m", "n": "l", "o": "j", "p": "v", "q": "p", "r": "y", "s": "õ", "t": "ä", "u": "f", "v": "g", "w": "b", "x": "c", "y": "ü", "z": "ö", "õ": "x", "ä": "z", "ö": "q", "ü": "w"}
#     print("Kas soovite salakeelt luua või tõlkida?")
#     valik = input("Sisestage oma valik: ")
#     if valik == "luua":
#         sona = input("Sisestage sõna, mida soovite salakeelde tõlkida: ")
#         salasona = ""
#         for i in sona:
#             salasona += keel[i]
#         print(salasona)
#     elif valik == "tõlkida":
#         salasona = input("Sisestage sõna, mida soovite salakeelest tõlkida: ")
#         sona = ""
#         for i in salasona:
#             for key, value in keel.items():
#                 if value == i:
#                     sona += key
#         print(sona)
#     else:
#         print("Vale valik!")
# salakeel()



# # 12. Eurokalkulaator

# def eur_eek():
#     summa = int(input("Sisestage summa eurodes: "))
#     print(summa*15.6466, "krooni")
# def eek_eur():
#     summa = int(input("Sisestage summa kroonides: "))
#     print(summa/15.6466, "eur")

# valik = input("Kas soovite teisendada Eurosid[EUR] või Kroone[EEK]: ")
# if valik == "EUR":
#     eur_eek()
# elif valik == "EEK":
#     eek_eur()
# else:    
#     print("Vale valik!")


# # 13. paaris või paaritu

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


# # 14. Palkade võrdlus

# def palgad():
#     fail = open("palk.txt", encoding="UTF-8")
#     mehed = []
#     naised = []
#     for rida in fail:
#         osad = rida.split()
#         if osad[2] == "m":
#             mehed.append(int(osad[3]))
#         else:
#             naised.append(int(osad[3]))
#     fail.close()
#     meeste_keskmine = sum(mehed)/len(mehed)
#     meeste_max = max(mehed)
#     naiste_keskmine = sum(naised)/len(naised)
#     naiste_max = max(naised)
#     print("Meeste keskmine palk on", meeste_keskmine)
#     print("Naiste keskmine palk on", naiste_keskmine)
#     print("Meeste kõrgeim palk on", meeste_max)
#     print("Naiste kõrgeim palk on", naiste_max)
#     if meeste_keskmine > naiste_keskmine and meeste_max > naiste_max:
#         print("Firmas toimub diskrimineerimist soo järgi")
#     else:
#         print("Firmas ei toimu diskrimineerimist soo järgi")

# palgad()


# # 15. temperatuurid

# temperatuurid = [
#     [-16, -12, -15, -20, 0, -1, -20, -2, -20, -14, -18, -8, 2, -1, -14, -7, -15, -17, -6, -17, -17, -7, 0, 3, -20, -17, -15, -8, -12, 3],
#     [-9, -2, -7, 1, -16, -19, -19, -11, -16, -15, -9, -2, -16, -4, -20, -5, -6, -17, -5, 0, -16, 2, 0, -20, -16, -2, -18],
#     [2, -9, -1, -3, -6, -2, 1, -2, -3, -9, -1, -4, 0, -6, -7, 1, 0, 2, -5, -10, 2, -7, -3, 2, -10, 2, -9, -8, -5, -2],
#     [-5, 0, 10, -9, 0, -9, -8, 6, -5, 3, -1, 4, 9, -1, 2, 0, 10, 0, 5, 0, -10, 0, 6, 3, -6, -2, -10, -8, -2],
#     [12, 5, 8, -1, -2, 4, 10, -1, 7, 15, 7, 3, 6, 4, 10, 9, 13, 6, 14, 10, 14, 2, 6, 12, 15, 2, 14, 11, 9, 1],
#     [12, 5, 17, 6, 10, 14, 9, 7, 15, 23, 29, 11, 16, 18, 9, 25, 14, 8, 16, 22, 19, 22, 23, 18, 16, 16, 26, 24, 22],
#     [15, 8, 21, 28, 18, 13, 9, 9, 8, 6, 8, 12, 12, 29, 28, 20, 6, 9, 12, 8, 14, 18, 14, 13, 23, 6, 24, 24, 17, 20],
#     [7, 6, 5, 19, 18, 18, 17, 20, 15, 11, 7, 10, 13, 12, 20, 11, 10, 14, 18, 14, 24, 6, 17, 16, 6, 17, 5, 13, 11],
#     [21, 19, 21, 9, 13, 18, 6, 6, 20, 7, 25, 13, 8, 9, 14, 16, 19, 10, 7, 25, 7, 17, 16, 15, 17, 18, 15, 9, 19],
#     [2, 2, 1, 5, -2, 5, 5, 2, 2, 2, 1, -2, 1, -2, 0, -2, 5, 4, 0, 1, -1, 2, 0, 2, 2, 2, -1, 1, 4, -1],
#     [-6, -7, -2, -7, -2, -4, 0, -7, -8, -6, 0, -9, -2, -3, -2, 0, -8, -2, -5, -2, -5, -8, -10, 0, -2, -9, -9, -7, -1]
# ]
# kuud = ['jaanuar', 'veebruar', 'märts', 'aprill', 'mai', 'juuni', 'juuli', 'august', 'september', 'oktoober', 'november']

# def koige_soojem(temperatuurid, kuud):
#     temp = 0
#     kuu = ""
#     paev = 0
#     for i in range(len(temperatuurid)):
#         if max(temperatuurid[i]) > temp:
#             temp = max(temperatuurid[i])
#             kuu = kuud[i]
#             paev = temperatuurid[i].index(max(temperatuurid[i])) + 1
#     print("Kõige soojem päev oli", kuu, paev, ". päeval. Temperatuur oli", temp, "kraadi.")
# koige_soojem(temperatuurid, kuud)

# # 16. Täringud

# def taringu_mang():
#     raha = 100
#     arvuti_raha = 100
#     nimi = input("Sisesta oma nimi: ")
#     print("Tere", nimi, "!")
#     print("Sul on 100€ ja arvutil on 100€.")
#     while raha > 0 and arvuti_raha > 0:
#         print("Sul on", raha, "€ ja arvutil on", arvuti_raha, "€.")
#         panus = int(input("Sisesta panus: "))
#         if panus > raha:
#             print("Sul ei ole nii palju raha!")
#             continue
#         enter = input("Vajuta enterit, et täringuid veeretada.")
#         taring = random.randint(1,6)
#         print("Sul tuli", taring, "silma.")
#         arvuti_taring = random.randint(1,6)
#         print("Arvutil tuli", arvuti_taring, "silma.")
#         if taring > arvuti_taring:
#             print("Sina võitsid!")
#             raha += panus
#             arvuti_raha -= panus
#         elif taring < arvuti_taring:
#             print("Arvuti võitis!")
#             raha -= panus
#             arvuti_raha += panus
#         else:
#             print("Viik!")
# taringu_mang()


# # 17. Email

# def email():
#     email = input("Sisesta email: ")
#     if "@" in email:
#         print("Tere " + email.split("@")[0].split(".")[0] + ", sinu email on serveris " + email.split("@")[1].split(".")[0] + " ja domeeniks on sul " + email.split("@")[1].split(".")[1])
#     else:
#         print("Vale email!")
# email()
