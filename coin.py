"""
Match Coins
Caleb Gebrezgi
Tossable coin game that tracks if the coin lands on heads or tails
"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

        def toss(self):
        result = random.randint(0, 1)
        if result == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup