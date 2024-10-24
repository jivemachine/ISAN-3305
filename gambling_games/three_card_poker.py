# Authors: Jeremy Cobb, John Courtright, Stanley Odiase
# Instructor: Zachary Kelley
# ISAN 3305: Business Programming I
# Three Card Poker interactive game
import random

# Constants
STARTING_FUNDS = 100.00 # every player starts w/ $100.00
RANK_MAP = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 
            'J': 11, 'Q': 12, 'K': 13, 'A': 14} # Map card values to numeric ranks (so characters can be compared to nums)

# Start-up: Basic UI for user, get number of players & rounds to play as inputs, pass them back to main
def main_menu():
    # Display message to welcome user
    print("--------------------")
    print("Let's play Three Card Poker!")
    
    # Get number of players & rounds from user, confirm numbers inputted 
        # .strip() to get rid of any whitespace and prevent errors
    while True:
        num_players = int(input("First, tell us how many people are playing today (1-16): ").strip())
        if 1 <= num_players <= 16: # max amount of players given 3 cards/player and 3 cards/player for the dealer in a round
            break
        print("Please enter a valid number of players between 1 and 16.")

    num_rounds = int(input(f"{num_players} players today? Great! Now, how many rounds would you like to play? ").strip())

    print(f"{num_rounds}? Sounds good! Now, let's go over our rules:")
    
    # Display rules for game, ranking, bets
    print("1) First, players will place an ante bet at the start of the round.")
    print("2) Players can also play an optional 'Pair Plus' bet.")
    print("3) The dealer and each player are dealt three face-down cards each")
    print("4) Players will look at their cards and decide to fold or play:")
    print("\t Fold: Forfeit your hand and lose your bets")
    print("\t Play: Place an additional play bet (equal to your ante bet) and compete against the dealer.")
    print("5) The dealer reveals their three cards and each player who decided to play will compare their hand's to the dealer's.\n")
    print("~COMPARISON RULES!~")
    print("If the dealer's hand does not contain a Queen or better, the dealer does not qualify and the player wins their bet back.")
    print("If the dealer's hand does have a Queen or higher, the hands are compared:")
    print("\tIf the player's hand is higher ranked, they win their ante and play bets back (1:1)")
    print("\tIf the player's hand is lower ranked or the rank ties, they lose both their bets")
    print("6)If the player played a pair plus bet, they will receive a payout based on their hand's strength, regardless of the dealer's hand:\n")
    print("~RANKING RULES!~")
    print("# 1. Straight Flush - three consecutive cards of same suit (40:1 Pair Plus payout)\n"
            "# 2. Three of a Kind - three cards of same number (30:1 Pair Plus payout)\n"
            "# 3. Straight - three consecutive cards of different suits (6:1 Pair Plus payout)\n"
            "# 4. Flush - three cards of same suit, non-consecutive (4:1 Pair Plus payout)\n"
            "# 5. Pair - two cards of the same rank, third card unmatched (1:1 Pair Plus payout)\n"
            "# 6. None - Take highest rank card of each deck, compare (no Pair Plus payout)\n")
    print("7) The game runs for how ever many rounds the player wants or until the player(s) run out of money.")
    print("Now, let's play!")
    print("--------------------")
    
    # Return number of players & rounds to main
    return num_players, num_rounds

