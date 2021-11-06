import pygame
import player
import background
import ground
import textx
from pygame import mixer 
import land
import random
mixer.init()
pygame.init();

#tao man hinh
screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("RUN NOW")

#tao cac object ban dau
playerr = player.Player(120, 230, "images/player.png", 0, 0, mixer)
score = textx.Textx("consolas", 30, "Score", (100, 200, 168))
landstart = land.Land(0, 250,130 ,40,"images/LAND/landstart.png",0,0)
land1 = land.Land(200, 240, 120 , 45,"images/LAND/land1.png",0,0)
land2 = land.Land(400 ,250, 120 , 40,"images/LAND/land2.png",0,0)
land3 = land.Land(600 , 260, 90 , 75,"images/LAND/land3.png",0,0)


#gioi han fps
fps = 60
clock = pygame.time.Clock()
quit_game = False
                            
def hien_thi():
    playerr.hien_thi(screen)
    score.hien_thi(screen, 0, 0, f"Score:{score.point}")
    landstart.draw(screen)
    land1.draw(screen)
    land2.draw(screen)
    land3.draw(screen)

def movement():
    playerr.jump()
    playerr.update(score)
    #cuc dat di dong
    land1.update()
    land2.update()
    land3.update()
    landstart.update()
    if landstart.x_pos < -landstart.width:
        landstart.x_pos = 800 - landstart.width
        landstart.y_pos = random.randint(235,265)
    if land1.x_pos < -land1.width:
        land1.x_pos = 800 - land1.width
        land1.y_pos = random.randint(235,265)
    if land2.x_pos < -land2.width:
        land2.x_pos = 800 - land2.width
        land2.y_pos = random.randint(235,265)
    if land3.x_pos < -land3.width:
        land3.x_pos = 800 - land3.width
        land3.y_pos = random.randint(235,265)

#vong lap game
# bg1 = background.Background(0,0,"images/bg.jpg",0,0)
# bg1.draw(screen)
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



