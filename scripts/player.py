import pygame
import objects


class Player(objects.Objects):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel)

        #for animation
        self.animation = []
        self.index = 0
        self.counter = 0
        for i in range(1, 7):
            img = pygame.image.load(f"images/player/player_run/Cyborg_run{i}.png")
            img = pygame.transform.scale(img, (35, 35))
            self.animation.append(img)
        self.image = self.animation[self.index]
        #slowdown animation
        self.slowdown = 20

    #player nhay khi giu phim space
    def jump(self):
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.y_pos > 215:
            self.y_vel -= 3

        # add gravity
        self.y_vel += 0.4
        if self.y_vel > 10:
            self.y_vel = 10

        if self.y_pos > 230:
            self.y_vel = 0
            self.y_pos = 230
        
        dy += self.y_vel

        self.y_pos += dy
    
    def update(self):
        self.counter += 3.5

        #handle animation
        if self.counter > self.slowdown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.animation):
                self.index = 0
            self.image = self.animation[self.index]
