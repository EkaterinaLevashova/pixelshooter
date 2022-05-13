import pygame

class Javelin:
    def __init__(self, screen):
        """init Javelin"""

        self.screen = screen
        self.image = pygame.image.load('images/Javelin.PNG')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        """painting Javelin"""
        self.screen.blit(self.image, self.rect)