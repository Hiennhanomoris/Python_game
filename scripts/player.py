import pygame
import objects


class Player(objects.Objects):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel, mixer):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        #for animation
        self.run_animation = []
        self.run_index = 0
        self.jump_animation = []
        self.jump_index = 0
        self.counter = 0
        self.on_ground = True

        #cho cac anh vao cac array de tien su dung
        for i in range(1, 7):
            img = pygame.image.load(f"images/player/player_run/Cyborg_run{i}.png")
            img = pygame.transform.scale(img, (60, 60))
            self.run_animation.append(img)
        for i in range(1, 5):
            img = pygame.image.load(f"images/player/player_jump/Cyborg_jump{i}.png")
            img = pygame.transform.scale(img, (60, 60))
            self.jump_animation.append(img)

        #slowdown animation
        self.slowdown = 20
        self.counter_sound = 0
        self.jumping_sound = mixer.Sound("sound/Plop_Jump_SFX.wav")


    #player nhay khi giu phim space
    def jump(self):
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.on_ground:
            self.on_ground = False
            self.y_vel -= 13
            #jumping audio
            self.jumping_sound.play()

        # add gravity
        self.y_vel += 0.6
        if self.y_vel > 10:
            self.y_vel = 10
        
        dy += self.y_vel
        self.rect.y += dy

    def check_collision(self, land_group):
        #check collision with ground
        if self.rect.y > 350:
            self.y_vel = 0
            self.rect.y = 350
            self.on_ground = True
            self.jump_index = 0
    
    def update(self, score, land_group):
        self.counter += 3.5

        #handle animation
        if self.counter > self.slowdown:
            score.incre_point()
            self.counter = 0
            if self.on_ground:
                self.image = self.run_animation[self.run_index]
                self.run_index += 1
                if self.run_index >= len(self.run_animation):
                    self.run_index = 0
            else:
                self.image = self.jump_animation[self.jump_index]
                self.jump_index += 1
                if self.jump_index >= len(self.jump_animation):
                    self.jump_index = len(self.jump_animation)-1
        
        self.check_collision(land_group)

    #hien thi player
    def hien_thi(self, screen):
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, width=2)

