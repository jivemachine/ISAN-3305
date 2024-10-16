import random as r

# Three Card Poker is played as heads-up between the player's hand and the dealer's hand.
# After all ante wagers are placed, three cards are dealt to each player and the dealer. 
# Players have a choice to either fold or continue in the game by placing a "play" wager equal to their ante. 
# Hands are then exposed and wagers resolved.[6]
# The dealer's hand must be Queen high or better for the dealer hand to play. 
# If the dealer does not play, then there is no action on play wagers and ante wagers are paid 1 to 1.
# If the dealer does play, the dealer and player hands are compared. If the player hand loses, both the ante and play wagers are lost. 
# If the player hand wins, both the ante and play wagers are paid 1 to 1. If the hands are tied, then there is no action on either wager.[6]
# Additional optional bets are offered. The Pair Plus wager is a bet that the player's hand will 
# be a pair or better. The Pair Plus wager wins if the player has at least a pair of twos. The payoff applies regardless of the dealer's hand, as the Pair 
# Plus wager is not in competition against the dealer's hand. Some casinos also offer an Ante Bonus, which is paid on the 
# ante wager for a straight or better. The typical Ante Bonus paytable pays 5 to 1 for a straight flush, 4 to 1 for a three of a kind, 
# and 1 to 1 for a straight. Like the Pair Plus wager, the Ante Bonus pays regardless of whether that hand beats the dealer's hand.[6]


# starting game:

# get # of players
# hand out tokens for betting 


# actual game:
# 3 cards delt to each player & dealer
# players can either fold or continue
# dealer can only play if they have a queen or better
# 

# resolve

# def create_deck(delt_cards = []):
#     deck = []
#     for i in range(0, 52):
#         deck.append(i)
        
#     if deck not in delt_cards:
#         return deck
#     else:
#         for delt_cards in deck:
        
#     return deck
    
    


def main():
    # deck = create_deck()
    # print(deck)
    # deck = [0, 1, 2]
    # delt = [1]
    # for i in delt:
    #     print(i)
    #     if i in deck:
    #         print(i)
    #         deck.remove(i)
            
    # deck = deck.pop(delt)
    
    # print (delt)
        
    # print(deck)
    deck = [0,1,2,3,4,5]
    delt_cards = [4, 3, 5]
    for i in delt_cards:
        if i in deck:
            deck.remove(i)
        
    print (delt_cards) # [4, 3, 5]
    print (deck)       # [0, 1, 2]
    
    
# deck = [0,1,2,3,4,5]
# delt_cards = [4, 3, 5]
# for i in delt_cards:
#     if i in deck:
#         deck.remove(i)
        
# print (delt_cards)
# print (deck)
    
    
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
# gameplay welcome menu
# ask user how many players are playing
# user inputs integers
#| ---------------- |
#| --- welcome ---- |

# game starts
# goes through each player and asks them for their ante bet
# then before to the next player asks if they want to do a pair plus bet
# does the same for every player

# dealing loop
# dealer hands out 3 cards for every player including themselves
# _ range (0, 4)
#   _ range(0, 12)
# something like this to start out and assign eahc player an arry tha is their hand

# once every player is delt their cards
# ask user if they want to enter a second ante bet or fold
    # folding 
    # deducts original ante bet from their chips
    # ante adds additional chips to original bet
# resolve
# dealer showing their hands 
# each player is told if they beat the dealer or not
# then if they played a pair plus bet, that is also deducted or add to their chips
# depending on the outcome

#deck [0-51]
#player1_hand = []



# def numbers_(num):
#    for i in num:
        



# prefessor Kelleys code for: 
# generating a deck of cards
# getting the card name 
# shuffeling the deck of cards
# selecting a random card


#import random

# Function to generate a deck of 52 cards
# def generate_deck():
#     suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
#     values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
#     # Create a deck as an array of tuples (numeric_id, value, suit)
#     deck = [(i, values[i % 13], suits[i // 13]) for i in range(52)]
#     return deck

# Function to get the string representation of a card from its numeric identifier
# def get_card_name(numeric_id):
#     deck = generate_deck()
#     _, value, suit = deck[numeric_id]
#     return f"{value} of {suit}"

# Function to shuffle the deck
# def shuffle_deck(deck):
#     random.shuffle(deck)
#     return deck

# Function to randomly select a card from the deck
# def select_random_card(deck):
#     return random.choice(deck)

# Example usage
# deck = generate_deck()
# print(f"Generated Deck: {deck}\n")

# shuffled_deck = shuffle_deck(deck)
# print(f"Shuffled Deck: {shuffled_deck}\n")

# selected_card = select_random_card(shuffled_deck)
# print(f"Randomly Selected Card: {get_card_name(selected_card[0])} (ID: {selected_card[0]})")

