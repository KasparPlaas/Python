# Ksuuruspar Plasuurus
# 30.01.202suurus

from tkinter import *

aken = Tk()
aken.title("Kalkulaator")
suurus = 50

aken.geometry("200x200")
aken.resizable(0,0)
aken.option_add('*font', ('tahoma', 12))
tekst = Label(aken, text="Siia kunagi vastus!")
tekst.grid(row=0, column=0, columnspan=4, padx=2, pady=2)
# nupp1-16
suurus = 4

nupp1 = Button(aken, text="7", width=suurus)
nupp1.grid(row=1, column=0, padx=2, pady=2)

nupp2 = Button(aken, text="4", width=suurus)
nupp2.grid(row=2, column=0, padx=2, pady=2)

nupp3 = Button(aken, text="1", width=suurus)
nupp3.grid(row=3, column=0, padx=2, pady=2)

nupp4 = Button(aken, text="0", width=suurus)
nupp4.grid(row=4, column=0, padx=2, pady=2)

nupp5 = Button(aken, text="8", width=suurus)
nupp5.grid(row=1, column=1, padx=2, pady=2)

nupp6 = Button(aken, text="5", width=suurus)
nupp6.grid(row=2, column=1, padx=2, pady=2)

nupp7 = Button(aken, text="2", width=suurus)
nupp7.grid(row=3, column=1, padx=2, pady=2)

nupp8 = Button(aken, text=",", width=suurus)
nupp8.grid(row=4, column=1, padx=2, pady=2)

nupp9 = Button(aken, text="9", width=suurus)
nupp9.grid(row=1, column=2, padx=2, pady=2)

nupp10 = Button(aken, text="6", width=suurus)
nupp10.grid(row=2, column=2, padx=2, pady=2)

nupp11 = Button(aken, text="3", width=suurus)
nupp11.grid(row=3, column=2, padx=2, pady=2)

nupp12 = Button(aken, text="=", width=suurus)
nupp12.grid(row=4, column=2, padx=2, pady=2)

nupp13 = Button(aken, text="/", width=suurus)
nupp13.grid(row=1, column=3, padx=2, pady=2)

nupp14 = Button(aken, text="*", width=suurus)
nupp14.grid(row=2, column=3, padx=2, pady=2)

nupp15 = Button(aken, text="-", width=suurus)
nupp15.grid(row=3, column=3, padx=2, pady=2)

nupp16 = Button(aken, text="+", width=suurus)
nupp16.grid(row=4, column=3, padx=2, pady=2)

aken.mainloop()