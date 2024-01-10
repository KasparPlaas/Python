# Kaspar Plaas
# IT23
# 18.12.2023


# 1.1
def tervita():
    print ("Tere, maailm!")

# 1.2
def liblikas():
    aasta = 2020
    liblikas = "teelehe-mosaiikliblikas"
    lause_keskosa = ". aasta liblikas on"
    lause = str(aasta) + lause_keskosa + liblikas
    print(lause)

# 1.3
def pilved(A):
    if A >= 6:
        print("Need on ülemised pilved")
    else:
        print("Need ei ole ülemised pilved")

# 1.4
def BussideArv(i, k):
    bussid = i % k
    if i == k:
        bussid = i // k
        viimases = i
    elif bussid > 0:
        bussid = bussid = i // k + 1
        viimases = i % k
    else:
        bussid = i // k
        viimases = k
    print(f"Busse vaja: {bussid}. \nViimases bussis: {viimases} inimest")            

tervita()
liblikas()
A = float(input("Sisesta pilevede kõrgus(KM): "))
pilved(A)
inimeste_arv = int(input("Mitu inimest?: "))
kohtade_arv = int(input("Bussi istekohtade arv: "))
BussideArv(inimeste_arv, kohtade_arv)
