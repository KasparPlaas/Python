from tkinter import *

#akna seaded
aken = Tk()
aken.title('Nupud')
aken.geometry("260x180")


# hinna sisestus

hind = Label(aken, text="Hind käibemaksuta: ")
hind.grid(row=0,column=0,sticky=W)

sisestus = Entry(aken)
sisestus.grid(row=0,column=1)



# käibemaksu valik

silt = Label(aken, text="Käibemaksumäär: ")
silt.grid(row=2,column=0, sticky=W)

var = DoubleVar()
maks9 = Radiobutton(aken,text="9%", variable=var, value=0.09,)
maks9.grid(row=2,column=1,sticky=W)
maks20 = Radiobutton(aken,text="20%", variable=var, value=0.20,)
maks20.grid(row=3,column=1,sticky=W)



# Vahe

vahe = Label(aken, text="______________________________________")
vahe.grid(row=4,column=0,columnspan=2)


# funktsioonid

def arvuta():
    hind = float(sisestus.get())
    maks = float(var.get())
    kaibemaks = hind * maks
    kokku = hind + kaibemaks
    vastus1.config(text=str(kaibemaks)+ " €")
    vastus2.config(text=str(kokku)+ " €")


# Vastused käibemaksu osa ja lõpphind


maks = Label(aken, text="Käibemaks: ",)
maks.grid(row=5,column=0,sticky=W)

vastus1 = Label(aken, text="")
vastus1.grid(row=5,column=1)

kokku = Label(aken, text="Hind käibemaksuga: ")
kokku.grid(row=6,column=0,sticky=W)

vastus2 = Label(aken, text="")
vastus2.grid(row=6,column=1)






# OK NUPP
nupp5 = Button(aken, text="OK", width=4, command=arvuta)
nupp5.grid(row=8, column=1, padx=2, pady=2, sticky=E)



mainloop()