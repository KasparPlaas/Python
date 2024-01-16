#Kaspar Plaas
# 10.01.2024

import math

'''
# Banner

def banner():
    print("\'Osta ja Sa ei kahetse!'".upper())
banner()

def banner2(tekst):
    print(tekst)

kord = int(input("Mitu korda soovite reklaamlauset kuvada? "))
tekst = input("Sisestage reklaamlause: ").upper()
for i in range(kord):
    banner2(tekst)

'''


'''
# Mahlapakid

def mahlapakkide_arv(kg):
    mahlapakk = round(kg*0.4/3)
    return mahlapakk

kogus = float(input("Sisestage õunte kogus kilogrammides: "))
mahlapakkide_arv(kogus)
print(mahlapakkide_arv(kogus))
'''

'''

# Eelarve

def eelarve(arv):
    kogusumma = arv * 10 + 55
    return kogusumma


kutsutud = int(input("mitu inimest on kutsutud?: "))
tuleb = int(input("Mitu inimest tuleb?: "))


print(f"Maksimaalne eelarve: {eelarve(kutsutud)} eurot ")
print(f"Minimaalne eelarve: {eelarve(tuleb)} eurot ")

'''


'''
# Tervitus
def tervitus(jrk):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {jrk}. kord tervitada, mõtiskleb võõrustaja.")
    print('külaline: "Tere, suur tänu kutse eest!')

kylaliste_arv = int(input("Mitu inimest on kutsutud:"))
for i in range(kylaliste_arv):
    tervitus(i+1)

    
'''



def pronksikarva_summa():
   pass

kassa = 0
failinimi = input("Palun sisestage faili nimi: ")
fail = open(failinimi)
for nr in fail:
    if int(nr)<=10:
        kassa+=int(nr)

print(kassa)



