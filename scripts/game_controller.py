import pygame
import player
import background


pygame.init();
#tao man hinh
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("DINOSAUR")

#tao cac object ban dau
playerr = player.Player(120, 230, "images/player.png", 0, 0)

#goi han fps
fps = 60
clock = pygame.time.Clock()

game_over = False

while game_over == False:
    clock.tick(fps)
    screen.fill((255, 255, 255))

    #hien thi player
    player_rect = screen.blit(playerr.image, (playerr.x_pos, playerr.y_pos))
    print(playerr.y_pos)

    #nhay
    playerr.jump()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()

pygame.quit 