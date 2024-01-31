import pygame, sys, random
pygame.init()

# Värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# Ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Harjutus 4")
screen.fill([255, 255, 255])
clock = pygame.time.Clock()

# Pildid
taust = pygame.image.load("img/rada.png")
taust = pygame.transform.scale(taust, [640,480])

auto1 = pygame.image.load("img/masin1.png")
auto1 = pygame.transform.scale(auto1, [45,95])

auto2 = pygame.image.load("img/masin2.png")
auto2 = pygame.transform.scale(auto2, [45,95])

# Kiiruts ja asukoht
posX, posY = 0, 0
speedX = 3

# Koordinaadid
coords = []
for i in range(10):
    posX = random.randint(200, 400)
    posY = random.randint(1, screenY)
    coords.append([posX, posY])

gameover = False
score = 0
font = pygame.font.Font(None, 28)
while not gameover:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(taust,[0,0])
    screen.blit(auto1,[310,380])
    
    for i in range(3):
        screen.blit(auto2, [coords[i][0], coords[i][1]])
        coords[i][1] += 1
        # kui auto jõuab alla, siis läheb uuesti üles
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-10, 100)
            coords[i][0] = random.randint(170, 460)
            score += 1
    
    text = font.render("Score: "+str(score), True, [0, 0, 0])
    screen.blit(text, [10, 10]) 
    
    pygame.display.flip()

pygame.quit()
