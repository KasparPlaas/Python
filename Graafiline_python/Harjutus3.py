# Kaspar Plaas
# 30.01.2024

from tkinter import *

aken = Tk()
aken.title('Tkinter "Tervitus"')
aken.configure(background='black')
aken.resizable(0, 0)
 

tekst = Label(aken, text="Nimi: Kaspar Plaas\nRühm: IT23\n2023", fg="red",font="Tahoma 20 bold italic", bg="black",)
tekst.pack(pady=10, padx=30)
aken.mainloop()