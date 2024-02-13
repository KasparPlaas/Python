# Kaspar Plaas
# 13.02.2024
from tkinter import *
import random


# Loo graafiliselt jĆ¤rgmised programmid (Tkinter). KĆ¼simused ja tulemused kuvatakse programmiaknas


# Aken

aken = Tk()
aken.title('Iseseisev_Tkinter')


# Ava aken, kus saab valida millise funktsiooni käivitab!
aken.geometry("320x420")
aken.resizable(0,0)
aken.option_add('*font', ('tahoma', 12))


tekst = Label(aken, text="Valige, millist programmi soovite kasutada!")
tekst.grid(row=0, column=1, padx=2, pady=2)




# Harjutus 1

def matemaatika():
    aken = Tk()
    aken.title('Matemaatika')


    # Ava aken, kus saab valida millise funktsiooni käivitab!
    aken.geometry("320x420")
    aken.resizable(0,0)
    aken.option_add('*font', ('tahoma', 12))


    tekst = Label(aken, text="Matemaatika!")
    tekst.grid(row=0, column=3, padx=2, pady=2)
    
    
    
    
    
    print("5 ülesannet")

    tehe = 0
    oiged = 0
    valed = 0

    for i in range(5):
        
        arv1 = random.randint(1,10)
        arv2 = random.randint(1,10)
        tehe += 1
        
        print("---- Ülesanne",tehe,"----")
        print("Kui palju on",arv1,"+",arv2,"?")
        sisestus = int(input("Vastus: "))
        if sisestus==arv1+arv2:
            print("Õige vastus!")
            oiged += 1
        else:
            print("Vale vastus!")
            valed +=1

    print("--------------")
    print("Õigesti vastasid",oiged,"!")
    print("Valesti vastasid",valed,"!")

#matemaatika()

# Harjutus 2

def romantika():
    
    armas = random.randint(0,100)
    
    nimi1 = str(input("Siseta esimene nimi!: "))
    nimi2 = str(input("Sisesta teine nimi!: "))
    print(nimi1,"ja",nimi2,"vahel on",armas,"% ""armastust")


#romantika()

# Harjutus 3




# Harjutus 4

def it_moisted():
    print("Kas oskad IT mõisteid?")
    
    moiste1 = "it"
    moiste2 = "son"
    
    print("1.",moiste1,"\n2.",moiste2)
    
    valik = int(input("Vali üks mõiste! Sisesta 1 või 2: "))
    if valik == 1:
        vastus = str(input("Sisesta 'IT' tähendus!: "))
        if vastus == "infotehnoloogia":
            print("Vastasite õigesti!")
        else:
            print("Vastasite valesti!")
            
    elif valik == 2:
        vastus = str(input("Sisestage 'SON' tähendus!: "))
        if vastus == "salvestamine on nõrkadele":
            print("Õige vastus!")
        else:
            print("Vale vastus!")
            
#it_moisted()

# Harjutus 5



# Harjutus 6

def arvamine():
    arvuti = random.randint(1,10)
    vastus = int(input("Arva ära arv vahemikus 1-10!"))
    if vastus == arvuti:
        print("Õige vastus!")
    else:
        print("Vale vastus!")
    
#arvamine()

# Harjutus 7

def valik():
    valik = str(input("Sisestage kalkulaatori valik: EUR -> EEK on EEK ja EEK -> EUR on EUR!: "))
    if valik == "EEK" or valik == "eek":
        krooni_kalkulaator()
    elif valik == "EUR" or valik == "eur":
        euro_kalkulaator()
    else:
        print("Sisestasite vale valiku!")
        print("Sisestage uuesti!!")
        valik()

def krooni_kalkulaator():
    eurod = float(input("Sisestage eurode arv: "))
    vastus = round(eurod * 15.6,2)
    print(eurod,"eurot on",vastus,"krooni!")

def euro_kalkulaator():
    kroonid = float(input("Sisestage kroonide arv: "))
    vastus = round(kroonid / 15.6,2)
    print(kroonid,"krooni on",vastus,"eurot!")
    
#valik()

# Harjutus 8

def taring():
    arvuti = random.randint(1,6)
    mangija = random.randint(1,6)
    print("Arvuti viskas", arvuti ,", sina said ",mangija,"!")
    if arvuti == mangija:
        print("viik")
    elif arvuti > mangija:
        print("Kaotasid")
    else:
        print("Võitsid")

#taring()

# Harjutus 9

def km():
    sisestus = str(input("Sisesta, kas soovid KM -> Miili on KM ja miilid -> KM on miilid!: "))
    if sisestus == "KM" or sisestus == "km":
        kilomeetrid()
    elif sisestus == "miilid" or siestus == "MIILID":
        miilid()
    else:
        print("Sisestasite valesti!")
        print("Proovige uuesti!")
        km()
        
        
def kilomeetrid():
    sisestus = int(input("Sisestage mitu KM soovite teisendada!: "))
    vastus = round(sisestus*0.621371,2)
    print(sisestus,"km on",vastus,"miili!")
    
def miilid():
    sisestus = int(input("Sisesta mitu miili soovite teisendada!: "))
    vastus = round(sisestus/0.621371,2)
    print(sisestus,"miili on",vastus,"km!")
    
#km()


# Harjutus 10
#10. Kontaktid - loo programm, mis küsib kasutajalt nime ja telefoninr ja lisab need tekstifaili.
def kontaktid():
    nimi = str(input("Sisestage oma nimi!: "))
    nr = int(input("Sisestage oma telefoni nr!: "))
    fail = open("kontaktid.txt","a")
    fail.write(nimi + " " + str(nr) + "\n")
    fail.close()


#kontaktid()


# Esimene akna valikud

nupp1 = Button(aken, text="Matemaatika", width=15, command=matemaatika)
nupp1.grid(row=1, column=1, padx=2, pady=2)



nupp2 = Button(aken, text="Romantika", width=15)
nupp2.grid(row=2, column=1, padx=2, pady=2)



nupp3 = Button(aken, text="Riigilipud", width=15)
nupp3.grid(row=3, column=1, padx=2, pady=2)



nupp4 = Button(aken, text="IT Mõisted", width=15)
nupp4.grid(row=4, column=1, padx=2, pady=2)



nupp5 = Button(aken, text="Riistvara", width=15)
nupp5.grid(row=5, column=1, padx=2, pady=2)



nupp6 = Button(aken, text="Arva ära", width=15)
nupp6.grid(row=6, column=1, padx=2, pady=2)



nupp7 = Button(aken, text="Euro kalkulaator", width=15)
nupp7.grid(row=7, column=1, padx=2, pady=2)



nupp8 = Button(aken, text="Täringud", width=15)
nupp8.grid(row=8, column=1, padx=2, pady=2)



nupp9 = Button(aken, text="Kilomeetrid", width=15)
nupp9.grid(row=9, column=1, padx=2, pady=2)



nupp10 = Button(aken, text="Kontaktid", width=15)
nupp10.grid(row=10, column=1, padx=2, pady=2)


aken.mainloop()