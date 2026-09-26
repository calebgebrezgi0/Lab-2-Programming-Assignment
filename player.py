"""
Match Coins
Caleb Gebrezgi
Tossable coin game that tracks if the coin lands on heads or tails
"""

from coin import Coin

class Player:
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()