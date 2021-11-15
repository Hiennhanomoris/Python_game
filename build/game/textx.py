import pygame


class Textx:
    def __init__(self, font, size, mess, RGB):
        self.font = pygame.font.SysFont(font, size)
        self.RGB = RGB
        self.text = self.font.render(mess, True, self.RGB)
        self.point = 0

    def hien_thi(self, screen, x, y, mess):
        self.text = self.font.render(mess, True, self.RGB)
        screen.blit(self.text, (x, y))

    def incre_point(self):
        self.point += 1