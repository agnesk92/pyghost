import pygame

from pyGhost.wall import Wall

WALLS = [
    Wall(300, 300),
    Wall(332, 300),
]


class Room:
    """ Read a room config, and build walls by that for the screen """

    def __init__(self, screen, walls=None):
        if walls is None:
            walls = WALLS

        self._walls = walls
        self.screen = screen

    @property
    def walls(self):
        return self._walls

    @walls.setter
    def walls(self, new_walls):
        self._walls = new_walls

    def show_room(self):
        for wall in self.walls:
            self.screen.blit(wall.figure, (wall.x, wall.y))
