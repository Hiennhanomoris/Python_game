import pygame
from pygame.constants import BUTTON_LEFT
import player
import background
import textx
from pygame import mixer 
import land
import os
import button

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
                main()
        if exit_button.get_click() == True:
                pygame.quit()
        pygame.display.update()
    pygame.quit()

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
fps = 120
clock = pygame.time.Clock()
quit_game = False
fade_counter = 0

#get high_score
if os.path.exists("high_score.txt"):
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
else:
    high_score = 0
                            
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
    global fade_counter
    fade_counter = 0
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


#game loop
def main():
    fps = 120
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
            game_over_screen()
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                reset()
            if key[pygame.K_BACKSPACE]:
                game_menu()

        for event in pygame.event.get():
            #Quit game
            if event.type == pygame.QUIT:
                quit_game = True

        pygame.display.update()

if __name__ == "__main__":
    game_menu()



