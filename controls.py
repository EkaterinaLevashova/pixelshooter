import pygame, sys
from rocket import Rocket

def events(screen, javelin, rockets):
    """event handling"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:

            # to the right
            if event.key == pygame.K_d:
                javelin.mright = True

            # to the left
            elif event.key == pygame.K_a:
                javelin.mleft = True

            # fire
            elif event.key == pygame.K_w:
                new_rocket = Rocket(screen, javelin)
                rockets.add(new_rocket)

        elif event.type == pygame.KEYUP:

            # to the right
            if event.key == pygame.K_d:
                javelin.mright = False

            # to the left
            elif event.key == pygame.K_a:
                javelin.mleft = False

def update(bg_color, screen, javelin, rockets):
    """screen updating"""
    screen.fill(bg_color)
    for rocket in rockets.sprites():
        rocket.draw_rocket()
    javelin.output()
    pygame.display.flip()

def update_rockets(rockets):
    """rockets position updating"""
    rockets.update()
    for rocket in rockets.copy():
        if rocket.rect.bottom <= 0:
            rockets.remove(rocket)