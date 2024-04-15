# Zee Pearson
# CIS 2131
# Final Project
# 4/15/24
"""
Dealer logic - stops at 17 or higher _10__/10
player logic randomly picks hit or stand and tracks result _10__/10
displays results for EACH starting value, Win/Loss/Draw count for hit and stand _10__/10
Simulator runs 100,000 times to calculate all the results _10__/10
Presentation and documentation _10__/10
Total _50___/50
"""
# import both json and random built in packages 
import random
import json

def total_hand(hand):
    """
    Total_hand function takes any cards, that are stored in a list, and totals them using the Blackjack card system.
    All the face value cards are worth the face value. 
    Example 2 is worth 2, and so on. A is worth 1 or 11. Queen, King, Jack are all worth 10.  
    The way this program works is if there is an Ace in the hand, and it goes passes 21, then the program will convert the A to 1, otherwise it stays at 11.
    
    How the code works?:
        Declare and initialize count and ace_count.
        Count keeps track of the total value of the hand, while ace_count keeps track of the number of aces.
        Used a for loop to loop through the list.
        Check each index so see if the index is an Ace, Queen, King, Jack.
            If the current 'i' is A:
                then add 11 to count
                increase ace_count by 1
            Else if i in a set that contains {'Q','K','J'}:
                then add 10 to count
            Else:
                convert i into an int, then add it to count
        While count > 21 and ace_count > 0
            subtract 10 from count, so that the Ace can be counted as 11
            subtract 1 from ace_count. This way if there's more than one Ace in the hand, it converts all Ace's to one, since more than one Ace will be a bust. 
        Return count.
            
    
    Parameters:
    hand (list): The list contains any hands that the player, or dealer might have.
    
    Returns:
    count (int): The total value of converted hands in Blackjack.
    
    Raises:
    ValueError: If the parameter value hand is not a list, then it will raise an exception.
    
    Examples:
    >>> hand = ['A','A',5]
    >>> x = total(hand)
    >>> print(x)
    17
    """
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
        if len(hand) == 2:
            if hand[0] == 'A' and hand[1] == 'A':
                return count
        while count > 21 and ace_count > 0:
            count -= 10
            ace_count -= 1
        return count
    else:
        raise('Input hand is not type list. See function total_hand()')

def dealer_turn(deck, dealerHand):
    """
    The dealer_turn function simulates an dealer in Blackjack.
    The dealer already has two cards.
    Based on the two cards, the dealer decides to hit or stand.
    The dealer will continue to draw cards if the total hand is <= 16.
    
    How does the code work?:
    First it checks deck, and dealerHand to make sure they are a list type.
        Then it calculates the total value of the hand, by calling the total_hand function.
        Stores the calculated value in a variable called total.
            In Blackjack the rule is if the dealer hand is less than 16, then it must hit.
                Once the dealer hits, it pops a card off the deck, and stores it in a variable called x.
                Once the card is pop off, then it adds the card to the dealer hand, by appending it to the dealer list.
            Else:
                returns nonthing
    
    Parameters:
    deck (list): Is a list that contains the main deck, that the player, and dealer will draw from.
    dealerHand (list): Is a list that contains only the dealers hand. The player will not be able to access this list.
    
    Returns: 
    None
    
    Raises:
    ValueError: If the parameter value dealerHand and deck are not a list type, then it will raise an exception.
    
    Note:
    The dealer_turn function calls the total_hand function. 
    """
    # This is a safety to check if deck, and dealerHand variable are type list. This way I can access both data types as list.  
    if isinstance(deck,list) and isinstance(dealerHand,list):
        total = total_hand(dealerHand)
        # Dealer draws a card if the total value of the dealer hand is <= 16, otherwise it just stands.
        if total <= 16:
            # Draw a card out of the main deck, by poping it from the deck.
            x = deck.pop()
            # Add that drawn card to the dealer hand, by appending it to the dealer hand list.
            dealerHand.append(x)
        else:
            return
    else:
        raise('Input deck, and playerHand needs to be type list. Type action must be string type. See function dealer_turn()')

def player_turn(deck, playerHand, action):
    """
    This simulates a players turn in Blackjack.
    The player has 2 options, hit or stand.
    If the player hits, then the player will draw a card unless if the total value of the players hand exceeds 21.
    
    How the code works?:
    First it checks to see if the parameters deck, playerHand, and action are a certain data type.
    If not it raises an ValueError.
    If action is equal to 'hit':
        Stored the calculated player hand in a variable called total.
        If the total < 21:
            This means the player hand is not a bust, so that player can draw a card.
            Player will draw a card out from the deck, by poping a value from the deck list.
            Stored that value in a variable called x.
            Add that card to the players hand, by appending that value to the playerHand list.
        Else if action is equal to 'stand':
            I used a return statement so that it exit the fuction.
    
    Parameters:
    deck (list): Is a list that contains the main deck, that the player, and dealer will draw from.
    playerHand (list): Is a list that contains only the player hand. The dealer will not be able to access this list.
    action (str): Is a string type, and will only contain two strings that say hit, or stand.
    
    Returns:
    None
    
    Raises:
    ValueError: The parameter deck and playerHand must be a list type. The parameter action must be a string type.
    """
    # This is a safety to check if deck, and dealerHand variable are type list, and action is string type.
    if isinstance(deck,list) and isinstance(playerHand,list) and isinstance(action,str):
        if action == 'hit':
            total = total_hand(playerHand)
            if total < 21:
                x = deck.pop()
                playerHand.append(x)
        elif action == 'stand':
            return
    else:
        raise('Input deck, and playerHand needs to be type list. Type action must be string type. See function player_turn()')

