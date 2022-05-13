import pygame, controls
from javelin import Javelin

def run():
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('PIXEL WARS')
    bg_color = (0, 0, 0)
    javelin = Javelin(screen)

    while True:
        controls.events(javelin)
        javelin.update_javelin()
        screen.fill(bg_color)
        javelin.output()
        pygame.display.flip()

run()
