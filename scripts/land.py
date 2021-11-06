import pygame
class Land():
    def __init__(self,x_pos, y_pos, width, height, image, x_vel, y_vel):
        self.x_pos = x_pos                         
        self.y_pos = y_pos                             
        self.x_vel = x_vel                         
        self.y_vel = y_vel     
        self.width = width
        self.height = height  
        img = pygame.image.load(image)  
        self.image = pygame.transform.scale(img, (self.width, self.height))      

    def draw(self,screen):
        screen.blit(self.image, (self.x_pos,self.y_pos))