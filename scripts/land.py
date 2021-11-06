import pygame
import random
import objects

class Land(objects.Objects):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel, width, height):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel)
    # def __init__(self,x_pos, y_pos, width, height, image, x_vel, y_vel):
    #     self.x_pos = x_pos                         
    #     self.y_pos = y_pos                             
    #     self.x_vel = x_vel                         
    #     self.y_vel = y_vel     
        self.width = width
        self.height = height  
        self.land_speed = 2 #toc do di chuyen cuc dat di dong
        img = pygame.image.load(image)  
        self.image = pygame.transform.scale(img, (self.width, self.height)) 
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos     

    def draw(self,screen):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x -= self.land_speed
        if self.rect.x < -self.width:
            self.rect.x = 800 - self.width
            self.rect.y = random.randint(280,350)
