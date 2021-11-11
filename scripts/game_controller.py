import pygame
from pygame.constants import BUTTON_LEFT
import player
import background
import textx
from pygame import mixer 
import land
import os
import button
import time

mixer.init() 
pygame.init()

#tao icon game
icon = pygame.image.load("images/avt.jpg")
pygame.display.set_icon(icon)

#tao man hinh
screen = pygame.display.set_mode((800, 400))  
pygame.display.set_caption("NINJA RUN")

# menu game
def game_menu():
    menu_sound = mixer.Sound("sound/menu_sound.mp3")
    menu_sound.set_volume(0.5)
    menu_sound.play(-1)
    menu = pygame.image.load("images/menu/menu.jpg")
    menu = pygame.transform.scale(menu,(800,400))
    screen.blit(menu,(0,0))
    start_img = pygame.image.load('images/menu/start.png').convert_alpha()
    exit_img = pygame.image.load('images/menu/exit.png').convert_alpha()
    start_button = button.Button(600, 140, start_img, 1)
    exit_button = button.Button(600, 220, exit_img, 1)
    start_button.draw(screen)
    exit_button.draw(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if start_button.get_click() == True:
                menu_sound.stop()
                main()
        if exit_button.get_click() == True:
                pygame.quit()
        pygame.display.update()
    pygame.quit()

#tao cac object ban dau
bg1 = background.Background(0,0,"images/bg.jpg",0,0)
bg2 = background.Background(0,0,"images/bg2.jpg",0,0)
bg3 = background.Background(0,0,"images/bg3.jpg",0,0)
bg4 = background.Background(0,0,"images/bg4.jpg",0,0)
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
fps = 100
clock = pygame.time.Clock()
quit_game = False
fade_counter = 0
check_restart = False
background_sound = mixer.Sound("sound/game_sound.mp3")
background_sound.set_volume(0.3)

#get high_score
if os.path.exists("high_score.txt"):
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
else:
#if this is the first time, high_score = 0
    high_score = 0
                            
def hien_thi():
    if score.point < 20:
        bg1.draw(screen)
    elif score.point >= 20 and score.point < 40:
        bg2.draw(screen)
    elif score.point >= 40 and score.point < 60:
        bg3.draw(screen)
    else :
        bg4.draw(screen)
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
    global check_restart
    global fade_counter
    check_restart = False
    fade_counter = 0
    background_sound.play(-1)
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

def game_over_screen():
    global check_restart
    global fade_counter
    global high_score
    if fade_counter < 400:
        fade_counter += 3
        pygame.draw.rect(screen, (33, 33, 33), (0, 0, fade_counter, 400))
        pygame.draw.rect(screen, (33, 33, 33), (800-fade_counter, 0, 800, 400))

    if score.point < high_score:  
        score.hien_thi(screen, 300, 100, f"Your Score:{score.point}")
        score.hien_thi(screen, 300, 150, f"High Score:{high_score}")
    else:
        score.hien_thi(screen, 300, 100, f"Best Score:{score.point}")
        #update high score
        high_score = score.point
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))

    game_over.hien_thi(screen, 230, 200, "GAME OVER!!!")
    play_again.hien_thi(screen, 260, 30, "press space to try again :)")   

    if fade_counter > 400:
        check_restart = True    


#game loop
def main():
    fps = 100
    clock = pygame.time.Clock()
    quit_game = False
    reset()
    while quit_game == False:
        clock.tick(fps)
        if playerr.die == False:
            screen.fill((255, 255, 255)) 
            #hien thi anh
            hien_thi()
            movement()
        else:
            background_sound.stop()
            game_over_screen()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and check_restart:
                reset()
            if key[pygame.K_BACKSPACE]:
                game_menu()

        for event in pygame.event.get():
            #Quit game
            if event.type == pygame.QUIT:
                quit_game = True
                pygame.quit()

        pygame.display.update()

if __name__ == "__main__":
    game_menu()



