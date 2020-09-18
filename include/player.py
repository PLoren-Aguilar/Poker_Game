#------------------------------------------------------------------
# The "newplayer" class takes care of all the actions done by the
# players in the game.
#
# Local dependecies: cordinates, menu class, holdem_probs/holdem_calc
#
# Author: Pablo Loren-Aguilar
#------------------------------------------------------------------
import pygame
import include.menu as menu
from include.holdem_probs import holdem_calc
from include.coordinates import *

pygame.init()

class newplayer():
    def __init__(self, id):
        self.cards  = []
        self.cash   = 100000
        self.id     = id
        self.active = True
        self.folded = False
    
    def get_cash(self):
        return self.cash
              
    def new_hand(self, cards):
        self.cards = cards
        
    def show_hand(self,cards):
        for card in self.cards:
            cards.get_card(card)

    def check(self):
        pass
    
    def call(self,amount):
        self.cash -= amount
                    
    def aibet(self, surface, card, hand, commons, pot, tocall, position, stage):
        #Load the hole cards
        hand_str = []
        for cards in hand:
            hand_str.append(card.int_to_str(cards))
        hand_str.append('?')
        hand_str.append('?')
        
        #Load the communal cards
        if (commons != None):
            board_str = []
            for cards in commons:
                board_str.append(card.int_to_str(cards))
        else:
            board_str = None
            
        #Calculate equity
        from include.holdem_probs import holdem_calc
        result = holdem_calc.calculate(board_str, False, 10, None, hand_str,False)
        
        #Define pre-flop and post-flop ranges
        if (stage == 'preflop'):
            if (position == 'early'):
                threshold = 0.65
            elif (position == 'middle'):
                threshold = 0.58
            elif (position == 'late'):
                threshold = 0.5
          
            if (result[0][1] > threshold):
                return 15
            else:
                return -1
        else:
            EV_Pot = 0.1
            Eq = result[0][1]
            if (Eq > EV_Pot):
                Eq  = min(Eq,0.9)
                Bet = pot*min(0.3,(Eq-EV_Pot)/(1.-Eq))
                return max(15,Bet)
            else:
                return -1
        
    def bet(self, surface, screen):
        font = pygame.font.SysFont('Tahoma', 30, True, False)
        text = font.render('What do you want to do?: (k) check, (c) call, (r) rise,  (f) fold, (q) exit', True, (0, 0, 0))
        surface.blit(text, (100,1000))
        pygame.display.update()
        
        game_running = True
        key_name=''
        amount = ''
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_k or event.key == pygame.K_c or event.key == pygame.K_r or event.key == pygame.K_f or event.key == pygame.K_q):
                        key_name = pygame.key.name(event.key)
                        game_running = False
                        
        if (key_name == 'q'):
            pygame.quit()
        elif (key_name == 'k'):
            amount = 0
            
            rect = pygame.Rect(100, 1000, 1075, 500)
            pygame.draw.rect(surface, (255,255,255), rect)
            pygame.draw.rect(surface, (255,255,255), rect, 1)
            
            return amount
        elif (key_name == 'c'):
            amount = 0
            
            rect = pygame.Rect(100, 1000, 1075, 500)
            pygame.draw.rect(surface, (255,255,255), rect)
            pygame.draw.rect(surface, (255,255,255), rect, 1)
            
            return amount
        elif (key_name == 'f'):
            screen.player_folds(surface,0)
            amount = -1
            
            rect = pygame.Rect(100, 1000, 1075, 500)
            pygame.draw.rect(surface, (255,255,255), rect)
            pygame.draw.rect(surface, (255,255,255), rect, 1)
            
            return amount
        elif (key_name == 'r'):           
            font = pygame.font.SysFont('Tahoma', 30, True, False)
            text = font.render('Type your bet and press return:', True, (0, 0, 0))
            surface.blit(text, (bet_x,bet_y))
            
            game_running = True
            amount = ''
            pos_x = bet_x + 500
            pos_y = bet_y
            while game_running:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                            pygame.quit(); sys.exit()
                        if event.unicode:
                            try:
                                test = int(event.unicode)
                                amount += event.unicode
                                text = font.render(event.unicode, True, (0, 0, 0))
                                pos_x +=20
                                surface.blit(text, (pos_x,pos_y))
                            except:
                                pass
                        if event.key == pygame.K_RETURN:
                            game_running = False
                    pygame.display.update()
                    
            rect = pygame.Rect(bet_x, bet_y, 600, 50)
            pygame.draw.rect(surface, (255,255,255), rect)
            pygame.draw.rect(surface, (255,255,255), rect, 1)
            
            rect = pygame.Rect(100, 1000, 1075, 500)
            pygame.draw.rect(surface, (255,255,255), rect)
            pygame.draw.rect(surface, (255,255,255), rect, 1)
            
            return amount