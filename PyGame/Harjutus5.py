import pygame, sys, random
pygame.init()

# Lae alla pall.png ja alus.png
# Loo uus mäng 640×480 suurusega. Vali heledam taustavärv
# Lisa ja animeeri pall
# palli suurus 20×20
# pall liigub sinu valitud kiirusega
# pall põrkub seintest tagasi
# Lisa ja animeeri alus
# aluse suurus 120×20
# aluse y-koordinaat on keskkohast allpool. Näiteks screenY/1.5
# alus liigub vasakule/paremale (vahetab suunda, kui puudub seinu)
# Kokkupõrke tuvastamine
# kui pall puutub alust siis muudab suunda.
# kui pall käitub kokkupuutel alusega imelikult, siis lisa tingimusse kontroll, et palli y-suund oleks suurem kui null (ballSpeedY > 0)
# Boonus
# kui pall puudub alumist äärt, siis saab mängija negatiivse punkti
# kui pall puutub alust, siis saab positiivse punkti
# kuva tulemus mängu ülemises nurgas


# Ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Harjutus 4")
screen.fill([153, 204, 255])
clock = pygame.time.Clock()

# Pildid
alus = pygame.image.load("img/alus.png")
alus = pygame.transform.scale(alus, [120,20])

pall = pygame.image.load("img/pall.png")
pall = pygame.transform.scale(pall, [20,20])




#kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4

gameover = False
while not gameover:
    #fps
    clock.tick(60)
    #mängu sulgemine ristist
    events = pygame.event.get()
    for i in pygame.event.get():
       if i.type == pygame.QUIT:
           sys.exit()
 
    #pildi lisamine ekraanile
        
    screen.blit(pall, (posX,posY))
 
    posX += speedX
    posY += speedY
    if posX > screenX-pall.get_rect().width or posX < 0:
        speedX = -speedX
 
    if posY > screenY-pall.get_rect().height or posY < 0:
        speedY = -speedY
    
    posXX, posYY = 0, 0
    screen.blit(alus, (posXX,screenY/1.5))
 
    posX += speedX
    if posX > screenX-pall.get_rect().width or posXX < 0:
        speedX = -speedX
    
    #graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill([153, 204, 255])
    
pygame.quit()