""" Main file for the game """

import pygame

# Initialize and create the screen
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('Random game')
ICON = pygame.image.load('map.png')
pygame.display.set_icon(ICON)

# Player
player_img = pygame.image.load('ghost.png')
player_x = 370
player_y = 480


def player():
    SCREEN.blit(player_img, (player_x, player_y))


# Game loop
RUNNING = True
while RUNNING:
    SCREEN.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                RUNNING = False

    player()
    pygame.display.update()
