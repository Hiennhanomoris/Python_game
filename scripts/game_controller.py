import pygame
import player
import background


pygame.init();
#tao man hinh
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("DINOSAUR")

#goi han fps
fps = 60
clock = pygame.time.Clock()

game_over = False

while game_over == False:
    clock.tick(fps)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

pygame.quit 