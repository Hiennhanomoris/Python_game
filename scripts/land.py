import pygame
import random
import objects

class Land(objects.Objects):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel, width, height):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel)
        self.width = width
        self.height = height  
        self.land_speed = 1                 #toc do di chuyen cuc dat di dong
        img = pygame.image.load(image)  
        self.image = pygame.transform.scale(img, (self.width, self.height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos   
        self.check_speed_up = True  

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def speed_up(self):
        self.land_speed += 1


    def update(self, score):
        self.rect.x -= self.land_speed
        if self.rect.x < -self.width:
            score.incre_point()
            self.rect.x = 800 - self.width
            self.rect.y = random.randint(280,350)

        if score.point%10 == 0 and self.check_speed_up == True:
            self.speed_up()
            self.check_speed_up = False
        if score.point%10 == 1:
            self.check_speed_up = True