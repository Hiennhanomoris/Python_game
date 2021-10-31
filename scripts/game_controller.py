import pygame
import player
import background
import ground
import textx


pygame.init();
#tao man hinh
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("RUN NOW")

#tao cac object ban dau
playerr = player.Player(120, 230, "images/player.png", 0, 0)

#gioi han fps
fps = 60
clock = pygame.time.Clock()
quit_game = False
                            
def hien_thi():
    screen.blit(playerr.image, playerr.rect)
    pygame.draw.rect(screen, (0, 0, 0), playerr.rect, width=2)
#vong lap game
while quit_game == False:
    clock.tick(fps)
    screen.fill((255, 255, 255))

    #hien thi anh
    hien_thi()

    #nhay
    playerr.jump()
    playerr.update()

    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.QUIT:
            quit_game = True

    pygame.display.update()

pygame.quit 

