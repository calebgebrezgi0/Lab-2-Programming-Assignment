"""
Match Coins
Caleb Gebrezgi
Tossable coin game that tracks if the coin lands on heads or tails
"""

from player import Player

def main():
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(player1.get_name(), "has", player1.get_wallet(), "coins.")
    print(player2.get_name(), "has", player2.get_wallet(), "coins.")

    play_again = input("Do you want to toss the coins? (y/n): ")
    game_over = False

    while play_again.lower() == "y" and game_over == False:
        print("\nTossing...")
        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(player1.get_name(), "tossed", side1)
        print(player2.get_name(), "tossed", side2)

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match!", player1.get_name(), "wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match!", player2.get_name(), "wins a coin.")

        print(player1.get_name(), "has", player1.get_wallet(), "coins.")
        print(player2.get_name(), "has", player2.get_wallet(), "coins.")

        play_again = input("Do you want to toss the coins? (y/n): ")