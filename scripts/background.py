import pygame
import objects

# cac thuoc tinh, chuc nang background
class Backgroud(objects.Objects):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel) 

        