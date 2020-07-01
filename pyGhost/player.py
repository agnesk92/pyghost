import pygame
import numpy as np
from operator import add

DEFAULT_START_X = 370
DEFAULT_START_Y = 400


class Player:

    def __init__(self, screen_rect):
        self.position = (screen_rect.centerx, screen_rect.centery)
        self.figure = pygame.image.load('pyGhost/icons/ghost.png')

    @property
    def position(self):
        return self._postion_x, self._postion_y

    @property
    def figure_rect(self):
        return self.figure.get_rect(topleft = self.position)




    @position.setter
    def position(self, new_pos):


        self._postion_x, self._postion_y = new_pos

    def move(self, move_x, move_y, walls):
        old_pos = self.position
        if np.any([self.figure_rect.colliderect(wall.figure_rect) for wall in walls]):
            print('collides!')
        else:
            self.position = list(map(add, self.position, [move_x, move_y]))
            if np.any([self.figure_rect.colliderect(wall.figure_rect) for wall in walls]):
                self.position = old_pos
