import pygame
import numpy as np

from pyGhost.player import Player
from pyGhost.room import Room



a=1

# Initialize and create the screen
pygame.init()
SCREEN = pygame.display.set_mode((1400, 800), pygame.FULLSCREEN)
screen_rect = SCREEN.get_rect()

# Title and icon
pygame.display.set_caption('pyGhost')
ICON = pygame.image.load('pyGhost/icons/map.png')
pygame.display.set_icon(ICON)

# Consts
DISTANCE = 1.8


def show_object(obj, position):
    SCREEN.blit(obj, position)


class Game:

    def __init__(self):
        self.running = False
        self.player = Player(screen_rect)

        # Build room
        self.room = Room(SCREEN, None)

    def run(self):
        # Game loop
        player_x_change = 0
        player_y_change = 0
        self.running = True
        while self.running:
            # Background color set
            SCREEN.fill((0, 0, 0))

            self.room.show_room()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_ESCAPE, pygame.K_q]:
                        self.running = False
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

            self.player.move(player_x_change, player_y_change, self.room.walls)
            show_object(self.player.figure, self.player.position)

            pygame.display.update()
