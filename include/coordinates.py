#----------------Players' cards coordinates on screen for a 1200x1200 display--------------------------
shiftx_hand = 40

#PLayer 1 hand
p1card1_x = 400 
p1card1_y = 800

p1card2_x = p1card1_x + shiftx_hand
p1card2_y = p1card1_y

#PLayer 2 hand
p2card1_x = 400 
p2card1_y = 300

p2card2_x = p2card1_x + shiftx_hand
p2card2_y = p2card1_y

#PLayer 3 hand
p3card1_x = 700 
p3card1_y = 300

p3card2_x = p3card1_x + shiftx_hand
p3card2_y = p3card1_y

#PLayer 4 hand
p4card1_x = 700 
p4card1_y = 800

p4card2_x = p4card1_x + shiftx_hand
p4card2_y = p4card1_y

#PLayer 5 hand
p5card1_x = 1000 
p5card1_y = 530

p5card2_x = p5card1_x + shiftx_hand
p5card2_y = p5card1_y

#PLayer 6 hand
p6card1_x = 100 
p6card1_y = 800

p6card2_x = p6card1_x + shiftx_hand
p6card2_y = p6card1_y

pcard1 = [(p1card1_x,p1card1_y), (p2card1_x,p2card1_y), (p3card1_x,p3card1_y), (p4card1_x,p4card1_y), (p5card1_x,p5card1_y), (p6card1_x,p6card1_y)]

pcard2 = [(p1card2_x,p1card2_y), (p2card2_x,p2card2_y), (p3card2_x,p3card2_y), (p4card2_x,p4card2_y), (p5card2_x,p5card2_y), (p6card2_x,p6card2_y)]            
            
#----------------Common cards coordinates on screen for a 1200x1200 display--------------------------
comm1_x = 395
comm1_y = 530

comm2_x = 480
comm2_y = 530

comm3_x = 565
comm3_y = 530

comm4_x = 650
comm4_y = 530

comm5_x = 735
comm5_y = 530

comm = [(comm1_x,comm1_y), (comm2_x,comm2_y), (comm3_x,comm3_y), (comm4_x,comm4_y), (comm5_x,comm5_y)]     

#---------------Buttons coordinates on screen for a 1200x1200 display--------------------------
b1_x = 410
b1_y = 920

b2_x = 375
b2_y = 250

b3_x = 685
b3_y = 250

b4_x = 685
b4_y = 920

buttons = ['Dealer', 'Small Blind', 'Big Blind', ' ']
buttons_coords = [(b1_x,b1_y), (b2_x,b2_y), (b3_x,b3_y), (b4_x,b4_y)]

#--------------Chips coordinates on screen for a 1200x1200 display-----------------------------
cp1_x = p1card1_x+10
cp1_y = p1card1_y-100

cp2_x = p2card1_x+10
cp2_y = p2card1_y+150

cp3_x = p3card1_x+10
cp3_y = p3card1_y+150

cp4_x = p4card1_x+10
cp4_y = p4card1_y-100

cp_displ = 15

chips_coords = [(cp1_x,cp1_y), (cp2_x,cp2_y), (cp3_x,cp3_y), (cp4_x,cp4_y)]
chips = ["Images/casino_chips/chip_5_w85h85.png", "Images/casino_chips/chip_10_w85h85.png", "Images/casino_chips/chip_50_w85h85.png", "Images/casino_chips/chip_100_w85h85.png"]

#------------------Pot coordinates on screen for a 1200x1200 display-----------------------------
pot_x = 890
pot_y = 100

#------------------Bet coordinates on screen for a 1200x1200 display-----------------------------
bet_x = 100
bet_y = 1100