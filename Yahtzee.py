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
textOne = TextAsset('Ones:' ,fill=black, style='8pt Times')
textTwo = TextAsset('Twos:' ,fill=black, style='8pt Times')
textThree = TextAsset('Threes:' ,fill=black, style='8pt Times')
textFour = TextAsset('Fours:' ,fill=black, style='8pt Times')
textFive = TextAsset('Fives:' ,fill=black, style='8pt Times')
textSix = TextAsset('Sixes:' ,fill=black, style='8pt Times')
text3ofakind = TextAsset('3 of a kind:' ,fill=black, style='8pt Times')
text4ofakind = TextAsset('4 of a kind:' ,fill=black, style='8pt Times')
textfullhouse = TextAsset('Full House:' ,fill=black, style='8pt Times')
textlargestraight = TextAsset('Large Str:' ,fill=black, style='8pt Times')
textsmallstraight = TextAsset('Small Str:' ,fill=black, style='8pt Times')
textYahtzee = TextAsset('Yahtzee:' ,fill=black, style='8pt Times')
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

def ones():
    count = data['dice'].count(1)
    data['scoreCard'][0] = [count]

def twos():
    count = data['dice'].count(2)
    data['scoreCard'][1][0] = [count]
    
def threes():
    count = data['dice'].count(3)
    data['scoreCard'][2][0] = [count]
    return True

def fours():
    count = data['dice'].count(4)
    print('4:',count*4)
    return True
    
def fives():
    count = data['dice'].count(5)
    print('5:',count*5)
    return True
    
def sixes():
    count = data['dice'].count(6)
    print('6:',count*6)
    return True
    
def is3ofakind():
    for num in data['dice']:
        count = data['dice'].count(num)
        if count == 3:
            print('3ofk:', sum(data['dice']))
            return True
    return False
            
def is4ofakind():
    for num in data['dice']:
        count = data['dice'].count(num)
        if count == 4:
            print('4ofk:' ,sum(data['dice']))
            return True
    return False
            
def isfullhouse():        
    data['dice'].sort() 
    count1 = data['dice'].count(data['dice'][0])
    count2 = data['dice'].count(data['dice'][4])
    if (count1 == 3 and count2 == 2) or (count1 == 2 and count2 == 3):
        print('fh:','25')
        return True
    else:
        return False
            
def issmallstraight():                              ####smallstraight problem
    data['dice'].sort()
    if 1 in data['dice'] and 2 in data['dice'] and 3 in data['dice'] and 4 in data['dice']:
        print('smallstr:','30')
        return True
    elif 2 in data['dice'] and 3 in data['dice'] and 4 in data['dice'] and 5 in data['dice']:
        print('smallstr:','30')
        return True
    elif 3 in data['dice'] and 4 in data['dice'] and 5 in data['dice'] and 6 in data['dice']:
        print('smallstr:','30')
        return True
    else:
        return False

            
def islargestraight():                                          
    for num in data['dice']:
        data['dice'].sort()
        if data['dice'] == [1,2,3,4,5]:
            print('lgstr:','40')
            return True
        elif data['dice'] == [2,3,4,5,6]:
            print('lgstr:','40')
            return True
        else:
            return False

def ischance():
    print('chance:',sum(data['dice']))
    return True
    
def isYahtzee():
        for num in data['dice']:
            count = data['dice'].count(num)
            if count == 5:
                print('Yahtezz:','100')
                return True
            else:
                return False
#########################Dice Roll###############################

def diceRoll():
    for num in range(0,5):
        if num+1 in data['dicePick']:
            data['dice'][num] = randint(1,6)

########################Roll Button####################################
def mouseClick(event):
    if event.x <= 750 and event.x >=650 and event.y <= 200 and event.y >= 100 and data['rollCount'] == []:
        print('turn is over')

    elif event.x <= 750 and event.x >=650 and event.y <= 200 and event.y >= 100:
        data['rollCount'].remove(1)
        diceRoll()
#################################Pick Dice#############################
    x = 0
    for dice in range(1,6):
        if event.x >= 100+x and event.x <= 200+x and event.y >= 100 and event.y <= 200:
            data['dicePick'].remove(dice)
            print(data['dice'])
            if data['dicePick'] == []:
                data['rollCount'] = []
        x += 100
        
    redrawAll()
##############################Score################################### H
    if event.x >= 300 and event.x <= 370 and event.y >= 275 and event.y <= 290:
        ones()
    if event.x >= 300 and event.x <= 370 and event.y >= 275 and event.y <= 290:
        twos()
    if event.x >= 300 and event.x <= 370 and event.y >= 275 and event.y <= 290:
        threes()
    if event.x >= 300 and event.x <= 370 and event.y >= 275 and event.y <= 290:
        fours()
    if event.x >= 300 and event.x <= 370 and event.y >= 275 and event.y <= 290:
        fives()
    if event.x >= 300 and event.x <= 370 and event.y >= 275 and event.y <= 290:
        sixes()
    if event.x >= 300 and event.x <= 370 and event.y >= 275 and event.y <= 290:
        sevens()
    
#################################redrawAll################################
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
        
    oneScore = TextAsset(str(data['scoreCard'][0]) ,fill=black, style='8pt Times')
    TwoScore = TextAsset(str(data['scoreCard'][1][0]) ,fill=black, style='8pt Times')
    ThreeScore = TextAsset(str(data['scoreCard'][2][0]) ,fill=black, style='8pt Times')
    FourScore = TextAsset(str(data['scoreCard'][3][0]) ,fill=black, style='8pt Times')
    FiveScore = TextAsset(str(data['scoreCard'][4][0]) ,fill=black, style='8pt Times')
    SixScore = TextAsset(str(data['scoreCard'][5][0]) ,fill=black, style='8pt Times')
    
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
    
    
####################Card 1#################
    Sprite(textOne,(60,280))
    Sprite(textTwo,(60,300))
    Sprite(textThree,(60,320))
    Sprite(textFour,(60,340))
    Sprite(textFive,(60,360))
    Sprite(textSix,(60,380))
    Sprite(text3ofakind,(60,400))
    Sprite(text4ofakind,(60,420))
    Sprite(textfullhouse,(60,440))
    Sprite(textsmallstraight,(60,460))
    Sprite(textlargestraight,(60,480))
    Sprite(textYahtzee,(60,500))
    
##################Card 2###################
    Sprite(textOne,(310,280))
    Sprite(oneScore,(360,280))
    Sprite(textTwo,(310,300))
    Sprite(textThree,(310,320))
    Sprite(textFour,(310,340))
    Sprite(textFive,(310,360))
    Sprite(textSix,(310,380))
    Sprite(text3ofakind,(310,400))
    Sprite(text4ofakind,(310,420))
    Sprite(textfullhouse,(310,440))
    Sprite(textsmallstraight,(310,460))
    Sprite(textlargestraight,(310,480))
    Sprite(textYahtzee,(310,500))

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
    data['rollCount'] = [1,1,1]
    data['scoreCard'] = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    
    redrawAll()
    App().listenMouseEvent("click", mouseClick)
    App().run()