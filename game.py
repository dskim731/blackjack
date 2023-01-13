from player import Player, Dealer


player_score = 0
dealer_score = 0

def deal_cards(player, dealer):
    print("Welcome to Blackjack!")
    user_input = input("Press any key to start the game.").lower()