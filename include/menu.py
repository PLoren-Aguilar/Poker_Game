#------------------------------------------------------------------
# The "newmenu" class takes care of all the graphic aspects of
# the game. From loading the table image, the cards, buttons, etc
#
# Local dependencies: coordinates, treys/Card class
#
# Author: Pablo Loren-Aguilar
#------------------------------------------------------------------
from include.treys.treys import Card
import pygame
from include.coordinates import *

pygame.init()

class newmenu:  
    def __init__(self):
        surface = pygame.display.set_mode((1200, 1200)) 
        surface.fill((255,255,255))
        pygame.display.set_caption("Texas Hold'em")
        
        font = pygame.font.SysFont('Tahoma', 100, True, False)
        text = font.render("Texas Hold'em", True, (0, 0, 0))
        surface.blit(text, (200,100))
        
        font = pygame.font.SysFont('Tahoma', 40, True, False)
        text = font.render("By Pablo Loren-Aguilar", True, (0, 0, 0))
        surface.blit(text, (325,225))
        
        font = pygame.font.SysFont('Tahoma', 30, True, False)
        text = font.render("Press s to start the game or x to quit", True, (0, 0, 0))
        surface.blit(text, (325,1000))
        
        image = pygame.image.load("Images/menu.jpg")
        surface.blit(image, (250,400))
        
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
                
    def create_table(self,surface):
        #Draw the table
        table = pygame.image.load("Images/table.jpg")
        table = pygame.transform.scale(table, (1400, 1000))
        surface.blit(table, (-100,100))
        pygame.display.flip()
        
        #empty_rect = pygame.Rect(cp1_x, cp1_y, 85, 110)
        #pygame.draw.rect(surface, (0,0,0), empty_rect, 1)
        #empty_rect = pygame.Rect(cp2_x, cp2_y, 310, 85)
        #pygame.draw.rect(surface, (0,0,0), empty_rect, 1)
        #empty_rect = pygame.Rect(cp3_x, cp3_y, 85, 110)
        #pygame.draw.rect(surface, (0,0,0), empty_rect, 1)
        #empty_rect = pygame.Rect(cp4_x, cp4_y, 85, 110)
        #pygame.draw.rect(surface, (0,0,0), empty_rect, 1)
        #empty_rect = pygame.Rect(cp5_x, cp5_y, 85, 110)
        #pygame.draw.rect(surface, (0,0,0), empty_rect, 1)
        #empty_rect = pygame.Rect(cp6_x, cp6_y, 85, 110)
        #pygame.draw.rect(surface, (0,0,0), empty_rect, 1)
        
    def player_cards(self,surface,hand,player):
        file1 = "Images/cards/" + Card.int_to_str(hand[0]) + ".png"
        file2 = "Images/cards/" + Card.int_to_str(hand[1]) + ".png"  
        card1 = pygame.image.load(file1)
        surface.blit(card1, pcard1[player])
        card2 = pygame.image.load(file2)
        surface.blit(card2, pcard2[player])
        
    def player_folds(self,surface,player):
        file1 = "Images/cards/cardback.png"
        file2 = "Images/cards/cardback.png"  
        card1 = pygame.image.load(file1)
        surface.blit(card1, pcard1[player])
        card2 = pygame.image.load(file2)
        surface.blit(card2, pcard2[player])
        
    def put_all_cards(self,surface,nplayers,players):    
        if (nplayers < 2 or nplayers > 6):
            print('Wrong number of players!')
            pygame.quit(); sys.exit()
        
        for indx,player in enumerate(players):
            if (player.cash > 0):
                card = pygame.image.load("Images/cards/cardback1.png")
                surface.blit(card, pcard1[indx])
                surface.blit(card, pcard2[indx])
                                    
        #Communal cards
        common = pygame.image.load("Images/cards/cardback1.png")        
        for i in range(5):
            surface.blit(common, comm[i])       
                   
    def put_buttons(self,surface,players_order,turn):
        #empty_rect = pygame.Rect(b1_x, b1_y-10, 170, 50)
        #pygame.draw.rect(surface, (255,255,255), empty_rect)
        #empty_rect = pygame.Rect(b2_x, b2_y-10, 170, 50)
        #pygame.draw.rect(surface, (255,255,255), empty_rect)
        #empty_rect = pygame.Rect(b3_x, b3_y-10, 170, 50)
        #pygame.draw.rect(surface, (255,255,255), empty_rect)
        
        font = pygame.font.SysFont('Tahoma', 20, True, False)
        if (len(players_order) >= 3):
            nplay = 3
            for i in range(nplay):
                button = "Images/" + buttons[i] + ".jpg"
                image = pygame.image.load(button)
                image = pygame.transform.scale(image, (50, 50))
                surface.blit(image, buttons_coords[players_order[i]])
        elif (len(players_order) == 2):
            #This is a quite special case. The dealer is also the small blind
            text = font.render(buttons[0] +'/'+ buttons[1], True, (0, 0, 0))
            surface.blit(text, buttons_coords[players_order[0]])
            
            text = font.render(buttons[2], True, (0, 0, 0))
            surface.blit(text, buttons_coords[players_order[1]])
            
    def show_common(self,surface,cards,n):
        if (n == 'preflop'):
            pass
        elif (n == 'flop'):
            card1 = "Images/cards/" + Card.int_to_str(cards[0]) + ".png"
            card2 = "Images/cards/" + Card.int_to_str(cards[1]) + ".png"           
            card3 = "Images/cards/" + Card.int_to_str(cards[2]) + ".png"
            common1 = pygame.image.load(card1)
            surface.blit(common1, (comm1_x,comm1_y))
            common2 = pygame.image.load(card2)
            surface.blit(common2, (comm2_x,comm2_y))
            common3 = pygame.image.load(card3)
            surface.blit(common3, (comm3_x,comm3_y))
        elif (n == 'turn'):
            card4 = "Images/cards/" + Card.int_to_str(cards[3]) + ".png"
            common4 = pygame.image.load(card4)
            surface.blit(common4, (comm4_x,comm4_y))
        elif (n == 'river'):
            card5 = "Images/cards/" + Card.int_to_str(cards[4]) + ".png"
            common5 = pygame.image.load(card5)
            surface.blit(common5, (comm5_x,comm5_y))
        else:
            print('Unknown option')
            quit()            
        
    def show_blinds(self,surface):
        font = pygame.font.SysFont('Tahoma', 30, True, False)
        text = font.render('Current blinds: 10/50', True, (0, 0, 0))
        surface.blit(text, (200,100))
              
    def put_blinds(self,surface,players_order):      
        if (len(players_order) >=3):
            for i in range(1,3):
                chips1 = pygame.image.load(chips[i])
                chips1 = pygame.transform.scale(chips1,(40,40))
                surface.blit(chips1, chips_coords[players_order[i]])
                
        if (len(players_order) == 2):
            #This is a special case. Here the dealer is the small blind and the other player the big blind
            chips1 = pygame.image.load(chips[1])
            chips1 = pygame.transform.scale(chips1,(40,40))
            surface.blit(chips1, chips_coords[players_order[0]])
            
            chips1 = pygame.image.load(chips[2])
            chips1 = pygame.transform.scale(chips1,(40,40))
            surface.blit(chips1, chips_coords[players_order[1]])
            
    def update_pot(self,surface,pot):
        rect = pygame.Rect(pot_x, pot_y-5, 170, 50)
        pygame.draw.rect(surface, (255,255,255), rect)
        pygame.draw.rect(surface, (255,255,255), rect, 1)
        
        font = pygame.font.SysFont('Tahoma', 30, True, False)
        text = font.render('Pot = ' + str(pot), True, (0, 0, 0))
        surface.blit(text, (800,100))
        
    def put_chips(self,surface,player,id,blind,amount,bet):
        if (bet == 'preflop'):
            if (blind == True):
                delta = cp_displ
            else:
                delta = 0
        else:
            delta = 0
           
        #Calculate the number of chips we need (and put them in the table)
        n100 = int(amount/100)
        if (n100 >= 0):
            if (id == 1 or id == 4):
                x = chips_coords[player][0]
                y = chips_coords[player][1] + delta
            else:
                x = chips_coords[player][0] + delta
                y = chips_coords[player][1]
                
            for i in range(n100):
                nchips = pygame.image.load(chips[3])
                nchips = pygame.transform.scale(nchips,(40,40))
                surface.blit(nchips, (x,y))
                if (id == 1 or id == 4):
                    y = y + cp_displ
                else:
                    x = x + cp_displ
                    
        amount = amount % 100
        n50 = int(amount/50)
        if (n50 >= 0):
            for i in range(n50):
                nchips = pygame.image.load(chips[2])
                nchips = pygame.transform.scale(nchips,(40,40))
                surface.blit(nchips, (x,y))
                if (id == 1 or id == 4):
                    y = y + cp_displ
                else:
                    x = x + cp_displ
                    
        amount = amount % 50
        n10 = int(amount/10)
        if (n10 >= 0):
            for i in range(n10):
                nchips = pygame.image.load(chips[1])
                nchips = pygame.transform.scale(nchips,(40,40))
                surface.blit(nchips, (x,y))
                if (id == 1 or id == 4):
                    y = y + cp_displ
                else:
                    x = x + cp_displ
                            
        amount = amount % 10
        n5 = int(amount/5)
        if (n5 >= 0):
            for i in range(n5):
                nchips = pygame.image.load(chips[0])
                nchips = pygame.transform.scale(nchips,(40,40))
                surface.blit(nchips, (x,y))
                if (id == 1 or id == 4):
                    y = y + cp_displ
                else:
                    x = x + cp_displ
            
    def remove_chips(self,surface):
        rect = pygame.Rect(cp1_x, cp1_y-5, 170, 50)
        pygame.draw.rect(surface, (0,153,105), rect)
        pygame.draw.rect(surface, (0,0,0), rect, 1)
        
        rect = pygame.Rect(cp2_x-5, cp2_y, 50, 170)
        pygame.draw.rect(surface, (0,153,105), rect)
        pygame.draw.rect(surface, (0,0,0), rect, 1)
        
        rect = pygame.Rect(cp3_x, cp3_y-5, 170, 50)
        pygame.draw.rect(surface, (0,153,105), rect)
        pygame.draw.rect(surface, (0,0,0), rect, 1)
        
        rect = pygame.Rect(cp4_x, cp4_y-5, 170, 50)
        pygame.draw.rect(surface, (0,153,105), rect)
        pygame.draw.rect(surface, (0,0,0), rect, 1)
        
        rect = pygame.Rect(cp5_x-5, cp5_y, 50, 170)
        pygame.draw.rect(surface, (0,153,105), rect)
        pygame.draw.rect(surface, (0,0,0), rect, 1)
        
        rect = pygame.Rect(cp6_x, cp6_y-5, 170, 50)
        pygame.draw.rect(surface, (0,153,105), rect)
        pygame.draw.rect(surface, (0,0,0), rect, 1)        