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
        
    def preflop(hand,position):
        if (hand[0][0] == 'A' and hand[1][0] == 'A'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'R'
            elif (position == 'M'):
                decision = 'R'
            elif (position == 'E'):
                decision = 'R'             
        elif (hand[0][0] == 'A' and hand[1][0] == 'K'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'R'
            elif (position == 'M'):
                decision = 'R'
            elif (position == 'E'):
                decision = 'R'      
        elif (hand[0][0] == 'A' and hand[1][0] == 'Q'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'R'
            elif (position == 'M'):
                decision = 'R'
            elif (position == 'E'):
                decision = 'R'        
        elif (hand[0][0] == 'A' and hand[1][0] == 'J'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            elif (position == 'M'):
                decision = 'P'
            elif (position == 'E'):
                decision = 'F'
        elif (hand[0][0] == 'A' and hand[1][0] == '10'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'M'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'E'):
                decision = 'F'      
        elif (hand[0][0] == 'A' and (hand[1][0] >= '2' and hand[1][0] <= 9)):
            if (position == 'COB'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            else:
                decision = 'F'
        elif (hand[0][0] == 'K' and hand[1][0] == 'K'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'R'
            elif (position == 'M'):
                decision = 'R'
            elif (position == 'E'):
                decision = 'R'             
        elif (hand[0][0] == 'K' and hand[1][0] == 'Q'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'P'
            elif (position == 'M'):
                decision = 'P'
            elif (position == 'E'):
                decision = 'F'             
        elif (hand[0][0] == 'K' and hand[1][0] == 'J'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'M'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'E'):              
                decision = 'F'
        elif (hand[0][0] == 'K' and (hand[1][0] >= '9' and hand[1][0] <= 10)):
            if (position == 'COB'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            else:
                decision = 'F'
        elif (hand[0][0] == 'Q' and hand[1][0] == 'Q'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'R'
            elif (position == 'M'):
                decision = 'R'
            elif (position == 'E'):
                decision = 'R'
        elif (hand[0][0] == 'Q' and hand[1][0] == 'J'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'M'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'E'):
                decision = 'F'
        elif (hand[0][0] == 'Q' and (hand[1][0] >= '9' and hand[1][0] <= 10)):
            if (position == 'COB'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            else:
                decision = 'F'
        elif (hand[0][0] == 'J' and hand[1][0] == 'J'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'R'
            elif (position == 'M'):
                decision = 'R'
            elif (position == 'E'):
                decision = 'P'
        elif (hand[0][0] == 'J' and hand[1][0] == '10'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'M'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'E'):
                decision = 'F'
        elif (hand[0][0] == '10' and hand[1][0] == '10'):
            if (position == 'COB'):
                decision = 'RR'
            elif (position == 'H'):
                decision = 'R'
            elif (position == 'M'):
                decision = 'P'
            elif (position == 'E'):
                decision = 'P'                        
        elif (hand[0][0] == '10' and hand[1][0] == '9'):
            if (position == 'COB'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'H'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'M'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            elif (position == 'E'):              
                decision = 'F' 
        elif (hand[0][0] == '9' and hand[1][0] == '9'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            elif (position == 'M'):
                decision = 'P'
            elif (position == 'E'):
                decision = 'F'
        elif (hand[0][0] == '8' and hand[1][0] == '8'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            elif (position == 'M'):
                decision = 'P'
            elif (position == 'E'):
                decision = 'F'      
        elif (hand[0][0] == '7' and hand[1][0] == '7'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            elif (position == 'M'):
                decision = 'P'
            elif (position == 'E'):
                decision = 'F'       
        elif (hand[0][0] == '6' and hand[1][0] == '6'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            else:
                decision = 'F'
        elif (hand[0][0] == '5' and hand[1][0] == '5'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            else:
                decision = 'F'
        elif (hand[0][0] == '4' and hand[1][0] == '4'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            else:
                decision = 'F'
        elif (hand[0][0] == '3' and hand[1][0] == '3'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            else:
                decision = 'F'
        elif (hand[0][0] == '2' and hand[1][0] == '2'):
            if (position == 'COB'):
                decision = 'P'
            elif (position == 'H'):
                decision = 'P'
            else:
                decision = 'F'
        else:
            if (position == 'COB'):
                if (hand[0][1] == hand[1][1]):
                    decision = 'P'
                else:
                    decision = 'F'
            else:
                decision = 'F'            
        if (decision != 'RR' and decision != 'R' & decision != 'P' and decision != 'F'):
              print('Wrong AI decision!')
               
        return decision
              
    def aibet(self, surface, card, id, hand, commons, pot):
        hand_str = []
        for cards in hand:
            hand_str.append(card.int_to_str(cards))
        hand_str.append('?')
        hand_str.append('?')
         
        board_str = None
        if (commons != None):
            board_str = []
            for cards in commons:
                board_str.append(card.int_to_str(cards))      
        probability = holdem_calc.calculate(board_str, False, 10, None, hand_str, False)          
        
        if (probability[0][1] > 0.5):
            return 15
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
            return amount
        elif (key_name == 'c'):
            amount = 0
            return amount
        elif (key_name == 'f'):
            screen.player_folds(surface,0)
            amount = 0
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
            
            return amount