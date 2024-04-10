import random


class GameHandler:
    def __init__(self):
        self.suits = ['Heart','Diamond','Club','Spade']
        self.deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        
    def shuffle(self):
        newdeck = list()
        for x in self.deck:
            for y in self.suits:
                string = f'{x}|{y}'
                newdeck.append(string)
        random.shuffle(newdeck)
        return newdeck
    
    def drawCard(self,deck,playerhand,num):
        if isinstance(deck,list) and isinstance(playerhand,list) and isinstance(num,int):
            count = 0
            while count < num:
                x = deck.pop()
                playerhand.append(x)
                count+=1
        else:
            return 0
        
    def checkHand(self,playerhand):
        if isinstance(playerhand,list):
            count = 0
            ranks = [card.split('|')[0] for card in playerhand]
            for i in ranks:
                if i == 'A':
                    # c = int(input('Enter 1 for Ace to be 1, or 11 for Ace to be 11: '))
                    count+=11
                elif i == 'K' or i == 'Q' or i == 'J':
                    count+= 10
                else:
                    count+= int(i)
            return count       
        else:
            return 0
    
    def print_deck(self, playerhand):
        for i in playerhand:
            print('[' + i + '] ')
        print()
        
            
        
        
        