import pygame
import random
import sys

pygame.init()

# Colors
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue = [153, 204, 255]

# Screen settings
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Hiir")
screen.fill(lBlue)
clock = pygame.time.Clock()

circles = []  # List to store circle information
max_circles = 10  # Maximum number of circles on the screen

game_over = False
while not game_over:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(circles) < max_circles:
                pos = pygame.mouse.get_pos()
                color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                size = 10 + len(circles)  # Increase size after each click
                circles.append((pos, color, size))
                if circles==max_circles:
                    Removecircle = True
                pygame.draw.circle(screen, color, pos, size)
                pygame.display.flip()

    # Bonus feature: Change background color randomly
    screen.fill([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])

    # Draw existing circles
    for circle in circles:
        pos, color, size = circle
        pygame.draw.circle(screen, color, pos, size)

    pygame.display.flip()

pygame.quit()
