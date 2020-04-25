""" Main file for the game """
import pygame
from operator import add

from pyGhost.player import Player

# Initialize and create the screen
pygame.init()
SCREEN = pygame.display.set_mode((1400, 800))

# Title and icon
pygame.display.set_caption('pyGhost')
ICON = pygame.image.load('pyGhost/icons/map.png')
pygame.display.set_icon(ICON)

# Consts
DISTANCE = 0.8

# Objects
pink_castle = pygame.image.load('pyGhost/icons/castle_pink.png')
grey_castle = pygame.image.load('pyGhost/icons/castle_grey.png')
castle = pygame.image.load('pyGhost/icons/castle.png')


def show_object(obj, position):
    SCREEN.blit(obj, position)


def run_game():
    """ Main function """
    player = Player()

    # Game loop
    player_x_change = 0
    player_y_change = 0
    running = True
    while running:
        # Background color set
        SCREEN.fill((0, 0, 0))

        # show_object(grey_castle, (100, 100))
        # show_object(pink_castle, (820, 500))
        # show_object(pink_castle, (920, 300))
        # show_object(castle, (600, 90))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_LEFT:
                    player_x_change = -DISTANCE
                if event.key == pygame.K_RIGHT:
                    player_x_change = DISTANCE
                if event.key == pygame.K_DOWN:
                    player_y_change = DISTANCE
                if event.key == pygame.K_UP:
                    player_y_change = -DISTANCE
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player_y_change = 0

        player.move(player_x_change, player_y_change)
        show_object(player.figure, player.position)

        pygame.display.update()



if __name__ == "__main__":
    run_game()
