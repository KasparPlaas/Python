# Kaspar Plaas  
# 30.01.2024

from tkinter import *


aken = Tk()
aken.title('Joonistamine')



louend = Canvas(aken, width=240, height=240)
louend.create_text(120,18, text="Tšehhi", font=("Tahoma", 24))
louend.pack()



louend.create_polygon(0,40, 0,240, 100,140, fill='blue')
louend.create_polygon(0,240, 100,140, 200,240, fill='red')
louend.create_rectangle(100,140, 239,239,  fill='red', outline='red')
louend.create_line(0,42, 239,42)






aken.mainloop()