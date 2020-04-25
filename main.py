""" Main file for the game """
import pygame
from operator import add

from pyGhost.player import Player

# Initialize and create the screen
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('pyGhost')
ICON = pygame.image.load('pyGhost/icons/map.png')
pygame.display.set_icon(ICON)

# Consts
DISTANCE = 0.3


def show_object(obj, position):
    SCREEN.blit(obj, position)


def main():
    """ Main function """
    player = Player()

    player_x_change = 0
    player_y_change = 0

    # Game loop
    running = True
    while running:
        # Background color set
        SCREEN.fill((0, 0, 0))

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
    main()
