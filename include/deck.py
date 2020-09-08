class newdeck:      
    def __init__(self):
        self.figures = {0:'2', 1:'3', 2:'4', 3:'5', 4:'6', 5:'7', 6:'8', 7:'9', 8:'10', 9:'jack', 10:'queen', 11:'king', 12:'ace'}
        self.suits   = {0:'clubs',1:'diamonds',2:'hearts',3:'spades'}  
        self.cards   = []
        self.hands   = {'Pair':[1,1,1,2], 'Three':[1,1,3], 'Double_Pair':[1,2,2], 'Full':[2,3], 'Four':[1,4], 'Five':[5]}
        self.flush   = {'Royal':[8,9,10,11,12], 'Straight':[0,1,2,3,4]}
        
        for i in range(len(self.suits)):
            for j in range(len(self.figures)):
                newcard = (j,i)
                self.cards.append(newcard)
                
    def get_card(self,card):
        return self.figures[card[0]]+'_of_'+self.suits[card[1]]+'.png'

    def test_flush(self, cards):
        figures = []
        suits   = []
        for tups in cards:
            figures.append(tups[0])
            suits.append(tups[1])
            
        elements, counts = np.unique(figures,return_counts=True)
        elements.sort()
        suits.sort()
                      
        if (suits[0] == suits[4]):
            if (list(elements) == self.flush['Royal']):
                print('You have a Royal Flush')
            elif (list(elements - elements[0]) == self.flush['Straight']):
                print('You have a Straight Flush')
            else:
                print('You have a Flush')        
        else:
            print('No Flush')
            
    def check_multiple(self, cards):
        figures = []
        suits   = []
        for tups in cards:
            figures.append(tups[0])
            suits.append(tups[1])
        elements, counts = np.unique(array,return_counts=True)
        
        if (len(elements) == 6):
            print('It must be a pair')
        if (len(elements) == 5 and 3 in counts):
            print('It must be three of a kind')
        if (len(elements) == 5 and 2 in counts):
            print('It must be a double pair')
        if (len(elements) == 4 and 3 in counts):
            print('It must be a full house')
        if (len(elements) <= 4 and (4 in counts or 5 in counts)):
            print('It must be four of a kind')
            
        return elements, counts