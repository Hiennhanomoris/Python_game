import pygame

class Object:
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.image.load(image)
        self.x_vel = x_vel
        self.y_vel = y_vel
