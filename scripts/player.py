import pygame
import objects
import game_controller

class Player(objects.Object):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel)

    #player nhay khi giu phim space
    def jump(self):
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.y_pos > 210:
            self.y_vel -= 1

        # add gravity
        self.y_vel += 0.2
        if self.y_vel > 10:
            self.y_vel = 10

        if self.y_pos > 230:
            self.y_vel = 0
            self.y_pos = 230
        
        dy += self.y_vel

        self.y_pos += dy