import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees - Kaspar Plaas")
screen.fill([0,0,0])

pygame.draw.circle(screen, [255, 255, 255], [150,200], 55)
pygame.draw.circle(screen, [255, 255, 255], [150,110], 40)
pygame.draw.circle(screen, [255, 255, 255], [150,45], 30)

pygame.draw.circle(screen, [0,0,0], [140,40], 5)
pygame.draw.circle(screen, [0,0,0], [160,40], 5)

pygame.draw.polygon(screen, (252, 0, 55), [[145,50], [155,50], [150,65]])


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