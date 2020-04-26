import pygame


class Wall(pygame.sprite.Sprite):
    """
    Walls can't be passed by player.
    """

    def __init__(self, x, y):
        # Init
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y

        # Create
        # self.figure = pygame.image.load('pyGhost/icons/wall.png')
        self.figure = pygame.image.load('pyGhost/icons/wall.png')
        # self.rect = self.figure.get_rect()
