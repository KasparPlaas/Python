import pygame, sys, random
pygame.init()

# Ekraani seaded
screenX = 640
screenY = 480
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Harjutus 4")
screen.fill([255, 255, 255])
clock = pygame.time.Clock()

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3

#koordinaatide loomine ja lisamine massiivi
coords = []
for i in range (10):
    posX = random.randint(1,screenX)
    posY = random.randint(1,screenY)
    coords.append([posX, posY])


# Pildid

rada = pygame.image.load("rada.png")
rada = pygame.transform.scale(rada, [640,480])
screen.blit(rada,[0,0])



masin = pygame.image.load("masin.png")
masin = pygame.transform.scale(masin, [120,120])
screen.blit(masin,[310,370])

auto = pygame.image.load("auto.png")
masin = pygame.transform.scale(auto, [60,60])



def extract_frames(auto, screenx, screeny):
    frames = extract_frames(auto, screenx, screeny)
    current_frame = frames[0]

    screen.blit(current_frame, (screenx, screeny)) 

