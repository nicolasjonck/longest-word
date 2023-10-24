# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        game = Game()
        # exercise
        grid = game.grid
        # verify
        assert type(grid) == list
        assert len(grid) == 9

        for letter in grid:
            assert letter in string.ascii_uppercase

        # teardown

    def test_empty_word_invalid(self):
        game = Game()
        assert game.is_valid('') is False


    def test_is_valid(self):
        """ Test if function returns True for valid words """
        # setup
        game = Game()
        test_grid = 'IRPLANEAD'
        # exercise
        game.grid = list(test_grid)
        assert game.is_valid('PLANE') is True
        assert game.is_valid('AIRPLANE') is True
        assert game.is_valid('LANE') is True
        assert game.is_valid('AIR') is True
        assert game.is_valid('DEAR') is True
        assert game.is_valid('READ') is True
        assert game.grid == list(test_grid)


    def test_is_invalid(self):
        """ Test if function returns False for invalid words """
        # setup
        game = Game()
        test_grid = 'IRPLANEAD'
        # exercise
        game.grid = list(test_grid)
        assert game.is_valid('MOTHER') is False
        assert game.is_valid('PLANES') is False
        assert game.grid == list(test_grid)
