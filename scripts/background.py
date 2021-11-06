import pygame
import objects

# cac thuoc tinh, chuc nang background
class Background(objects.Objects):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel) 
        img = pygame.image.load(image)
        self.image = pygame.transform.scale(img, (800, 400))
        
    def draw(self,screen):
        screen.blit(self.image,(self.x_pos,self.y_pos))
    

        