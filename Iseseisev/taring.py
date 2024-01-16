# 17. Email
# 	Kasutaja lisab emaili kujul enimi.pnimi@server.com
# 	Programm kontrollib kas email on sisestatud Ćµigesti
# 	Programm tĆ¼keldab selle ja vĆ¤ljastab lause: Tere enimi, sinu email on server serveris ja domeeniks on sul com
#   näide: kaspar.plaas@hkhk.edu.ee väljastab: Tere Kaspar, sinu email on serveris hkhk ja domeeniks on sul com

def email():
    email = input("Sisesta email: ")
    if email.find("@") != -1 and email.find(".") != -1:
        email = email.split("@")
        email2 = email[1].split(".")
        print("Tere " + email[0].capitalize() + ", sinu email on serveris " + email2[0] + " ja domeeniks on sul " + email2[1])
    else:
        print("Email on valesti sisestatud!")
email()