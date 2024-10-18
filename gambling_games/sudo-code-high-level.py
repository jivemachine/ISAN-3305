# Authors: Jeremy Cobb, John Courtright, Stanley Odiase

# Instructor: Zachary Kelley

# ISAN 3305: Business Programming I

# Three Card Poker interactive game

# imports
import random
import sys
import time


def print_slow(str, speed=0.05):
    for letter in str:
        print(letter, end="", flush=True)
        time.sleep(speed)
        

 

# Start-up: Basic UI for user, get number of players & rounds to play as inputs, pass them back to main

def main_menu():

    # Display message to welcome user

    print("--------------------")

    print("Let's play Three Card Poker!")

   

    # Get number of players & rounds from user, confirm numbers inputted

    num_players = int(input("First, tell us how many people are playing today: "))

    num_rounds = int(input(f"{num_players} players today? Great! Now, how many rounds would you like to play? "))

    print(f"{num_rounds}? Sounds good! Now, let's go over our rules:")

   

    # Display rules

    print("1) First, players will place an ante bet at the start of the round.")

    print("2) Players can also play an optional 'Pair Plus' bet.")

    print("3) The dealer and each player are dealt three face-down cards each")

    print("4) Players will look at their cards and decide to fold or play:")

    print("\t Fold: Forfeit your hand and lose your bets")

    print("\t Play: Place an additional play bet (equal to your ante bet) and compete against the dealer.")

    print("5) The dealer reveals their three cards and each player who decided to play will compare their hand's to the dealer's.")

    print("~COMPARISON RULES!~")

    print("If the dealer's hand does not contain a Queen or better, the dealer does not qualify and the player wins their bet back.")

    print("If the dealer's hand does have a Queen or higher, the hands are compared:")

    print("\tIf the player's hand is higher ranked, they win their ante and play bets back (1:1)")

    print("\tIf the player's hand is lower ranked or the rank ties, they lose both their bets")

    print("6)If the player played a pair plus bet, they will receive a payout based on their hand's strength, regardless of the dealer's hand:")

    print("~RANKING RULES!~")

    print("# 1. Straight Flush - three consecutive cards of same suit (40:1 Pair Plus payout)\n"

            "# 2. Three of a Kind - three cards of same number (30:1 Pair Plus payout)\n"

            "# 3. Straight - three consecutive cards of different suits (6:1 Pair Plus payout)\n"

            "# 4. Flush - three cards of same suit, non-consecutive (4:1 Pair Plus payout)\n"

            "# 5. Pair - two cards of the same rank, third card unmatched (1:1 Pair Plus payout)\n"

            "# 6. None - Take highest rank card of each deck, compare (no Pair Plus payout)")

    print("7) The game runs for how ever many rounds the player wants or until the player(s) run out of money.")

    print("Now, let's play!")

    print("--------------------")

   

    # Return number of players & rounds to main

    return num_players, num_rounds

 

# For num of rounds entered  

    # Placing Bets

        # Take Ante Bet (bet = 100 - some num of chips)

            # 100 is base amt for every player, need to keep track of each players chips b/w rounds

        # Option for pair plus bet

            # If yes, take another chip amount, mark a pair_plus as TRUE

            # If no, mark a pair_plus as FALSE

 

    # Draw Cards

        # Array with 52 cards

        # Dealer gets three cards, remove from deck

            # confirmation message

        # for each player

            # 3 cards each, remove from deck

            # display cards to each player, confirmation

 

    # For num of players in game

        # Player choice after getting cards

            # Make choice to

                # Fold: forfeit hand and lose their ante bet (and pair plus, if applicable)

                # Play: place additional bet (equal to their ante bet) and compete against dealer

 

        # Compare w/ dealer

            # If dealer's hand does not contain queen or better, does not qualify

                # Player wins back their ante bet

            # If dealer's hand qualifies

                # Rank player and dealer hands

                    # If player's hand rank is higher

                        # Win both ante and pair play bets

                    # If player's hand rank is lower or ties

                        # Loses both bets

 

# Rankings (highest to lowest)

# 1. Straight Flush - three consecutive cards of same suit

# 2. Three of a Kind - three cards of same rank (number)

# 3. Straight - three consecutive cards of different suits

# 4. Flush - three cards of same suit, non-consecutive

# 5. Pair - two cards of the same rank, third card unmatched

# 6. None - Take highest rank card of each deck, compare

 

# Main

def main():
  

    # Get number of players and rounds to play

    num_players, num_rounds = main_menu()

   

    # Repeat for each number of rounds

    # for i in range(num_rounds):

    #     print(f"Round {i}!")

       

        # Game logic

 

if __name__ == "__main__":

    main()