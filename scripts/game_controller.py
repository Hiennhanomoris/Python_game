import pygame
import player
import background
import textx
from pygame import mixer 
import land
mixer.init()
pygame.init()

#tao man hinh
screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("RUN NOW")

#tao cac object ban dau
bg1 = background.Background(0,0,"images/bg.jpg",0,0)
playerr = player.Player(250, 90, "images/player.png", 0, 0, mixer)
score = textx.Textx("consolas", 30, "Score", (100, 200, 168))
game_over = textx.Textx("consolas", 60, "game over", (255, 30, 0))
play_again = textx.Textx("consolas", 20, "play again", (255, 255, 255))
landstart = land.Land(0, 250,"images/LAND/landstart.png",0,0, 130, 40)
land1 = land.Land(200, 240,"images/LAND/land1.png",0,0, 120, 45)
land2 = land.Land(400 ,250,"images/LAND/land2.png",0,0, 120, 40)
land3 = land.Land(600 , 260,"images/LAND/land3.png",0,0, 90, 75)
land_group = [land1, land2, land3, landstart]


#gioi han fps
fps = 60
clock = pygame.time.Clock()
quit_game = False
                            
def hien_thi():
    bg1.draw(screen)
    playerr.hien_thi(screen)
    score.hien_thi(screen, 0, 0, f"Score:{score.point}")
    for land in land_group:
        land.draw(screen)

def movement():
    playerr.jump()
    playerr.update(land_group)
    for land in land_group:
        land.update(score)

def reset():
    playerr.die = False
    score.point = 0
    playerr.rect.y = 90
    land1.rect.x = 200
    land1.rect.y = 240
    land2.rect.x = 400
    land2.rect.y = 250
    land3.rect.x = 600
    land3.rect.y = 260
    landstart.rect.x = 0
    landstart.rect.y = 250
    for land in land_group:
        land.land_speed = 1

#vong lap game
while quit_game == False:
    clock.tick(fps)
    if playerr.die == False:
        screen.fill((255, 255, 255)) 
        #hien thi anh
        hien_thi()
        movement()
    else:
        game_over.hien_thi(screen, 230, 200, "GAME OVER!!!")
        play_again.hien_thi(screen, 260, 30, "press space to try again :)")
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            reset()

    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.QUIT:
            quit_game = True

    pygame.display.update()

pygame.quit 



