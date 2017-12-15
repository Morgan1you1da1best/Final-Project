#Morgan Baughman
#12/14/17
#Yahtzee.py

from random import randint
from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)

blackOutline = LineStyle(1,black) #pixels, color
whiteRectangle = RectangleAsset(100,100,blackOutline,white) #Width, height, outline, fill.
blackCircle = CircleAsset(10,blackOutline,black) #Radius, outline, fill.
redCircle = CircleAsset(50,blackOutline,red)
text = TextAsset('Yahtzee' ,fill=red, style='bold 40pt Times')

data = {}

####################### Die #1 ############################## (dice(dice#)(dot#))
def diceOneOne():
    Sprite(blackCircle,(150,150))

def diceOneTwo():
    Sprite(blackCircle,(165,130))
    Sprite(blackCircle,(135,170))

def diceOneThree():
    Sprite(blackCircle,(165,130))
    Sprite(blackCircle,(150,150))
    Sprite(blackCircle,(135,170))

def diceOneFour():
    Sprite(blackCircle,(130,130))
    Sprite(blackCircle,(130,170))
    Sprite(blackCircle,(170,130))
    Sprite(blackCircle,(170,170))

def diceOneFive():
    Sprite(blackCircle,(130,130))
    Sprite(blackCircle,(130,170))
    Sprite(blackCircle,(150,150))
    Sprite(blackCircle,(170,130))
    Sprite(blackCircle,(170,170))

def diceOneSix():
    Sprite(blackCircle,(130,125))
    Sprite(blackCircle,(130,150))
    Sprite(blackCircle,(130,175))
    Sprite(blackCircle,(170,125))
    Sprite(blackCircle,(170,150))
    Sprite(blackCircle,(170,175))
    
####################### Die #2 ##############################
def diceTwoOne():
    Sprite(blackCircle,(250,150))
    
def diceTwoTwo():
    Sprite(blackCircle,(265,130))
    Sprite(blackCircle,(235,170))
    
def diceTwoThree():
    Sprite(blackCircle,(265,130))
    Sprite(blackCircle,(250,150))
    Sprite(blackCircle,(235,170))
    
def diceTwoFour():
    Sprite(blackCircle,(230,130))
    Sprite(blackCircle,(230,170))
    Sprite(blackCircle,(270,130))
    Sprite(blackCircle,(270,170))

def diceTwoFive():
    Sprite(blackCircle,(230,130))
    Sprite(blackCircle,(230,170))
    Sprite(blackCircle,(250,150))
    Sprite(blackCircle,(270,130))
    Sprite(blackCircle,(270,170))

def diceTwoSix():
    Sprite(blackCircle,(230,125))
    Sprite(blackCircle,(230,150))
    Sprite(blackCircle,(230,175))
    Sprite(blackCircle,(270,125))
    Sprite(blackCircle,(270,150))
    Sprite(blackCircle,(270,175))

####################### Die #3 ##############################
def diceThreeOne():
    Sprite(blackCircle,(350,150))
    
def diceThreeTwo():
    Sprite(blackCircle,(365,130))
    Sprite(blackCircle,(335,170))
    
def diceThreeThree():
    Sprite(blackCircle,(365,130))
    Sprite(blackCircle,(350,150))
    Sprite(blackCircle,(335,170))
    
def diceThreeFour():
    Sprite(blackCircle,(330,130))
    Sprite(blackCircle,(330,170))
    Sprite(blackCircle,(370,130))
    Sprite(blackCircle,(370,170))

def diceThreeFive():
    Sprite(blackCircle,(330,130))
    Sprite(blackCircle,(330,170))
    Sprite(blackCircle,(350,150))
    Sprite(blackCircle,(370,130))
    Sprite(blackCircle,(370,170))

def diceThreeSix():
    Sprite(blackCircle,(330,125))
    Sprite(blackCircle,(330,150))
    Sprite(blackCircle,(330,175))
    Sprite(blackCircle,(370,125))
    Sprite(blackCircle,(370,150))
    Sprite(blackCircle,(370,175))

####################### Die #4 ##############################
def diceFourOne():
    Sprite(blackCircle,(450,150))
    
def diceFourTwo():
    Sprite(blackCircle,(465,130))
    Sprite(blackCircle,(435,170))
    
