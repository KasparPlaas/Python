import pygame
pygame.init()
 
# Ekraani seaded
screen=pygame.display.init() 
pygame.display.set_mode([300,300])
pygame.display.set_caption("Lumemees - Kaspar Plaas")

screen.fill([0,0,0])

#Joonistamine
pygame.draw.circle(screen, [255, 255, 255], [150, 250], 100, 1)

pygame.display.flip()


