import pygame
pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Khung long bao chua")
pygame.display.update()
clock  = pygame.time.Clock()
green = (157,210,181)
bg = pygame.image.load('bg.jpg')
bg = pygame.transform.scale(bg, (800,400))
x_character = 50
y_character = 300
character = pygame.image.load('character.png')
character = pygame.transform.scale(character, (80, 100))
open = True
while open:
    clock.tick(60)
    screen.fill(green)
    screen.blit(bg,(0,0))
    cr = screen.blit(character,(x_character,y_character))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            open = False
    pygame.display.flip();
    

pygame.quit()
quit()
#abcdef