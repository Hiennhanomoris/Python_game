import pygame

pygame.init();
#tao man hinh
screen = pygame.display.set_mode((900, 400))
pygame.display.set_caption("DINOSAUR")

#goi han fps
fps = 60
clock = pygame.time.Clock()

game_over = False

while game_over == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

pygame.quit