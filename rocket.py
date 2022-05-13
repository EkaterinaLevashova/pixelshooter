import pygame

class Rocket(pygame.sprite.Sprite):

    def __init__(self, screen, javelin):
        """creating rocket by javelin position"""
        super(Rocket, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 255, 255, 0
        self.speed = 1
        self.rect.centerx = javelin.rect.centerx
        self.rect.top = javelin.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """moving rocket up"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_rocket(self):
        """draw rocket on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


