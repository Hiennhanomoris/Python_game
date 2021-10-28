import pygame
import game_controller
import objects

class Backgroud(objects.Object):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel)