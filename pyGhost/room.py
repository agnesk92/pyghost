import pygame

from pyGhost.wall import Wall
import pyGhost.object_consts as objects


# POSITIONS =

WALLS = [
    Wall(300, 300),
    Wall(332, 300),
]

def get_horizontal_positions(from_coords, to_coords):
    pos = [(pos, from_coords[1]) for pos in range(from_coords[0], to_coords[0] + objects.SIZE, objects.SIZE)]
    return pos


def get_vertical_positions(from_coords, to_coords):
    pos = [(from_coords[0], pos) for pos in range(from_coords[1], to_coords[1], objects.SIZE)]
    return pos


def create_walls(screen, chained=True, number=40, closed=False, symmetric=False):
    x, y = screen.get_size()

    top_left = (int(x/2)-336, int(y/2)-336)
    top_right = (int(x/2)+336, int(y/2)-336)
    bottom_right = (int(x/2)+336, int(y/2)+336)
    bottom_left = (int(x/2)-336, int(y/2)+336)

    top_side = get_horizontal_positions(top_left, top_right)
    right_side = get_vertical_positions(top_right, bottom_right)
    bottom_side = get_horizontal_positions(bottom_left, bottom_right)
    left_side = get_vertical_positions(top_left, bottom_left)

    positions = top_side + right_side + bottom_side + left_side
    walls = [Wall(el[0], el[1]) for el in positions]
    return walls


class Room:
    """ Read a room config, and build walls by that for the screen """

    def __init__(self, screen, walls=None):
        if walls is None:
            walls = create_walls(screen)

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
