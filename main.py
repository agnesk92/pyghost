""" Main file for the game """

import pygame


# Initialize and create the screen
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption('Random game')
ICON = pygame.image.load('icons/map.png')
pygame.display.set_icon(ICON)

# Consts
DISTANCE = 0.3

# Player
player_img = pygame.image.load('icons/ghost.png')


def player(pos_x, pos_y):
    """ Show the player """
    SCREEN.blit(player_img, (pos_x, pos_y))


def main():
    """ Main function """

    player_x = 370
    player_y = 480
    player_x_change = 0
    player_y_change = 0

    # Game loop
    running = True
    while running:
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

        player_x += player_x_change
        player_y += player_y_change

        player(player_x, player_y)
        pygame.display.update()


if __name__ == "__main__":
    main()
