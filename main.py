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
        raise('Input deck, and playerHand needs to be type list. Type action must be string type. See function dealer_turn()')

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
        raise('Input deck, and playerHand needs to be type list. Type action must be string type. See function player_turn()')

def update(key,subkey,value):
    with open('player.json','r') as read:
        x = json.load(read)
        if value == 'wins':
            x[key][subkey][0]["wins"]+=1
        elif value == 'draws':
            x[key][subkey][0]["draws"]+=1
        elif value == 'losses':
            x[key][subkey][0]["losses"]+=1
    read.close()
    with open('player.json','w') as write:
        json.dump(x,write,indent=4)
    write.close()
    
def reset(player_hand, dealer_hand, deck, key):
    if isinstance(deck,list) and isinstance(player_hand,list) and isinstance(dealer_hand,list) and isinstance(key,str):
        player_hand = []
        dealer_hand = []
        deck = []
        deck = ['2','3','4','5','6','7','8','9','10','J','K','Q','A'] * 4
        random.shuffle(deck)
        A = deck.pop()
        B = deck.pop()
        C = deck.pop()
        D = deck.pop()
        player_hand.append(A)
        player_hand.append(B)
        dealer_hand.append(C)
        dealer_hand.append(D)
        key = str(total_hand(player_hand))
    else:
        raise('See function reset()')

def main():
    key = ''
    subkey = ''
    player_hand = list()
    dealer_hand = list()
    deck = list()
    player_choice = ['hit','stand']
    reset(player_hand, dealer_hand, deck, key)
    total = 0
    limit = 100
    while total < limit:
        subkey = random.choice(player_choice)
        player_turn(deck,player_hand,subkey)
        dealer_turn(deck,dealer_hand)
        player_hand_total = total_hand(player_hand)
        dealer_hand_total = total_hand(dealer_hand)
        if (player_hand_total >= 21 and dealer_hand_total >= 21):
            print('Draw!')
            update(key,subkey,'draws')
            reset(player_hand, dealer_hand, deck, key)
        elif player_hand_total == 21:
            print('Player Wins!')
            update(key,subkey,'wins')
            reset(player_hand, dealer_hand, deck, key)
        elif dealer_hand_total == 21:
            print('Player Losses!')
            update(key,subkey,'losses')
            reset(player_hand, dealer_hand, deck, key)
        elif player_hand_total > 21:
            print('Player Losses!')
            update(key,subkey,'losses')
            reset(player_hand, dealer_hand, deck, key)
        elif dealer_hand_total > 21:
            print('Player Wins!')
            update(key,subkey,'wins')
            reset(player_hand, dealer_hand, deck, key)
        else:
            p = 21 - player_hand_total
            d = 21 - dealer_hand_total
            if p < d:
                print('Player Wins!')
                update(key,subkey,'wins')
            else:
                print('Player Losses!')
                update(key,subkey,'losses')
        total+=1
        
main()