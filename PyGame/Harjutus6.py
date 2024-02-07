import pygame
import sys

pygame.init()

# Muusika

pygame.mixer.music.load("music/muusika.mp3")
pygame.mixer.music.play()


# Ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Harjutus 5")
screen.fill([153, 204, 255])
clock = pygame.time.Clock()

# Pildid
alus = pygame.image.load("img/alus.png")
alus = pygame.transform.scale(alus, [120, 20])

pall = pygame.image.load("img/pall.png")
pall = pygame.transform.scale(pall, [20, 20])

# kiirus ja asukoht
        # Aluse seaded
alusX = 0
speedX, speedY = 0.1, 0

        # Palli seaded
pallX, pallY = 0, 0
pallspeedX, pallspeedY = 3, 4
directionX = 0

# Punktid
punktid = 0

gameover = False
while not gameover:
    clock.tick(60)
    
    # mängu sulgemine ristist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamover = True
            sys.exit()

        # Klaviatuuri nupud
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -5
            elif event.key == pygame.K_RIGHT:
                speedX = 5
            
    
    # Piirid
    
    if directionX == "move_left":
        if alusX > 0:
            alusX -= 3
    elif directionX == "move_right":
        if alusX + 30 < screenX:
            alusX += 3
        
        
    # Palli liikumine
    screen.blit(pall, (pallX, pallY))
    pallX += pallspeedX
    pallY += pallspeedY

    if pallX > screenX - pall.get_rect().width or pallX < 0:
        pallspeedX = -pallspeedX

    if pallY > screenY - pall.get_rect().height or pallY < 0:
        pallspeedY = -pallspeedY

    # Aluse liikumine
    screen.blit(alus, (alusX, screenY / 1.5))
    alusX += speedX

    if alusX > screenX - alus.get_rect().width or alusX < 0:
        speedX = -speedX

    # Kokkupõrke tuvastamine
    
    if pallX + pall.get_rect().width > alusX and pallX < alusX + alus.get_rect().width and pallY + pall.get_rect().height == screenY / 1.5:
        pallspeedY = -pallspeedY
        punktid += 1    
    
    # punktid
    font = pygame.font.Font(None, 28)
    text = font.render("punktid: " + str(punktid), True, [0, 0, 0])
    screen.blit(text, [10, 10])

    # Lõpetab mängu kui pall vastu alumist serva läheb
    
    if pallY > 460:
        gameover = True
        sys.exit()

    # graafika kuvamine ekraanil
    pygame.display.flip()
    screen.fill([153, 204, 255])

pygame.quit()