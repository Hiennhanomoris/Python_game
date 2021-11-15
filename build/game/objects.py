import pygame

# thuoc tinh chung cua cac vat the
class Objects:
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel):
        self.x_pos = x_pos                         #toa do Ox
        self.y_pos = y_pos                         #toa do Oy
        self.image = pygame.image.load(image)      #hinh anh
        self.x_vel = x_vel                         #toc do theo chieu Ox (neu co)
        self.y_vel = y_vel                         #toc do theo chieu Oy (neu co) 
    