def diceFourThree():
    Sprite(blackCircle,(465,130))
    Sprite(blackCircle,(450,150))
    Sprite(blackCircle,(435,170))
    
def diceFourFour():
    Sprite(blackCircle,(430,130))
    Sprite(blackCircle,(430,170))
    Sprite(blackCircle,(470,130))
    Sprite(blackCircle,(470,170))

def diceFourFive():
    Sprite(blackCircle,(430,130))
    Sprite(blackCircle,(430,170))
    Sprite(blackCircle,(450,150))
    Sprite(blackCircle,(470,130))
    Sprite(blackCircle,(470,170))

def diceFourSix():
    Sprite(blackCircle,(430,125))
    Sprite(blackCircle,(430,150))
    Sprite(blackCircle,(430,175))
    Sprite(blackCircle,(470,125))
    Sprite(blackCircle,(470,150))
    Sprite(blackCircle,(470,175))

####################### Die #5 ##############################

def diceFiveOne():
    Sprite(blackCircle,(550,150))
    
def diceFiveTwo():
    Sprite(blackCircle,(565,130))
    Sprite(blackCircle,(535,170))
    
def diceFiveThree():
    Sprite(blackCircle,(565,130))
    Sprite(blackCircle,(550,150))
    Sprite(blackCircle,(535,170))
    
def diceFiveFour():
    Sprite(blackCircle,(530,130))
    Sprite(blackCircle,(530,170))
    Sprite(blackCircle,(570,130))
    Sprite(blackCircle,(570,170))

def diceFiveFive():
    Sprite(blackCircle,(530,130))
    Sprite(blackCircle,(530,170))
    Sprite(blackCircle,(550,150))
    Sprite(blackCircle,(570,130))
    Sprite(blackCircle,(570,170))

def diceFiveSix():
    Sprite(blackCircle,(530,125))
    Sprite(blackCircle,(530,150))
    Sprite(blackCircle,(530,175))
    Sprite(blackCircle,(570,125))
    Sprite(blackCircle,(570,150))
    Sprite(blackCircle,(570,175))


#########################Dice Roll#################################

def diceRoll():
    num = randint(1,6)
    if num == 1:
        diceOneOne()
        data['diceOneOne'] = True
    if num == 2:
        diceOneTwo()
        data['diceOneTwo'] = True
    if num == 3:
        diceOneThree()
        data['diceOneThree'] = True
    if num == 4:
        diceOneFour()
        data['diceOneFour'] = True
    if num == 5:
        diceOneFive()
        data['diceOneFive'] = True
    if num == 6:
        diceOneSix()
        data['diceOneSix'] = True

data['diceOneOne'] = False
data['diceOneTwo'] = False
data['diceOneThree'] = False
data['diceOneFour'] = False
data['diceOneFive'] = False
data['diceOneSix'] = False


def diceRoll2():
    num = randint(1,6)
    if num == 1:
        diceTwoOne()
        data['diceTwoOne'] = True
    if num == 2:
        diceTwoTwo()
        data['diceTwoTwo'] = True
    if num == 3:
        diceTwoThree()
        data['diceTwoThree'] = True
    if num == 4:
        diceTwoFour()
        data['diceTwoFour'] = True
    if num == 5:
        diceTwoFive()
        data['diceTwoFive'] = True
    if num == 6:
        diceTwoSix()
        data['diceTwoSix'] = True
        
data['diceTwoOne'] = False
data['diceTwoTwo'] = False
data['diceTwoThree'] = False
data['diceTwoFour'] = False
data['diceTwoFive'] = False
data['diceTwoSix'] = False

def diceRoll3():
    num = randint(1,6)
    if num == 1:
        diceThreeOne()
        data ['diceThreeOne'] = True
    if num == 2:
        diceThreeTwo()
        data ['diceThreeTwo'] = True
    if num == 3:
        diceThreeThree()
        data ['diceThreeThree'] = True
    if num == 4:
        diceThreeFour()
        data ['diceThreeFour'] = True
    if num == 5:
        diceThreeFive()
        data ['diceThreeFive'] = True
    if num == 6:
        diceThreeSix()
        data ['diceThreeSix'] = True
        