def update_json(key,subkey,value):
    """
    The update json function will update wins/draws/losses from hit, and stand. 
    Each hit, and stand contains a list, and inside that list is a set of values, wins, draws, losses.
    If the players action is a hit, and wins that hit, then it will add a 1 to wins.
    
    This code, x[str(key)][str(subkey)][0]['wins']+=1, will had 1 to the wins value.
    The variable key contains values ranging from 4-22. ---> x[str(key)]
    The variable subkey contains values ranging from hit, or stand. ---> [str(subkey)]
    The [0] means access the first index of the list. Inside the index will contain a set. ---> [0]
    "wins" is the value in a set, which is a list. ---> ['wins']
    
    Here's what the json looks like:
    '20': { <------------------------------- primary key
        'hit': [ <-------------------------- Subkey
            {
                'wins': 0, <----------------|
                'draws': 0,<----------------| Values that are associated with the subkey.
                'losses': 0<----------------|
            }
        ],
        'stand': [
            {
                'wins': 0,
                'draws': 0,
                'losses': 0
            }
        ]
    },

    Parameters:
    key (string): Is a primary key, and contains the values 4-22.
    subkey (string): Is a subkey of the primary key, and contains values from the players action, such as hit or stand.
    value (string): Is a string that contains the Blackjack outcomes. For each round the player can win the hand, losse, or the hand is a draw. 
    """
    # opens up the json file as read
    with open('player.json','r') as read:
        # load json file in a value called x
        x = json.load(read)
        # checks to see if the value passed is wins, draws, losses
        if value == 'wins':
            x[str(key)][str(subkey)][0]["wins"]+=1
        elif value == 'draws':
            x[str(key)][str(subkey)][0]["draws"]+=1
        elif value == 'losses':
            x[str(key)][str(subkey)][0]["losses"]+=1
    # closes the read file
    read.close()
    # create a new open as write
    with open('player.json','w') as write:
        # dumps the x variable in the same json file as read
        # indent = 4 allows for 4 indent spaces so that json file is not on one single line
        json.dump(x,write,indent=4)
    # closes the write file
    write.close()
    

    
def reset(player_hand, dealer_hand, deck):
    """
    The function reset, resets the game every time the dealer, or player makes Blackjack, or exceeds 21.
    
    Parameters:
    playerHand (list): Is a list that contains only the player hand. The dealer will not be able to access this list.
    dealerHand (list): Is a list that contains only the dealers hand. The player will not be able to access this list.
    deck (list): Is a list that contains the main deck, that the player, and dealer will draw from.
    
    How does it work?:
    Check the instance of all the parameters.
    If player hand, dealer hand, and deck are not list type, then raise an ValueError in the console.
    Clear player_hand so that the player can start with a new hand that is empty.
    Clear the dealer_hand so that the dealer can start with a new hand that is empty.
    Clear the deck so that all 52 cards can be added back.
    Add all the cards back to the deck, by using the append method for deck list.
    Shuffle the new deck, by using the random.shuffle method.
    Have the dealer, and player draw 2 cards each. 
    This is done by popping the main deck, then store it in a variable.
    Once popped then append the cards to either, player hand, or dealer hand.
    
    Returns:
    None
    
    Raises:
    ValueError: All the parameters variables must be list type.
    """
    if isinstance(deck,list) and isinstance(player_hand,list) and isinstance(dealer_hand,list):
        # Clear the list of player_hand, dealer_hand, and the main deck, by calling the clear() function.
        player_hand.clear()
        dealer_hand.clear()
        deck.clear()
        # Onces the deck is clear, add all the cards back to the deck, so that the player, and dealer can draw cards.
        # There is 52 cards in a deck, and each card contains, 4 of the same cards, but with different suits.
        # In Blackjack suits don't matter, so I just copy and paste 2-A 4 times to represent the 52 cards in the deck.
        deck.append('2')
        deck.append('3')
        deck.append('4')
        deck.append('5')
        deck.append('6')
        deck.append('7')
        deck.append('8')
        deck.append('9')
        deck.append('10')
        deck.append('J')
        deck.append('K')
        deck.append('Q')
        deck.append('A')
        deck.append('2')
        deck.append('3')
        deck.append('4')
        deck.append('5')
        deck.append('6')
        deck.append('7')
        deck.append('8')
        deck.append('9')
        deck.append('10')
        deck.append('J')
        deck.append('K')
        deck.append('Q')
        deck.append('A')
        deck.append('2')
        deck.append('3')
        deck.append('4')
        deck.append('5')
        deck.append('6')
        deck.append('7')
        deck.append('8')
        deck.append('9')
        deck.append('10')
        deck.append('J')
        deck.append('K')
        deck.append('Q')
        deck.append('A')
        deck.append('2')
        deck.append('3')
        deck.append('4')
        deck.append('5')
        deck.append('6')
        deck.append('7')
        deck.append('8')
        deck.append('9')
        deck.append('10')
        deck.append('J')
        deck.append('K')
        deck.append('Q')
        deck.append('A')
        # shuffle the deck
        random.shuffle(deck)
        # Lines 296-305 draws 2 cards for both the player and dealer. It draws 4 cards by poping the main deck list, and storing it in a variable called A, B, C, D.
        A = deck.pop()
        B = deck.pop()
        C = deck.pop()
        D = deck.pop()
        # It appends A, B to the players hand, and C, D to the dealer hand, to represent both the player and dealer drawing cards.
        player_hand.append(A)
        player_hand.append(C)
        dealer_hand.append(B)
        dealer_hand.append(D)
    else:
        raise('See function reset()')

