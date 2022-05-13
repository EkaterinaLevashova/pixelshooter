import pygame, controls
from javelin import Javelin
from pygame.sprite import Group

def run():
    pygame.init()
    screen = pygame.display.set_mode((500, 600))
    pygame.display.set_caption('PIXEL WARS')
    bg_color = (0, 0, 0)
    javelin = Javelin(screen)
    rockets = Group()


    while True:
        controls.events(screen, javelin, rockets)
        javelin.update_javelin()
        controls.update(bg_color, screen, javelin, rockets)
        controls.update_rockets(rockets)

run()
