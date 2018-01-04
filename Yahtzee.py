#Morgan Baughman
#12/14/17
#Yahtzee.py

from random import randint
from ggame import*


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
    for num in range(0,5):
        if num+1 in data['dicePick']:
            data['dice'][num] = randint(1,6)

########################Roll Button####################################
def mouseClick(event):
    if event.x <= 750 and event.x >=650 and event.y <= 200 and event.y >= 100:
        diceRoll()
#################################Pick Dice#############################
    x = 0
    for dice in range(1,6):
        if event.x >= 100+x and event.x <= 200+x and event.y >= 100 and event.y <= 200:
            data['dicePick'].remove(dice)
            if 1 in data['dice']:
                data['score'].append(1)
            if 2 in data['dice']:
                data['score'].append(2)
            if 3 in data['dice']:
                data['score'].append(3)
            if 4 in data['dice']:
                data['score'].append(4)
            if 5 in data['dice']:
                data['score'].append(5)
            if 6 in data['dice']:
                data['score'].append(6)
                scoreCard()
        x += 100
        
    redrawAll()
    
def scoreCard():
    print(data['score'][:])
#################################redrawAll################################
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()


    Sprite(whiteRectangle,(100,100))
    Sprite(whiteRectangle,(200,100))
    Sprite(whiteRectangle,(300,100))
    Sprite(whiteRectangle,(400,100))
    Sprite(whiteRectangle,(500,100))
    Sprite(redCircle,(700,150))
    Sprite(cardRectangle,(50,250))
    Sprite(cardRectangle,(300,250))
    Sprite(titleCard,(125,250))
    Sprite(titleCard2,(375,250))
    Sprite(text,(250,0))
    Sprite(textRoll,(675,135))
    
    x = 0
    for dice in data['dice']:
        if dice == 1:
            numOne(150+x)
        if dice == 2:
            numTwo(165+x,135+x)
        if dice == 3:
            numThree(170+x,150+x,130+x)
        if dice == 4:
            numFour(130+x,170+x,130+x,170+x)
        if dice == 5:
            numFive(130+x,170+x,150+x,130+x,170+x)
        if dice == 6:
            numSix(130+x,130+x,130+x,170+x,170+x,170+x)
        x += 100
        

if __name__=='__main__':
    

    data = {}
    data['dice'] = [1,2,3,4,5]
    data['dicePick'] = [1,2,3,4,5]
    data['score'] = [1,2,3,4,5,6]

    
    redrawAll()
    App().listenMouseEvent("click", mouseClick)
    App().run()