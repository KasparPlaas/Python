# Kaspar Plaas
# IT23
# 18.12.2023
import winsound
import random

def alarm(k):
    for i in range(k):
        winsound.Beep(3000, 1000)
        print("Tõuse ja sära!")
        
def jankud(r)
    joostud_ringid = 0
    porgandid = 0
    while joonstud_ringid < r:
        joostud_ring+=1
        if joostud_ring%2 == 0:
            porgandid+=joostud_ring
    print(f"Porgandite arv on {porgandid}")


def taring(t):
    for i in range(t):
        print(random.randint(1,6))


def male(arv):
    ruut = 1
    nisutera = 1
    while ruut < arv:
        nisutera*=2
        ruut+=1
    print(nisutera)
    
male(4)


def lumi(p):
    ounad = 14
    for i in range(p):
        oun = random.randint(1,2)
        ounad-=oun
        print(oun)
        
    print(f"lumivalgekesele jäi {ounad} õuna")





'''
lumi(6)
taring(5)
jankud(6) 
korda = int(input("Mitu korda äratada?: "))
alarm(korda)
'''