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


def deal_cards(deck, players_dictionary, player_number = None):
    # for i in num_players:
    # creating players name to find in dictionary
    if player_number is None:
        name = "dealer"
    else:
        name = f"player_{player_number}"
        
    
    # adding delt cards to players hand
    players_dictionary[name]['hand'] = r.sample(deck, k=3)
    # removing delt cards from deck
    for card in players_dictionary[name]['hand']:
        deck.remove(card)
    
    
def deduct_bet_from_players_chips(player_number, bet, players_dictionary):
    name = f"player_{player_number}"
    # removes bet from players chip count and adds to players bet count
    players_dictionary[name]['chips'] -= bet
    players_dictionary[name]['bet'] += bet
    
    
    
    
def flush(hand):
    # append all suits in hand to single list
    suits = []
    for card in hand:
        suits.append(card[2])
    
    # if more than 2 suits match
    # append to flush array
    flush = []
    for suit in suits:
        if suits.count(suit) > 2:
            flush.append(suit)
    
    if len(flush) == 3:
        return True
    else:
        return False
 
def convert_str_to_int(str_val):       
    return int(str_val)
    
def straight(hand):
    
    hand_value = []
    
    # appending cards face value to array and converting face cards to numbers as well
    for card in hand:
        if card[1] == 'J':
            hand_value.append('11')
        elif card[1] == 'Q':
            hand_value.append('12')
        elif card[1] == 'K':
            hand_value.append('13')
        elif card[1] == 'A':
            hand_value.append('14')
        else:
            hand_value.append(card[1])
            
    # converting integer strings into actual integers
    # for i in range(0, len(hand_value)):
        # hand_value[i] = int(hand_value[i])
        
    # sorting values    
    # hand_value.sort()
    print(sorted(hand_value, key=convert_str_to_int))
    
# def rankings(deck):
    
    
    
    
    

def main():
    # generates deck
    deck = generate_deck()
    # print(deck)
    
    # generates dictionary of all players 
    # argument one generates dealer + 1 player
    # argument of two would generate dealer + 2 extra players
    all_players = create_players(1)
    # print(all_players)
    
    # deal cards deals cards to one single player 
    # adds the cards as a tuple to the players 
    # dictionary object
    # and thenremoves the delt cards from the deck.
    # the last argument being blank deals to dealer
    # argument of 1 would deal to player_1...etc.
    deal_cards(deck, all_players)
    deal_cards(deck, all_players, 1)
    # print(deck)
    # deal_cards(deck, all_players, 1)
    # print("  ")
    # print(deck)
    
    flush_dealer = flush(all_players['dealer']['hand'])
    straight(all_players['deale']['hand'])
    flush_player_1 = flush(all_players['player_1']['hand'])
    # print(all_players)
    # print(deck)
    # print("     ")
    # print("     ")
    # print("     ")
    # print("     ")
    # print(all_players)
    
    
    
    
if __name__ == '__main__':
    main()