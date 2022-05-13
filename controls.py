import pygame, sys

def events(javelin):
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
        elif event.type == pygame.KEYUP:
            # to the right
            if event.key == pygame.K_d:
                javelin.mright = False
            # to the left
            elif event.key == pygame.K_a:
                javelin.mleft = False