data['diceThreeOne'] = False
data['diceThreeTwo'] = False
data['diceThreeThree'] = False
data['diceThreeFour'] = False
data['diceThreeFive'] = False
data['diceThreeSix'] = False
        
def diceRoll4():
    num = randint(1,6)
    if num == 1:
        diceFourOne()
        data['diceFourOne'] = True
    if num == 2:
        diceFourTwo()
        data['diceFourTwo'] = True
    if num == 3:
        diceFourThree()
        data['diceFourThree'] = True
    if num == 4:
        diceFourFour()
        data['diceFourFour'] = True
    if num == 5:
        diceFourFive()
        data['diceFourFive'] = True
    if num == 6:
        diceFourSix()
        data['diceFourSix'] = True

data['diceFourOne'] = False
data['diceFourTwo'] = False
data['diceFourThree'] = False
data['diceFourFour'] = False
data['diceFourFive'] = False
data['diceFourSix'] = False



def diceRoll5():
    num = randint(1,6)
    if num == 1:
        diceFiveOne()
        data['diceFiveOne'] = True
    if num == 2:
        diceFiveTwo()
        data['diceFiveTwo'] = True
    if num == 3:
        diceFiveThree()
        data['diceFiveThree'] = True
    if num == 4:
        diceFiveFour()
        data['diceFiveFour'] = True
    if num == 5:
        diceFiveFive()
        data['diceFiveFive'] = True
    if num == 6:
        diceFiveSix()
        data['diceFiveSix'] = True
        
data['diceFiveOne'] = False
data['diceFiveTwo'] = False
data['diceFiveThree'] = False
data['diceFiveFour'] = False
data['diceFiveFive'] = False
data['diceFiveSix'] = False

####################### Roll Dice ###########################

data['diceRoll'] = True
data['diceRoll2'] = True
data['diceRoll3'] = True
data['diceRoll4'] = True
data['diceRoll5'] = True

def mouseClick(event):
    if event.x <= 750 and event.x >=650 and event.y <= 200 and event.y >= 100:
        if data['diceRoll'] == True:
            diceRoll()
        if data['diceRoll2'] == True:
            diceRoll2()
        if data['diceRoll3'] == True:
            diceRoll3()
        if data['diceRoll4'] == True:
            diceRoll4()
        if data['diceRoll5'] == True:
            diceRoll5()
    
#################################Pick Dice #1#############################
    
    if event.x >= 100 and event.x <= 200 and event.y >= 100 and event.y <= 200 and data['diceOneOne'] == True:
        print('1')
        data['diceRoll'] = False
    if event.x >= 100 and event.x <= 200 and event.y >= 100 and event.y <= 200 and data['diceOneTwo'] == True:
        print('2')
        data['diceRoll'] = False
    if event.x >= 100 and event.x <= 200 and event.y >= 100 and event.y <= 200 and data['diceOneThree'] == True:
        print('3')
        data['diceRoll'] = False
    if event.x >= 100 and event.x <= 200 and event.y >= 100 and event.y <= 200 and data['diceOneFour'] == True:
        print('4')
        data['diceRoll'] = False
    if event.x >= 100 and event.x <= 200 and event.y >= 100 and event.y <= 200 and data['diceOneFive'] == True:
        print('5')
        data['diceRoll'] = False
    if event.x >= 100 and event.x <= 200 and event.y >= 100 and event.y <= 200 and data['diceOneSix'] == True:
        print('6')
        data['diceRoll'] = False

#################################Pick Dice #2#############################

    if event.x >= 200 and event.x <= 300 and event.y >= 100 and event.y <= 200 and data['diceTwoOne'] == True:
        print('1')
        data['diceRoll2'] = False
    if event.x >= 200 and event.x <= 300 and event.y >= 100 and event.y <= 200 and data['diceTwoTwo'] == True:
        print('2')
        data['diceRoll2'] = False
    if event.x >= 200 and event.x <= 300 and event.y >= 100 and event.y <= 200 and data['diceTwoThree'] == True:
        print('3')
        data['diceRoll2'] = False
    if event.x >= 200 and event.x <= 300 and event.y >= 100 and event.y <= 200 and data['diceTwoFour'] == True:
        print('4')
        data['diceRoll2'] = False
    if event.x >= 200 and event.x <= 300 and event.y >= 100 and event.y <= 200 and data['diceTwoFive'] == True:
        print('5')
        data['diceRoll2'] = False
    if event.x >= 200 and event.x <= 300 and event.y >= 100 and event.y <= 200 and data['diceTwoSix'] == True:
        print('6')
        data['diceRoll2'] = False
 
