import pygame
import objects


class Player(objects.Objects):
    def __init__(self, x_pos, y_pos, image, x_vel, y_vel, mixer):
        super().__init__(x_pos, y_pos, image, x_vel, y_vel)
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.die = False

        #for animation
        self.run_animation = []
        self.run_index = 0
        self.jump_animation = []
        self.jump_index = 0
        self.counter = 0
        self.on_ground = True

        #cho cac anh vao cac array de tien su dung
        for i in range(1, 7):
            img = pygame.image.load(f"images/player/RUN/run{i}.png")
            img = pygame.transform.scale(img, (60, 60))
            self.run_animation.append(img)
        for i in range(1, 4):
            img = pygame.image.load(f"images/player/JUMP/jump{i}.png")
            img = pygame.transform.scale(img, (60, 60))
            self.jump_animation.append(img)

        #slowdown animation
        self.slowdown = 20
        self.counter_sound = 0
        self.jumping_sound = mixer.Sound("sound/Plop_Jump_SFX.wav")
        self.game_over_sound = mixer.Sound("sound/game_over.wav")


    #player nhay khi giu phim space
    def jump(self):
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.on_ground:
            self.on_ground = False
            self.y_vel -= 7.5
            #jumping audio
            self.jumping_sound.play()

        # add gravity
        self.y_vel += 0.3
        if self.y_vel > 10:
            self.y_vel = 10
        
        dy += self.y_vel
        self.rect.y += dy

    def check_collision(self, land_group):
        #check collision with ground
        if self.rect.y > 350:
            self.die = True
            self.rect.y = 350
            self.y_vel = 0
            self.game_over_sound.play()

        #check collision with land
        for land in land_group:
            if land.rect.colliderect(self.rect.x, self.rect.y, 60, 60):
                if self.rect.bottom < land.rect.centery:
                    self.rect.bottom = land.rect.top
                    self.y_vel = 0
                    self.on_ground = True
    
    def update(self, land_group):
        self.counter += 2.2

        #handle animation
        if self.counter > self.slowdown:
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
        #pygame.draw.rect(screen, (0, 0, 0), self.rect, width=2)

