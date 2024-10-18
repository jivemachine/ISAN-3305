import random as r

# Function to generate a deck of 52 cards
def generate_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    # Create a deck as an array of tuples (numeric_id, value, suit)
    deck = [(i, values[i % 13], suits[i // 13]) for i in range(52)]
    return deck

# def create_players(num_arrays):
#     players_master_array = []
#     for i in range(num_arrays+1): # + 1 because dealer
#         players_master_array.append([])
#     return players_master_array

def create_players(num_players):
    # empty dictionary to hold all players their hands and their chips
    players_master_dict = {}
    
    # add dealer outside of loop
    players_master_dict["dealer"] = {"hand": "", "chips": 0}
    
    # all players as indicated in num_players argument
    for i in range(1, num_players+1): # + 1 because dealer
        player_name = f"player_{i}"
        players_master_dict[player_name] = {"hand": "", "chips": 100, "ante": 0, "pair_plus_wager": 0}
        
    return players_master_dict


def deal_cards(player_number, deck, players_dictionary):
    # for i in num_players:
    # creating players name to find in dictionary
    name = f"player_{player_number}"
    
    # adding delt cards to players hand
    players_dictionary[name]['hand'] = r.choices(deck, k=3)
    # removing delt cards from deck
    for card in players_dictionary[name]['hand']:
        deck.remove(card)
    
    
def deduct_bet_from_players_chips(player_number, bet, players_dictionary):
    name = f"player_{player_number}"
    # removes bet from players chip count and adds to players bet count
    players_dictionary[name]['chips'] -= bet
    players_dictionary[name]['bet'] += bet
    
    
    
    
# def royal_flush(hand):
    
    
    
# def rankings(deck):
    
    
    
    
    

def main():
    deck = generate_deck()
    # print(deck)
    
    all_players = create_players(4)
    # print(all_players)
    
    deal_cards(1, deck, all_players)
    # print(all_players)
    # print(all_players)
    print(deck)
    print("     ")
    print("     ")
    print("     ")
    print("     ")
    print(all_players)
    
    
    
    
if __name__ == '__main__':
    main()