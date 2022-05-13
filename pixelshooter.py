import pygame
import sys
from javelin import Javelin

def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('PIXEL WARS')
    bg_color = (0, 0, 0)
    javelin = Javelin(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        javelin.output()
        pygame.display.flip()

run()
