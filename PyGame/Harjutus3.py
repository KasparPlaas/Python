import pygame
import sys
pygame.init()

# Parameetrid

laius = 640
korgus = 480
varv = "red"
suurus = 50

# Ekraani seaded
screen=pygame.display.set_mode([laius,korgus])
pygame.display.set_caption("Harjutus 3")
screen.fill([0, 0, 0])

# funktsioon

def ruudud(v,s):
    for x in range(0, laius, s):
        for y in range(0, korgus, s):
            rect = pygame.Rect(x, y, s, s)
            pygame.draw.rect(screen, varv, rect, 1)
ruudud(varv,suurus)

# Ilma selleta, kui käivitasin, läks kohe kinni kui ekraan ette tuli 
crashed = False
clock = pygame.time.Clock()
counter = 1
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
    pygame.display.update()
    print(counter)
    counter += 1
    clock.tick(1) # will be 10 in the next run 