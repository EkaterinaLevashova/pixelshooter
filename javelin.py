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
        self.mright = False
        self.mleft = False

    def output(self):
        """painting Javelin"""
        self.screen.blit(self.image, self.rect)

    def update_javelin(self):
        """updating position"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        elif self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1