#-------------------------------------------------------------------------------
# The "newtable" class takes care of all the table actions in the game.
# It is loaded as the "croupier" in the main game.
#
# Local dependencies: player class, treys/Card class, holdem_probs/holdem_calc
#
# Author: Pablo Loren-Aguilar
#-------------------------------------------------------------------------------
import random as rnd
import include.player as player
from include.treys.treys import Card
import pygame
from include.holdem_probs import holdem_calc

hand_rankings = ("High Card", "Pair", "Two Pair", "Three of a Kind",
                 "Straight", "Flush", "Full House", "Four of a Kind",
                 "Straight Flush", "Royal Flush")
pygame.init()

class newtable():
    def __init__(self, nplay, players):
        self.pot = 0
        self.common_cards  = []
        self.common_suits  = []
        self.players_order = [x for x in range(nplay)]
        self.bet_order     = [x for x in range(nplay)]
        self.nactive       = nplay
        
        for n in range(nplay):                           #Sit the players in the table
            if (n == 0):
                players.append(player.newplayer(1))
            else:
                players.append(player.newplayer(0))
      
    def set_common(self,deck):
        self.common_cards = deck.draw(5)
        print(self.common_cards)
    
    def show_common(self):
        print('\nThe common cards are:',Card.print_pretty_cards(self.common_cards))
            
    def clean_common(self):
        self.common_cards.clear()
        
    def set_dealer(self,players):        
        nplay = int(len(self.players_order))
        players_order = self.players_order    
         
        players_sort = players_order[0]
        for n in range(int(len(players_order))-1):
            players_order[n]   = players_order[n+1]
        players_order[nplay-1] = players_sort
        
        new_players_order = []
        for i in range(int(len(players_order))):
            if (players[players_order[i]].active == True):
                new_players_order.append(players_order[i])                
        self.players_order = new_players_order

    def set_bet(self,bet):
        nplay = len(self.players_order)
        self.bet_order.clear()
        if (bet == 'preflop'):
            #Order to bet in pre-flop
            if (nplay > 3):
                self.bet_order.append(self.players_order[3])
                self.bet_order.append(self.players_order[4])
                self.bet_order.append(self.players_order[5])
                self.bet_order.append(self.players_order[0])
                self.bet_order.append(self.players_order[1])
                self.bet_order.append(self.players_order[2])
            elif (nplay == 3):
                self.bet_order.append(self.players_order[0])
                self.bet_order.append(self.players_order[1])
                self.bet_order.append(self.players_order[2])
            elif (nplay == 2):
                self.bet_order.append(self.players_order[0])
                self.bet_order.append(self.players_order[1])
        else:
            #Order to bet post-flop
            if (nplay > 3):
                self.bet_order.append(self.players_order[1])
                self.bet_order.append(self.players_order[2])
                self.bet_order.append(self.players_order[3])
                self.bet_order.append(self.players_order[4])
                self.bet_order.append(self.players_order[5])
                self.bet_order.append(self.players_order[0])
            elif (nplay == 3):
                self.bet_order.append(self.players_order[1])
                self.bet_order.append(self.players_order[2])
                self.bet_order.append(self.players_order[0])
            elif (nplay == 2): 
                self.bet_order.append(self.players_order[1])
                self.bet_order.append(self.players_order[0])                
            
    def set_hand(self,players,deck):
        for person in players:
            person.cards = deck.draw(2)
            
    def bet_round(self,screen,surface,card,players,n):
        #Reveal common cards (if necessary)
        screen.show_common(surface,self.common_cards,n)
        pygame.display.update()

        #Start round of bets.
        pot    = 0
        tocall = 0
        for i in range(len(self.bet_order)):
            if (players[self.bet_order[i]].folded == False):
                blind = False
                if (n == 'preflop'):
                    if (i == len(self.bet_order)-1 or i == len(self.bet_order)-2):
                        blind = True
                else:
                    if (i == 0 or i == 1):
                        blind = True
 
                position = 'early'
                if (self.nactive > 1):
                    if (players[self.bet_order[i]].id == 1):
                        amount = int(players[self.bet_order[i]].bet(surface, screen))
                    else:
                        amount = int(players[self.players_order[i]].aibet(surface, card, players[self.bet_order[i]].cards, self.common_cards, self.pot, tocall, position, n))
                    
                    if (amount >= 0):
                        pot += amount
                        screen.put_chips(surface,self.bet_order[i],self.bet_order[i],blind,amount,n)
                        pygame.display.update()
                    else:
                        screen.player_folds(surface,self.bet_order[i])
                        players[self.bet_order[i]].folded = True
                        self.nactive -= 1
                print('Player #',i,' bets',amount)
                pygame.time.delay(500)
                #pygame.display.update()   

        #Clean the chips after the round ends (chips are already in the pot)
        screen.remove_chips(surface)
        screen.update_pot(surface, self.pot)              
        self.pot += pot
        pygame.display.update()   
    
    def show_pot(self):
        return self.pot
    
    def check_winner(self,screen,surface,players,card):
        if (self.nactive == 1):
            rect = pygame.Rect(100, 1000, 1075, 100)
            pygame.draw.rect(surface, (255,255,255), rect)
            pygame.draw.rect(surface, (255,255,255), rect, 1)
            font = pygame.font.SysFont('Tahoma', 30, True, False)
            text = font.render("Press s to continue the game or x to quit", True, (0, 0, 0))
            surface.blit(text, (325,1100))
            
            text = font.render("Active player wins the pot", True, (0, 0, 0))
            surface.blit(text, (325,1000))
        else:
            #hand_str = []
            #for player in players:
            #    if player.folded == False:
            #        for cards in player.cards:
            #            hand_str.append(card.int_to_str(cards))
            hand_str = []
            for player in players:
                for cards in player.cards:
                    hand_str.append(card.int_to_str(cards))
                
            board_str = []
            for cards in self.common_cards:
                board_str.append(card.int_to_str(cards))

            result = holdem_calc.calculate(board_str, False, 10, None, hand_str,False)          
            for indx,player in enumerate(players):
                if player.folded == True:
                    result[0][indx+1] = -1
            winner = result[0].index(max(result[0]))
            
            best_hand = 0
            for item in result[1]:
                best_hand = max(best_hand,item[1].index(max(item[1])))
  
            #Show cards
            for indx,player in enumerate(players):
                if (indx > 0):
                    if (player.folded == False):
                        screen.player_cards(surface,player.cards,indx)
                        pygame.display.update()

            rect = pygame.Rect(100, 1000, 1075, 500)
            pygame.draw.rect(surface, (255,255,255), rect)
            pygame.draw.rect(surface, (255,255,255), rect, 1)
        
            font = pygame.font.SysFont('Tahoma', 30, True, False)
            text = font.render("Press s to continue the game or x to quit", True, (0, 0, 0))
            surface.blit(text, (325,1100))
                           
            if (winner == 0):
                #We need now to find out a way to distinguish between the hands
                #High Card.
                high_bin = []
                for player in players
                high_bin.append(max(hand_bin1))
                high_bin.append(max(hand_bin2))
                
                #Pairs + Kicker
                
                #Double Pairs
                
                #Three of a kind
                
                #Straight
                
                #Flush
                
                #Full House
                
                #Four of a kind
                
                #Straight Flush
                
                #Royal Flush              
                
                text=font.render("No winner, shared pot. Best hand is "+hand_rankings[best_hand], True, (0,0,0))
            else:
                text = font.render("Player "+str(winner)+" wins with a "+hand_rankings[best_hand], True, (0,0,0))
            surface.blit(text, (325,1050))

        #Actions in the menu
        game_running = True
        while game_running:
            #Loop through active events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        pygame.quit(); sys.exit()
                    if event.key == pygame.K_s:
                        game_running = False
                pygame.display.update()

