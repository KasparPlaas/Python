import pygame
pygame.init()

# Ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutus 2")
screen.fill([255, 255, 255])
 
# Pildid

shop = pygame.image.load("shop.jpg")
shop = pygame.transform.scale(shop, [640,480])
screen.blit(shop,[0,0])

seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, [224,282])
screen.blit(seller,[120,180])

chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, [240,180])
screen.blit(chat,[240,100])


# Tekst
font = pygame.font.Font(None, 28)
text = font.render("Tere, olen Kaspar", True, [255,255,255])
screen.blit(text, [270,160])
 
pygame.display.flip()

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