# Kaspar Plaas
# 13.02.2024
from tkinter import *
import random

# Harjutus 1

def matemaatika_programm():
    
    aken = Tk()
    aken.title('Matemaatika')
    aken.geometry("250x180")
    aken.resizable(0, 0)
    aken.option_add('*font', ('tahoma', 12))
    
    oige = 0
    vale = 0
    
    def matemaatika(oige=oige, vale=vale):
        
        arv1 = random.randint(1, 10)
        arv2 = random.randint(1, 10)
        vastus = arv1 + arv2
        
        vastuse_sisestus = Label(aken, text="Sisesta vastus:")
        vastuse_sisestus.grid(row=0, column=0, padx=1, pady=1, sticky=W)
        
        tehte_kuvamine = Label(aken, text=str(arv1) + " + " + str(arv2) + " = ")
        tehte_kuvamine.grid(row=1, column=0, padx=1, pady=1, sticky=W)
        
        sisestus = Entry(aken, width= 5)
        sisestus.grid(row=1, column=1, padx=1, pady=1, sticky=W)
        
        oige_tekst = Label(aken, text="Õigeid vastuseid: " + str(oige))
        oige_tekst.grid(row=4, column=0, padx=1, pady=1, sticky=W)
        
        vale_tekst = Label(aken, text="Valesid vastuseid: " + str(vale))
        vale_tekst.grid(row=5, column=0, padx=1, pady=1, sticky=W)
        
        def tehe(oige=oige, vale=vale):
            kasti_sisestus = int(sisestus.get())
            
            if kasti_sisestus == vastus:
                vastus1 = Label(aken, text="Õige vastus!")
                vastus1.grid(row=3, column=1, padx=1, pady=1, sticky=W)
                
                oige += 1
                oige_tekst.config(text="Õigeid vastuseid: " + str(oige))
                
            else:
                vastus2 = Label(aken, text="Vale vastus!")
                vastus2.grid(row=3, column=1, padx=1, pady=1, sticky=W)
                
                vale += 1
                vale_tekst.config(text="Valesid vastuseid: " + str(vale))
            
            matemaatika(oige, vale)
        
        nupp = Button(aken, text="OK", command=tehe)
        nupp.grid(row=2, column=1, padx=1, pady=1, sticky=W)
    
    matemaatika()
    
    aken.mainloop()

# Harjutus 2

def romantika():
    aken = Tk()
    aken.title('Matemaatika')
    aken.geometry("400x300")
    aken.resizable(0, 0)
    aken.option_add('*font', ('tahoma', 12))
    
    pealkiri = Label(aken, text="Romantika")
    pealkiri.pack(pady=10)
    
    tekst_nimi1 = Label(aken, text="Sisesta esimene nimi:")
    tekst_nimi1.pack(pady=5)
    
    sisestus1 = Entry(aken, width=10)
    sisestus1.pack(pady=5)
    
    tekst_nimi2 = Label(aken, text="Sisesta teine nimi:")
    tekst_nimi2.pack(pady=5)
    
    sisestus2 = Entry(aken, width=10)
    sisestus2.pack(pady=5)

    vastus = Label(aken, text="")
    vastus.pack(pady=10)

    def arvutus():
        nimi1 = str(sisestus1.get())
        nimi2 = str(sisestus2.get())
        
        armas = random.randint(0, 100)
        vastus.config(text=str(nimi1) + " ja " + str(nimi2) + " vahel on " + str(armas) + "% armastust!")

    ok_nupp = Button(aken, text="OK", command=arvutus)
    ok_nupp.pack(pady=10)

# Harjutus 3

# KUNAGI TULEB :)


# Harjutus 4

def it_moisted():
    aken = Tk()
    aken.title('Matemaatika')
    aken.geometry("400x300")
    aken.resizable(0, 0)
    aken.option_add('*font', ('tahoma', 12))
    
    pealkiri = Label(aken, text="IT Mõisted")
    pealkiri.pack(pady=10)
    
    
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

def kontaktid():
    nimi = str(input("Sisestage oma nimi!: "))
    nr = int(input("Sisestage oma telefoni nr!: "))
    fail = open("kontaktid.txt","a")
    fail.write(nimi + " " + str(nr) + "\n")
    fail.close()


def pea():
    aken = Tk()
    aken.title('Iseseisev_Tkinter')

    aken.geometry("320x420")
    aken.resizable(0,0)
    aken.option_add('*font', ('tahoma', 12))

    tekst = Label(aken, text="Valige, millist programmi soovite kasutada!")
    tekst.grid(row=0, column=1, padx=2, pady=2)

    nupp1 = Button(aken, text="Matemaatika", width=15, command=matemaatika_programm)
    nupp1.grid(row=1, column=1, padx=2, pady=2)



    nupp2 = Button(aken, text="Romantika", width=15, command=romantika)
    nupp2.grid(row=2, column=1, padx=2, pady=2)



    nupp3 = Button(aken, text="Riigilipud", width=15)
    nupp3.grid(row=3, column=1, padx=2, pady=2)



    nupp4 = Button(aken, text="IT Mõisted", width=15, command= it_moisted)
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
pea()