#################################Pick Dice #3#############################

    if event.x >= 300 and event.x <= 300 and event.y >= 100 and event.y <= 200 and data['diceThreeOne'] == True:
        print('1')
        data['diceRoll3'] = False
    if event.x >= 300 and event.x <= 400 and event.y >= 100 and event.y <= 200 and data['diceThreeTwo'] == True:
        print('2')
        data['diceRoll3'] = False
    if event.x >= 300 and event.x <= 400 and event.y >= 100 and event.y <= 200 and data['diceThreeThree'] == True:
        print('3')
        data['diceRoll3'] = False
    if event.x >= 300 and event.x <= 400 and event.y >= 100 and event.y <= 200 and data['diceThreeFour'] == True:
        print('4')
        data['diceRoll3'] = False
    if event.x >= 300 and event.x <= 400 and event.y >= 100 and event.y <= 200 and data['diceThreeFive'] == True:
        print('5')
        data['diceRoll3'] = False
    if event.x >= 300 and event.x <= 400 and event.y >= 100 and event.y <= 200 and data['diceThreeSix'] == True:
        print('6')
        data['diceRoll3'] = False


#################################Pick Dice #4#############################

    if event.x >= 400 and event.x <= 500 and event.y >= 100 and event.y <= 200 and data['diceFourOne'] == True:
        print('1')
        data['diceRoll4'] = False
    if event.x >= 400 and event.x <= 500 and event.y >= 100 and event.y <= 200 and data['diceFourTwo'] == True:
        print('2')
        data['diceRoll4'] = False
    if event.x >= 400 and event.x <= 500 and event.y >= 100 and event.y <= 200 and data['diceFourThree'] == True:
        print('3')
        data['diceRoll4'] = False
    if event.x >= 400 and event.x <= 500 and event.y >= 100 and event.y <= 200 and data['diceFourFour'] == True:
        print('4')
        data['diceRoll4'] = False
    if event.x >= 400 and event.x <= 500 and event.y >= 100 and event.y <= 200 and data['diceFourFive'] == True:
        print('5')
        data['diceRoll4'] = False
    if event.x >= 400 and event.x <= 500 and event.y >= 100 and event.y <= 200 and data['diceFourSix'] == True:
        print('6')
        data['diceRoll4'] = False

#################################Pick Dice #5#############################

    if event.x >= 500 and event.x <= 600 and event.y >= 100 and event.y <= 200 and data['diceFiveOne'] == True:
        print('1')
        data['diceRoll5'] = False
    if event.x >= 500 and event.x <= 600 and event.y >= 100 and event.y <= 200 and data['diceFiveTwo'] == True:
        print('2')
        data['diceRoll5'] = False
    if event.x >= 500 and event.x <= 600 and event.y >= 100 and event.y <= 200 and data['diceFiveThree'] == True:
        print('3')
        data['diceRoll5'] = False
    if event.x >= 500 and event.x <= 600 and event.y >= 100 and event.y <= 200 and data['diceFiveFour'] == True:
        print('4')
        data['diceRoll5'] = False
    if event.x >= 500 and event.x <= 600 and event.y >= 100 and event.y <= 200 and data['diceFiveFive'] == True:
        print('5')
        data['diceRoll5'] = False
    if event.x >= 500 and event.x <= 600 and event.y >= 100 and event.y <= 200 and data['diceFiveSix'] == True:
        print('6')
        data['diceRoll5'] = False


Sprite(whiteRectangle,(100,100))
Sprite(whiteRectangle,(200,100))
Sprite(whiteRectangle,(300,100))
Sprite(whiteRectangle,(400,100))
Sprite(whiteRectangle,(500,100))
Sprite(redCircle,(700,150))
Sprite(text, (250,0))
App().listenMouseEvent("click", mouseClick)
App().run()