def main():
    # Create a variable called key to stored the player starting hand.
    key = ''
    # Create a variable called subkey to stored the player action.
    subkey = ''
    # Create lists called player hand, and dealer hand to stored the cards that the player, or dealer will draw.
    player_hand = list()
    dealer_hand = list()
    # Create list called deck. This will act as the main deck that both the dealer, and player can draw from.
    deck = list()
    # Create list called player choice that will contain the actions of the player.
    player_choice = ['hit','stand']
    # Call the reset function to set the game in motion.
    reset(player_hand, dealer_hand, deck)
    # Initialize key so that it contains the values of the starting player hand.
    key = total_hand(player_hand)
    # Create total so it can keep track of how long should the game run. Also set it = 0.
    total = 0
    # Create limit which sets the limit of how long should the game run.
    limit = 100000
    # This loop will run only when total is less than limit. 
    # Total will increase by one every time the loop finishes.
    while total < limit:
        # Initialize subkey to contain the players actions during this match in Blackjack.
        subkey = random.choice(player_choice)
        # Call the player_turn method which will handle the players action.
        player_turn(deck,player_hand,subkey)
        # Once the player is done, then it is the dealers turn. 
        # Call the dealer_turn method which will handle the dealers action.
        dealer_turn(deck,dealer_hand)
        # Calculate the players hand total and stored it in a variable called player_hand_total.
        player_hand_total = total_hand(player_hand)
        # Calculate the dealer hand total and stored it in a variable called dealer_hand_total.
        dealer_hand_total = total_hand(dealer_hand)
        # If both the dealer and player hand goes passes 21, then it is a tie!
        if (player_hand_total > 21 and dealer_hand_total > 21):
            # This print statement is a debug that helps keep track of the current state of the game.
            print('Draw!')
            update_json(key,subkey,'draws')
            reset(player_hand, dealer_hand, deck)
            key = total_hand(player_hand)
        # If the player gets a Blackjack, the player wins the game.
        elif player_hand_total == 21:
            # This print statement is a debug that helps keep track of the current state of the game.
            print('Player Wins!')
            # Call the update_json fuction to update the games stats.
            update_json(key,subkey,'wins')
            # Because both dealer and player busted out, it must reset the game.
            reset(player_hand, dealer_hand, deck)
            # Stored the starting hand of the player.
            key = total_hand(player_hand)
        # If the dealer gets a Blackjack, the player losses the game.
        elif dealer_hand_total == 21:
            # This print statement is a debug that helps keep track of the current state of the game.
            print('Player Losses!')
            # Call the update_json fuction to update the games stats.
            update_json(key,subkey,'losses')
            # Reset the game, by calling the rest method.
            reset(player_hand, dealer_hand, deck)
            # Stored the starting hand of the player.
            key = total_hand(player_hand)
        elif player_hand_total > 21:
            # This print statement is a debug that helps keep track of the current state of the game.
            print('Player Losses!')
            # Call the update_json fuction to update the games stats.
            update_json(key,subkey,'losses')
            # Reset the game, by calling the rest method.
            reset(player_hand, dealer_hand, deck)
            # Stored the starting hand of the player.
            key = total_hand(player_hand)
        elif dealer_hand_total > 21:
            # This print statement is a debug that helps keep track of the current state of the game.
            print('Player Wins!')
            update_json(key,subkey,'wins')
            reset(player_hand, dealer_hand, deck)
            key = total_hand(player_hand)
        else:
            # Lines 387-397
            # means the player and dealer have not gone over the 21, or made 21 mark.
            # To determine who wins, it subtracts the total value hand from 21, and which is closer to 21 is the winner. In other words which one is smaller is the winner.
            if (21 - player_hand_total) < (21 - dealer_hand_total):
                # This print statement is a debug that helps keep track of the current state of the game.
                print('Player Wins!')
                update_json(key,subkey,'wins')
            else:
                # This print statement is a debug that helps keep track of the current state of the game.
                print('Player Losses!')
                update_json(key,subkey,'losses')
        total+=1
        




main()