import pygame

DEFAULT_START_X = 370
DEFAULT_START_Y = 400


class Player:

    def __init__(self):
        self.position = (DEFAULT_START_X, DEFAULT_START_Y)
        self.figure = pygame.image.load('pyGhost/icons/ghost.png')

    @property
    def position(self):
        return self._postion_x, self._postion_y

    @position.setter
    def position(self, new_pos):
        self._postion_x = new_pos[0]
        self._postion_y = new_pos[1]

    def move(self, move_x, move_y):
        # self.position = list(map(add, self.position, [move_x, move_y]))
        new_pos_x = self.position[0] + move_x
        new_pos_y = self.position[1] + move_y
        self.position = (new_pos_x, new_pos_y)
