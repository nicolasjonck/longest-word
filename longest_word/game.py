import random
import string
import requests

class Game:
    """ Create Game class """
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        if not word:
            return False
        letters = self.grid.copy()

        """ Check all letters in grid """
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False

        """ Check word exists """
        response = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}').json()
        return response['found']
