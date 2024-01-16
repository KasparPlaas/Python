# Kaspar Plaas
# IT23
# 10.01.2023

import random
import datetime 


'''

#rebased

fail = open("rebased.txt", encoding="UTF-8")

vastuvoetud = []

for rida in fail:

    vastuvoetud.append(int(rida))

aasta = 2011
print(f"Aastal {aasta} võeti vastu {vastuvoetud[aasta-2011]} õpilast")
fail.close()


#konto.txt

fail = open("konto.txt", encoding="UTF-8")
for rida in fail:
    if float(rida) > 0:
        print(float(rida))
    
fail.close()
'''


'''
# jukebox
failinimi = input("Palun sisestage faili nimi: ")
fail = open(failinimi, encoding="utf-8")
nr = 1
for rida in fail:
    print(f"{nr}. {rida}",end="")
    nr+=1

fail.seek(0)
nr = 1
jrk = int(input("\nValige laulu järjekorranumber: "))
for rida in fail:
    if nr==jrk:
        print(f"Mängitav muusikapala on: {rida}.")
    nr+=1
fail.close()

'''

#nimekiri

fail = open("nimekiri.txt", encoding="utf-8")

p = (datetime.datetime.now().day)

nr = 1
for rida in fail:
    if nr==p:
        print(f"Tahvli ette tuleb: {rida}.")
    nr+=1
    
fail.close()