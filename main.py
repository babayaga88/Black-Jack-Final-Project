import random
import json
def total_hand(hand):
    if isinstance(hand,list):
        count = 0
        ace_count = 0
        for i in hand:
            if i == 'A':
                count+=11
                ace_count += 1
            elif i in {'Q','K','J'}:
                count+=10
            else:
                count+= int(i)
        while ace_count > 0:
            count -= 10
            ace_count -= 1
        return count
    else:
        raise('Input hand is not type list. See function total_hand()')

def dealer_turn(deck, dealerHand):
    if isinstance(deck,list) and isinstance(dealerHand,list):
        total = total_hand(dealerHand)
        if total <= 16:
            print('debug [dealer has hit!]')
            x = deck.pop()
            dealerHand.append(x)
        else:
            print('debug [dealer has stand!]')
            return
    else:
        raise('Input deck, and playerHand needs to be type list. Type action must be string type. See function total_hand()')

def player_turn(deck, playerHand, action):
    if isinstance(deck,list) and isinstance(playerHand,list) and isinstance(action,str):
        if action == 'hit':
            print('debug [player has hit!]')
            total = total_hand(playerHand)
            if total < 21:
                x = deck.pop()
                playerHand.append(x)
        elif action == 'stand':
            print('debug [player stand!]')
            return
    else:
        raise('Input deck, and playerHand needs to be type list. Type action must be string type. See function total_hand()')

def main():
    player_hand = list()
    dealer_hand = list()
    deck = ['2','3','4','5','6','7','8','9','10','J','K','Q','A'] * 4
    random.shuffle(deck)
    player_choice = ['hit','stand']
    
    total = 0
    limit = 1
    while total < limit:
        choice = random.choice(player_choice)
        player_turn(deck,player_hand,choice)
        dealer_turn(deck,dealer_hand)
        player_hand_total = total_hand(player_hand)
        dealer_hand_total = total_hand(dealer_hand)
        if (player_hand_total >= 21 and dealer_hand_total >= 21):
            print('Draw!')
            pass
        elif player_hand_total == 21:
            print('Player Wins!')
            pass
        elif dealer_hand_total == 21:
            print('Player Losses!')
            pass
        elif player_hand_total > 21:
            print('Player Losses!')
            pass
        elif dealer_hand_total > 21:
            print('Player Wins!')
            pass
        else:
            p = 21 - player_hand_total
            d = 21 - dealer_hand_total
            if p < d:
                print('Player Wins!')
                pass
            else:
                print('Player Losses!')
                pass
        total+=1
        
def update(key,subkey,value):
    with open('player.json','r') as read:
        x = json.load(read)
    read.close()
    return x

def write(data):
    with open('player.json','r') as write:
        json.dump(data,write)
    write.close()