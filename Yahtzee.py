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
cardRectangle = RectangleAsset(200,300,blackOutline,white)
blackCircle = CircleAsset(10,blackOutline,black) #Radius, outline, fill.
redCircle = CircleAsset(50,blackOutline,red)
text = TextAsset('Yahtzee' ,fill=red, style='bold 40pt Times')
titleCard = TextAsset('Player 1' ,fill=black, style='10pt Times')
titleCard2 = TextAsset('Player 2' ,fill=black, style='10pt Times')
textRoll = TextAsset('Roll' ,fill=black, style='20pt Verdana')


####################### Die Roll ############################## (dice(dice#)(dot#))
def numOne(xcord1):
        Sprite(blackCircle,(xcord1,150))
        print('bye')

def numTwo(xcord1,xcord2):
        Sprite(blackCircle,(xcord1,165))
        Sprite(blackCircle,(xcord2,135))

def numThree(xcord1,xcord2,xcord3):
        Sprite(blackCircle,(xcord1,165))
        Sprite(blackCircle,(xcord2,150))
        Sprite(blackCircle,(xcord3,135))

def numFour(xcord1,xcord2,xcord3,xcord4):
        Sprite(blackCircle,(xcord1,130))
        Sprite(blackCircle,(xcord2,130))
        Sprite(blackCircle,(xcord3,170))
        Sprite(blackCircle,(xcord4,170))

def numFive(xcord1,xcord2,xcord3,xcord4,xcord5):
        Sprite(blackCircle,(xcord1,130))
        Sprite(blackCircle,(xcord2,130))
        Sprite(blackCircle,(xcord3,150))
        Sprite(blackCircle,(xcord4,170))
        Sprite(blackCircle,(xcord5,170))

def numSix(xcord1,xcord2,xcord3,xcord4,xcord5,xcord6):
        Sprite(blackCircle,(xcord1,125))
        Sprite(blackCircle,(xcord2,150))
        Sprite(blackCircle,(xcord3,175))
        Sprite(blackCircle,(xcord4,125))
        Sprite(blackCircle,(xcord5,150))
        Sprite(blackCircle,(xcord6,175))

#########################Dice Roll###############################

def diceRoll():
    num = randint(1,6)
    if num == 1:
        numOne(150)
        data['diceOneOne'] = True
    if num == 2:
        numTwo(165,135)
        data['diceOneTwo'] = True
    if num == 3:
        numThree(170,150,130)
        data['diceOneThree'] = True
    if num == 4:
        numFour(130,170,130,170)
        data['diceOneFour'] = True
    if num == 5:
        numFive(130,170,150,130,170)
        data['diceOneFive'] = True
    if num == 6:
        numSix(130,130,130,170,170,170)
        data['diceOneSix'] = True

def diceRoll2():
    num = randint(1,6)
    if num == 1:
        numOne(250)
        data['diceTwoOne'] = True
    if num == 2:
        numTwo(265,235)
        data['diceTwoTwo'] = True
    if num == 3:
        numThree(270,250,230)
        data['diceTwoThree'] = True
    if num == 4:
        numFour(230,270,230,270)
        data['diceTwoFour'] = True
    if num == 5:
        numFive(230,270,250,230,270)
        data['diceTwoFive'] = True
    if num == 6:
        numSix(230,230,230,270,270,270)
        data['diceTwoSix'] = True
        
def diceRoll3():
    num = randint(1,6)
    if num == 1:
        numOne(350)
        data ['diceThreeOne'] = True
    if num == 2:
        numTwo(365,335)
        data ['diceThreeTwo'] = True
    if num == 3:
        numThree(370,350,330)
        data ['diceThreeThree'] = True
    if num == 4:
        numFour(330,370,330,370)
        data ['diceThreeFour'] = True
    if num == 5:
        numFive(330,370,350,330,370)
        data ['diceThreeFive'] = True
    if num == 6:
        numSix(330,330,330,370,370,370)
        data ['diceThreeSix'] = True

def diceRoll4():
    num = randint(1,6)
    if num == 1:
        numOne(450)
        data['diceFourOne'] = True
    if num == 2:
        numTwo(465,435)
        data['diceFourTwo'] = True
    if num == 3:
        numThree(470,450,430)
        data['diceFourThree'] = True
    if num == 4:
        numFour(430,470,470,430)
        data['diceFourFour'] = True
    if num == 5:
        numFive(430,470,450,430,470)
        data['diceFourFive'] = True
    if num == 6:
        numSix(430,430,430,470,470,470)
        data['diceFourSix'] = True

def diceRoll5():
    num = randint(1,6)
    if num == 1:
        numOne(550)
        data['diceFiveOne'] = True
    if num == 2:
        numTwo(565,535)
        data['diceFiveTwo'] = True
    if num == 3:
        numThree(565,550,535)
        data['diceFiveThree'] = True
    if num == 4:
        numFour(530,570,530,570)
        data['diceFiveFour'] = True
    if num == 5:
        numFive(530,570,550,530,570)
        data['diceFiveFive'] = True
    if num == 6:
        numSix(530,530,530,570,570,570)
        data['diceFiveSix'] = True
        


####################### Roll Dice ###########################


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
    redrawAll()
    
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    x = 0
    for dice in data['dice']:
        if dice == 1:
            numOne(150+x)
        x += 100
        if dice == 2:
            numTwo(165+x,135+x)
        x += 100
        if numThree(
##################Sprite Dice######################
    Sprite(whiteRectangle,(100,100))
    Sprite(whiteRectangle,(200,100))
    Sprite(whiteRectangle,(300,100))
    Sprite(whiteRectangle,(400,100))
    Sprite(whiteRectangle,(500,100))
    Sprite(redCircle,(700,150))
#################Sprite Game Card##################
    Sprite(cardRectangle,(50,250))
    Sprite(cardRectangle,(300,250))
    Sprite(titleCard,(125,250))
    Sprite(titleCard2,(375,250))
    Sprite(text, (250,0))
    Sprite(textRoll, (675,135))
    

if __name__=='__main__':
    
    data = {}
    data['dice'] = [1,2,3,4,5]

    data['diceRoll'] = True
    data['diceRoll2'] = True
    data['diceRoll3'] = True
    data['diceRoll4'] = True
    data['diceRoll5'] = True
    data['diceFiveOne'] = False
    data['diceFiveTwo'] = False
    data['diceFiveThree'] = False
    data['diceFiveFour'] = False
    data['diceFiveFive'] = False
    data['diceFiveSix'] = False
    data['diceOneOne'] = False
    data['diceOneTwo'] = False
    data['diceOneThree'] = False
    data['diceOneFour'] = False
    data['diceOneFive'] = False
    data['diceOneSix'] = False
    data['diceTwoOne'] = False
    data['diceTwoTwo'] = False
    data['diceTwoThree'] = False
    data['diceTwoFour'] = False
    data['diceTwoFive'] = False
    data['diceTwoSix'] = False
    data['diceThreeOne'] = False
    data['diceThreeTwo'] = False
    data['diceThreeThree'] = False
    data['diceThreeFour'] = False
    data['diceThreeFive'] = False
    data['diceThreeSix'] = False
    data['diceFourOne'] = False
    data['diceFourTwo'] = False
    data['diceFourThree'] = False
    data['diceFourFour'] = False
    data['diceFourFive'] = False
    data['diceFourSix'] = False

    redrawAll()
    App().listenMouseEvent("click", mouseClick)
    App().run()

