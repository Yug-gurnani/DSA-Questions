# -*- coding: utf-8 -*-
"""
Spyder Editor

Author Sam / Kaydee
"""

import random
class bankAccount():
    
    def __init__(self,name,amount):
        self.name = name 
        self.amount = amount
        
    def bet(self,b):
        self.b = b
        if self.b > self.amount:
            print("Not enough funds")
            print("Restarting game")
            driver_core()
        else:
            self.amount -= self.b
            print("Bet placed")
        
class deck_hand():
    def __init__(self):
        self.deck = []
    
            
        
class blackJack():
    def __init__ (self, deck):
        self.deck = deck
        self.player = ['P']
        self.dealer = ['D']
        self.final_player_sum = []
    
    def play(self):
        self.player = self.start(self.player)
        self.dealer = self.start(self.dealer)
        
        self.show_deck(self.dealer)
        self.show_deck(self.player)
        self.final_player_sum.append(self.deck[self.player[1]][1])
        self.final_player_sum.append(self.deck[self.player[2]][1])
        
        print("Your deck current total : {}".format(sum([self.deck[self.player[1]][1], self.deck[self.player[2]][1]])))
        self.turn()
        pass
    
    
    
    def start(self,pdeck):
        for i in range(2):
            pdeck.append(random.randint(1,13))
        return pdeck
    def show_deck(self,sdeck):
        if sdeck[0] == 'D':
            print("Dealer Deck(One card is hidden) :")
            self.card(self.dealer[1:-1])
        elif sdeck[0] == 'T':
            print("Dealer's full deck : ")
            self.card(self.dealer[1:])
        else:
            print("Player Deck :")
            self.card(self.player[1:])
            
    def turn(self):
        
        isHit = False
        
        cmd = input("Hit or Stay : ")
        if cmd == "hit" or cmd == "Hit":
            isHit = True
        self.hit_or_stay(isHit)
        
        
        
    def replay(self):
        print("Do you want to Play Again Yes/No")
        y = input()
        if y == 'yes' or y == 'Yes':
            driver_core()
        else:
            print('Game Ended \nThanks For Playing!')
        
    
    def hit_or_stay(self,isHit):
        
        if isHit:
            p_deck_sum = []
            self.player.append(random.randint(1,13))
            for i in range(1,len(self.player)):
                p_deck_sum.append(self.deck[self.player[i]][1])
            self.show_deck(self.dealer)
            self.show_deck(self.player)
            print("Your deck current total : {}".format(sum(p_deck_sum)))
            if sum(p_deck_sum) > 21:
                print("You busted")
            elif sum(p_deck_sum) == 21:
                print("BLACKJACK!! You won!!")
            else:
                self.final_player_sum = p_deck_sum
                self.turn()
            
        else:

            
            self.dealer_reveal()
    def dealer_reveal(self):
        d_deck_sum = []
        self.dealer[0] = 'T'
        print("Now playing : Dealer")
        self.show_deck(self.dealer)
        for i in range(1,len(self.dealer)):
                d_deck_sum.append(self.deck[self.dealer[i]][1])
                
        if sum(d_deck_sum) <= 17:
            print('Dealer is Taking A Card')
            self.hit_dealer(True)
            
        elif sum(d_deck_sum) > 17:
            if sum(d_deck_sum) > 21:
                if 11 in d_deck_sum:
                    d_deck_sum.remove(11)
                    d_deck_sum.append(1)
            print("Dealer total : {}, Your total : {}".format(sum(d_deck_sum),sum(self.final_player_sum)))
           
            if sum(d_deck_sum)>21:
                print("Dealer Busted, You won!")
            elif sum(d_deck_sum) <= 17:
                self.hit_dealer(True)
            elif sum(d_deck_sum) > 17:
                print("Dealer total : {}, Your total : {}".format(sum(d_deck_sum),sum(self.final_player_sum)))
                if sum(d_deck_sum) > sum(self.final_player_sum):
                    print("Dealer sum is higher, you lost!")
                else:
                    print("Your sum is higher, you won!")
                        
            else:
                if sum(d_deck_sum) > sum(self.final_player_sum):
                    print("Dealer sum is higher, you lost!")
                else:
                    print("Your sum is higher, you won!")
        
    def hit_dealer(self,isHit):
         d_deck_sum = []
         if isHit:
             self.dealer.append(random.randint(1,13))
             for i in range(1,len(self.dealer)):
                d_deck_sum.append(self.deck[self.dealer[i]][1])
             self.show_deck(self.dealer)
             self.show_deck(self.player) 
             self.dealer_reveal()
     
                 
                 
                
            
        
    
    def card(self,c):
        
        
        for i in c:
            
           
           
           print("+-----+")
           print("|{0}    |".format(self.deck[i][2]))
           print("|     |")
           print("|    {0}|".format(self.deck[i][2]))
           print("+-----+")       
        
            
 

def deck_init(deck):   
    for i in range(2,11):
        deck[i] = [4,i,str(i)]
    
    deck[1]  =  [4,11,'A']
    deck[11] = [4,10,'J']
    deck[12] = [4,10,'Q']
    deck[13] = [4,10,'K']
    return deck
    




def driver_core(): 
    deck = {}
    deck = deck_init(deck)
    name = input("Enter your name : ")
    amt = int(input("Enter the amount : "))
    playerAC = bankAccount(name,amt)
    bet_call = int(input("Enter bet amount : "))
    playerAC.bet(bet_call)
    table(deck)
    
    
    
def table(deck):
    game = blackJack(deck)
    game.play()
    game.replay()
    
    
        
deck = {}

driver_core()
        
