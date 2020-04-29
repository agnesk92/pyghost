""" Main file for the game """
import logging

from pyGhost.game import Game


def run_game():
    """ Main function """
    logging.info('Run game')
    game = Game()
    game.run()
    logging.info('Stopped game')


if __name__ == "__main__":
    run_game()