# Function to generate a deck of 52 cards - Provided by Professor Kelley
def generate_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # Array of the suits
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # Array of the values/ranks of the cards
    
    # Create a deck as an array of tuples (numeric_id, value, suit)
    # Creates an array of 52 cards with:
        # An index value
        # Value/Rank determined by the remainder of the current index and 13 (# of ranks/suit)
        # Suit determined by the integer quotient of the current index divided by 13
    deck = [(i, values[i % 13], suits[i // 13]) for i in range(52)]
    
    random.shuffle(deck)
    return deck # Pass deck to main

# Function to generate array of players for a game
def generate_players(num_players):
    
    # Empty dictionary to hold all players their hands and their chips
    players_master_dict = {}
    
    # Add dealer outside of loop, they get no chips :(
    players_master_dict["dealer"] = {"hand": "", "chips": 0}
    
    # All players as indicated in num_players argument
    for i in range(1, num_players+1): # + 1 because dealer
        player_name = f"Player {i}"
        players_master_dict[player_name] = {"hand": "", "chips": STARTING_FUNDS}
        
    return players_master_dict

# Function to generate a hand of cards for a player
def generate_hand(deck):
    
    # Empty array for the hand
    hand = []
    
    # Randomly selects a card from the deck, pops it, and appends it to the hand array
    # Selects 3 cards
    for i in range(3):
        hand.append(deck.pop())
    
    # Pass hand back
    return hand

# Function to sort a hand in increasing order by rank
def sort_hand(hand):
    # lambda function necessary so max() uses numeric rank from RANK_MAP for comparisons
    sorted_hand = sorted(hand, key=lambda card: RANK_MAP[card[1]])
    return sorted_hand

# Function that handles the betting process
def betting(player_list, player_key):
    # Display current chip amount
    print(f"{player_key} remaining chips: {player_list[player_key]['chips']}")
    # Loop to ensure valid bet
    while True:
        try:
            # Place the initial bet as a float (allowing decimals)
            bet = float(input("Please enter your bet for this round: ").strip())
            # If bet exceeds current chips, prompt the user again
            if bet > player_list[player_key]['chips']:
                print("You do not have sufficient chips for that bet. Please enter a lower amount.")
            elif bet <= 0:
                print("The bet must be greater than zero. Please enter a valid amount.")
            else:
                # Valid bet, exit the loop
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # Subtract ante bet from their total chips
    player_list[player_key]["chips"] -= bet
    return bet

# Function handles wether player has enough chips to bet or not
def validate_bet(player_list, player_key):
    if player_list[player_key]['chips'] <= 0:
        return False
    else:
        return True

# Function that adds ante and play bets back to player's chips if they win
def add_ante_play_bets(player_list, player_key, ante, play):
    player_list[player_key]["chips"] += ante + play

# Function that adds pair plus bets back to player's chips if they have a match
def add_pair_plus_bets(player_list, player_key, bet, rank):
    
    # Pair 1:1
    if rank == 2:
        player_list[player_key]["chips"] += bet
    # Flush 4:1
    if rank == 3:
        player_list[player_key]["chips"] += (bet * 3)
    # Straight 6:1
    if rank == 4:
        player_list[player_key]["chips"] += (bet * 6)
    # ToK 30:1
    if rank == 5:
        player_list[player_key]["chips"] += (bet * 30)
    # Straight Flush 40:1
    if rank == 6:
        player_list[player_key]["chips"] += (bet * 40)
    
# Function that handles the prompt for pair plus betting
def ask_pair_plus_bet():
    # Loop until the player enters a valid response ('y' or 'n')
    while True:
        pair_plus_choice = input("Would you like to play a Pair Plus bet this round? (Y/N): ").strip().lower()     
        if pair_plus_choice in ['y', 'n']:
            return pair_plus_choice  # Return the valid choice
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
    
            
# Function that handles the prompt for playing or folding
def ask_play_choice():
    # Loop until the player enters a valid response ('y' or 'n')
    while True:
        play_choice = input("Would you like to fold or play this round? (P/F): ").strip().lower()
        
        if play_choice in ['p', 'f']:
            return play_choice  # Return the valid choice
        else:
            print("Invalid input. Please enter 'P' for play or 'F' for fold.")

# RANKING ALGORITHM (highest to lowest)
def ranking(hand):
    ranks = sorted([RANK_MAP[card[1]] for card in hand], reverse=False)  # Access card[1] for value, assign rank from rank map, ascending order
    suits = [card[2] for card in hand]  # Access card[2] for suit
    
    hand_rank = straight_flush(ranks, suits, hand)
    
    return hand_rank

# 1. Straight Flush - three consecutive cards of same suit
def straight_flush(ranks, suits, hand):
    is_flush = len(set(suits)) == 1 # List of suits seen in the hand is only 1 "suit-long" 
    is_straight = ranks[0] - ranks[1] == 1 and ranks[1] - ranks[2] == 1 # Difference between card 1 and 2 is 1 and card 2 and 3 is 1
    if is_flush and is_straight:
        return 6
    else:
        return three_of_a_kind(ranks, suits, hand)

# 2. Three of a Kind - three cards of same rank (number)
def three_of_a_kind(ranks, suits, hand):
    is_three_of_a_kind = ranks[0] == ranks[1] == ranks[2] # Ranks are all the same
    if is_three_of_a_kind:
        return 5
    else:
        return straight(ranks, suits, hand)

# 3. Straight - three consecutive cards of different suits
def straight(ranks, suits, hand):
    is_straight = ranks[0] - ranks[1] == 1 and ranks[1] - ranks[2] == 1
    if is_straight:
        return 4
    else:
        return flush(ranks, suits, hand)

# 4. Flush - three cards of same suit, non-consecutive
def flush(ranks, suits, hand):
    is_flush = len(set(suits)) == 1 
    if is_flush:
        return 3
    else:
        return pair(ranks, hand)

# 5. Pair - two cards of the same rank, third card unmatched
def pair(ranks, hand):
    is_pair = ranks[0] == ranks[1] or ranks[1] == ranks[2] or ranks[0] == ranks[2]  # Checks any combination of two matching
    if is_pair:
        return 2
    else:
        return find_max_card(hand) / 10 # Converts to a float w/ 1 decimal place

# 6. None - Take highest rank card of each deck, compare
def find_max_card(hand):
    # lambda function necessary so max() uses numeric rank from RANK_MAP for comparisons
    max_card = max(hand, key=lambda card: RANK_MAP[card[1]])
    # Return the rank corresponding to the value of the highest-ranking card
    return RANK_MAP[max_card[1]]

# Function that prints a summary of the game
def print_summary(player_list):
    print("-------------------")
    for player_key, player_info in player_list.items():
        # Skip dealer in the summary
        if player_key == "dealer":
            continue
        
        final_chips = player_info["chips"]
        difference = final_chips - STARTING_FUNDS  # Calculate difference from starting amount
        
        # Display the player's name, final chips, and difference
        if difference >= 0:
            print(f"{player_key}: Final Chips = ${final_chips:.2f} (Earnings: +${difference:.2f})")
        else:
            print(f"{player_key}: Final Chips = ${final_chips:.2f} (Earnings: ${difference:.2f})")

# Main 
def main():
    # Get number of players and rounds to play
    num_players, num_rounds = main_menu()
    # Create array of players + dealers
    player_list = generate_players(num_players)
    # print(player_list)
    
    # Repeat for each number of rounds
    for i in range(num_rounds):  
        
        # Generate the 52-card deck (w/ method from Kelley)
            # Because we're removing cards, need to regenerate
        deck = generate_deck()

        print(f"Round {i+1}!")
        
        # Game logic for each player
        for i in range(num_players):
            
            # Deal a sorted hand to the dealer
            player_list["dealer"]["hand"] = sort_hand(generate_hand(deck))
            dealer_rank = ranking(player_list["dealer"]["hand"]) # rank their hand 
            
            print(f"Player {i+1}'s turn: ")
            # Set key for the player list for this round
            player_key = f"Player {i+1}"
            
            # Initialize player_rank
            player_rank = None  # Start with None
            
            # Check if the player has any chips left
            if player_list[player_key]["chips"] <= 0:
                print(f"{player_key} has no chips left and will skip this round.")
                continue  # Skip to the next player if they have no chips
                        
            # 1) Player places an ante bet
            # validate player has chips to bet
            if validate_bet(player_list, player_key):
                ante_bet = betting(player_list, player_key)
            else:
                ante_bet = 0
                
            
            # 2) OPTIONAL: Player may elect to place a pair plus bet
            if validate_bet(player_list, player_key):
                pair_plus_choice = ask_pair_plus_bet()
            else:
                pair_plus_choice = 'n'
                
            # Print confirmation for user
            if pair_plus_choice == 'y':
                print("Player has chosen to place a Pair Plus bet.")
                # Make the bet
                pair_plus_bet = betting(player_list, player_key)
                
            else:
                print("Player has chosen not to place a Pair Plus bet.")
            
            # 3) Deal cards to player (sorted)
            player_list[player_key]["hand"] = sort_hand(generate_hand(deck))
            
            # 4) Display hand to player
            print("Here's your current hand:")
            print(f"{player_key} hand: {player_list[player_key]['hand']}")
            
            # 5) Ask player if they'd like to fold or play this hand
            play_choice = ask_play_choice()
            
            # 6a) If the player folded
            if play_choice == "f":
                print("Player has folded and will lose their bet this round.")
            
            # 6b) If the player played
            else:
                
                # Take additional bet
                if validate_bet(player_list, player_key):
                    play_bet = betting(player_list, player_key)
                else:
                    play_bet = 0
                
                # Check if dealer has a Queen (ranked 12) or higher
                if find_max_card(player_list["dealer"]["hand"]) >= 12:
                    player_rank = ranking(player_list[player_key]["hand"])
                    if player_rank > dealer_rank:
                        print("Your hand ranked higher than the dealer's! Here's your winnings:")
                        add_ante_play_bets(player_list, player_key, ante_bet, play_bet)
                    if dealer_rank >= player_rank:
                        print("Your hand ranked lower or tied with the dealer's... You've lost your bets.")
                else:
                    # Player gets bets back
                    print("The dealer did not have a Queen or higher and did not qualify. You've earned your bets back!")
                    # add bets back to players chip count
                    add_ante_play_bets(player_list, player_key, ante_bet, play_bet)
                pass
            
            # 7) Pair Plus Bet, happens regardless of player's choice of playing/folding
            if pair_plus_choice == "y":
                # If rank matches a pair plus rank
                if player_rank in [2, 3, 4, 5, 6]:
                    print("You have a match! Here's your Pair Plus winnings:")
                    add_pair_plus_bets(player_list, player_key, pair_plus_bet, player_rank)
                else:
                    print("No Pair Plus match found. Pair Plus bet is lost.")
        
    # End game
    print("The game is over! Here are the results:")
    # Print summary of the game (total winnings or losses for each player)
    print_summary(player_list)
    print("Thank you for playing Three Card Poker!")
        
if __name__ == "__main__":
    main()
