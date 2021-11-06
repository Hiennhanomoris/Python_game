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
    playerr.update(score)
    for land in land_group:
        land.update()

#vong lap game
while quit_game == False:
    clock.tick(fps)
    screen.fill((255, 255, 255)) 
    #hien thi anh
    hien_thi()
    movement()

    for event in pygame.event.get():
        #Quit game
        if event.type == pygame.QUIT:
            quit_game = True

    pygame.display.update()

pygame.quit 



