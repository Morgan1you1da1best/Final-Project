#Morgan Baughman
#12/14/17
#Yahtzee.py

from random import randint
from ggame import*
##############################Colors###########################
red = Color(0xFF0000,1)
green = Color(0x38AD00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
white = Color(0xFFFFFF,1)
############################Consistant Text/Graphics##################
blackOutline = LineStyle(1,black) #pixels, color
whiteRectangle = RectangleAsset(100,100,blackOutline,white) #Width, height, outline, fill.
greenRectangle = RectangleAsset(1000,1000,blackOutline,green) #Width, height, outline, fill.
cardRectangle = RectangleAsset(200,290,blackOutline,white)
blackCircle = CircleAsset(10,blackOutline,black) #Radius, outline, fill.
redCircle = CircleAsset(50,blackOutline,red)
text = TextAsset('Yahtzee' ,fill=black, style='bold 40pt Times')
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
textchance = TextAsset('Chance:' ,fill=black, style='8pt Times')
textYahtzee = TextAsset('Yahtzee:' ,fill=black, style='8pt Times')
texttotal = TextAsset('Total:' ,fill=black, style='8pt Times')
print('Roll the dice!')
####################### Die Roll ############################## Black Dot Sprite Pos.
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


###################################Scoring Functions#1#######################

def ones():
    count = data['dice'].count(1)
    data['scoreCard'][0] = [count]

def twos():
    count = data['dice'].count(2)
    data['scoreCard'][1] = [count*2]
    
def threes():
    count = data['dice'].count(3)
    data['scoreCard'][2] = [count*3]

def fours():
    count = data['dice'].count(4)
    data['scoreCard'][3] = [count*4]
    
def fives():
    count = data['dice'].count(5)
    data['scoreCard'][4] = [count*5]
    
def sixes():
    count = data['dice'].count(6)
    data['scoreCard'][5] = [count*6]
    
def is3ofakind():
    for num in data['dice']:
        count = data['dice'].count(num)
        if count == 3 or count == 4 or count == 5:
            data['scoreCard'][6] = [sum(data['dice'])]
            return True
    return False
            
def is4ofakind():
    for num in data['dice']:
        count = data['dice'].count(num)
        if count == 4 or count == 5:
            data['scoreCard'][7] = [sum(data['dice'])]
            return True
    return False
            
def isfullhouse():        
    data['dice'].sort() 
    count1 = data['dice'].count(data['dice'][0])
    count2 = data['dice'].count(data['dice'][4])
    if (count1 == 3 and count2 == 2) or (count1 == 2 and count2 == 3):
        data['scoreCard'][8] = [25]
        return True
    else:
        return False
            
def issmallstraight():                             
    data['dice'].sort()
    if 1 in data['dice'] and 2 in data['dice'] and 3 in data['dice'] and 4 in data['dice']:
        data['scoreCard'][9] = [30]
        return True
    elif 2 in data['dice'] and 3 in data['dice'] and 4 in data['dice'] and 5 in data['dice']:
        data['scoreCard'][9] = [30]
        return True
    elif 3 in data['dice'] and 4 in data['dice'] and 5 in data['dice'] and 6 in data['dice']:
        data['scoreCard'][9] = [30]
        return True
    else:
        return False
        
def islargestraight():                                          
    for num in data['dice']:
        data['dice'].sort()
        if data['dice'] == [1,2,3,4,5]:
            data['scoreCard'][10] = [40]
            return True
        elif data['dice'] == [2,3,4,5,6]:
            data['scoreCard'][10] = [40]
            return True
        else:
            return False
            
def ischance():
    print('chance:',sum(data['dice']))
    data['scoreCard'][11] = [sum(data['dice'])]
    return True
    
def isYahtzee():
        for num in data['dice']:
            count = data['dice'].count(num)
            if count == 5:
                data['scoreCard'][12] = [50]
                return True
            else:
                return False
###############################Scoring Function#2 ##############################
            
def ones2():
    count = data['dice'].count(1)
    data['scoreCard2'][0] = [count]

def twos2():
    count = data['dice'].count(2)
    data['scoreCard2'][1] = [count*2]
    
def threes2():
    count = data['dice'].count(3)
    data['scoreCard2'][2] = [count*3]

def fours2():
    count = data['dice'].count(4)
    data['scoreCard2'][3] = [count*4]
    
def fives2():
    count = data['dice'].count(5)
    data['scoreCard2'][4] = [count*5]
    
def sixes2():
    count = data['dice'].count(6)
    data['scoreCard2'][5] = [count*6]
    
def is3ofakind2():
    for num in data['dice']:
        count = data['dice'].count(num)
        if count == 3 or count == 4 or count == 5:
            data['scoreCard2'][6] = [sum(data['dice'])]
            return True
    return False
            
def is4ofakind2():
    for num in data['dice']:
        count = data['dice'].count(num)
        if count == 4 or count == 5:
            data['scoreCard2'][7] = [sum(data['dice'])]
            return True
    return False
            
def isfullhouse2():        
    data['dice'].sort() 
    count1 = data['dice'].count(data['dice'][0])
    count2 = data['dice'].count(data['dice'][4])
    if (count1 == 3 and count2 == 2) or (count1 == 2 and count2 == 3):
        data['scoreCard2'][8] = [25]
        return True
    else:
        return False
            
def issmallstraight2():         
    data['dice'].sort()
    if 1 in data['dice'] and 2 in data['dice'] and 3 in data['dice'] and 4 in data['dice']:
        data['scoreCard2'][9] = [30]
        return True
    elif 2 in data['dice'] and 3 in data['dice'] and 4 in data['dice'] and 5 in data['dice']:
        data['scoreCard2'][9] = [30]
        return True
    elif 3 in data['dice'] and 4 in data['dice'] and 5 in data['dice'] and 6 in data['dice']:
        data['scoreCard2'][9] = [30]
        return True
    else:
        return False

def islargestraight2():                                          
    for num in data['dice']:
        data['dice'].sort()
        if data['dice'] == [1,2,3,4,5]:
            data['scoreCard2'][10] = [40]
            return True
        elif data['dice'] == [2,3,4,5,6]:
            data['scoreCard2'][10] = [40]
            return True
        else:
            return False

def ischance2():
    print('chance:',sum(data['dice']))
    data['scoreCard2'][11] = [sum(data['dice'])] 
    return True
    
def isYahtzee2():
        for num in data['dice']:
            count = data['dice'].count(num)
            if count == 5:
                data['scoreCard2'][12] = [50]
                return True
            else:
                return False
############################End Turn############################# Ends turn. Adds to lists inorder to go again.       
def endTurn():
    data['rollCount'] = [1,1,1]
    data['dicePick'] = [1,2,3,4,5]
    print('Next player turn!')

#########################Dice Roll############################### Randomizes and Rolls dice
def diceRoll():
    for num in range(0,5):
        if num+1 in data['dicePick']:
            data['dice'][num] = randint(1,6)
    
def gameOver():
    print(data['scoreCard'][:][:])
    print(data['scoreCard2'][:][:])

########################Roll Button#################################### Cords for pressing 'Roll'
def mouseClick(event):
    if event.x <= 750 and event.x >=650 and event.y <= 200 and event.y >= 100 and data['rollCount'] == []:
        print('0 rolls left')
        print('Double click on the 0 in your desired catagory!')
        
    elif event.x <= 750 and event.x >=650 and event.y <= 200 and event.y >= 100:
        data['rollCount'].remove(1)
        diceRoll()
#################################Pick Dice############################# Pick the dice you want to play
    x = 0
    for dice in range(1,6):
        if event.x >= 100+x and event.x <= 200+x and event.y >= 100 and event.y <= 200:
            if dice in data['dicePick']:
                data['dicePick'].remove(dice)
            if data['dicePick'] == []:
                data['rollCount'] = []
        x += 100
        
    redrawAll()

###################################Score - Card #1 Select############################# Select which score catagory 
    if event.x >= 110 and event.x <= 120 and event.y >= 275 and event.y <= 290:
        ones()
        endTurn()
    if event.x >= 110 and event.x <= 120 and event.y >= 295 and event.y <= 310:
        twos()
        endTurn()
    if event.x >= 110 and event.x <= 120 and event.y >= 315 and event.y <= 330:
        threes()
        endTurn()
    if event.x >= 110 and event.x <= 120 and event.y >= 335 and event.y <= 350:
        fours()
        endTurn()
    if event.x >= 110 and event.x <= 120 and event.y >= 355 and event.y <= 370:
        fives()
        endTurn()
    if event.x >= 110 and event.x <= 120 and event.y >= 375 and event.y <= 390:
        sixes()
        endTurn()
    if event.x >= 120 and event.x <= 130 and event.y >= 395 and event.y <= 410 and is3ofakind() == True:
        is3ofakind()
        endTurn()
    if event.x >= 120 and event.x <= 130 and event.y >= 415 and event.y <= 430 and is4ofakind() == True:
        is4ofakind()
        endTurn()
    if event.x >= 120 and event.x <= 130 and event.y >= 435 and event.y <= 450 and isfullhouse() == True:
        isfullhouse()
        endTurn()
    if event.x >= 120 and event.x <= 130 and event.y >= 455 and event.y <= 470 and issmallstraight() == True:
        issmallstraight()
        endTurn()
    if event.x >= 120 and event.x <= 130 and event.y >= 475 and event.y <= 490 and islargestraight() == True:
        islargestraight()
        endTurn()
    if event.x >= 120 and event.x <= 130 and event.y >= 495 and event.y <= 510 and ischance() == True:
        ischance()
        endTurn()
    if event.x >= 120 and event.x <= 130 and event.y >= 515 and event.y <= 530 and isYahtzee() == True:
        isYahtzee()
        endTurn()
    if event.x >= 150 and event.x <= 170 and event.y >= 270 and event.y <= 290:
        gameOver()
##############################Score - Card #2 Select################################### Pick which score catagory

    if event.x >= 360 and event.x <= 380 and event.y >= 275 and event.y <= 290:
        ones2()
        endTurn()
    if event.x >= 360 and event.x <= 380 and event.y >= 295 and event.y <= 310:
        twos2()
        endTurn()
    if event.x >= 360 and event.x <= 380 and event.y >= 315 and event.y <= 330:
        threes2()
        endTurn()
    if event.x >= 360 and event.x <= 380 and event.y >= 335 and event.y <= 350:
        fours2()
        endTurn()
    if event.x >= 360 and event.x <= 380 and event.y >= 355 and event.y <= 370:
        fives2()
        endTurn()
    if event.x >= 360 and event.x <= 380 and event.y >= 375 and event.y <= 390:
        sixes2()
        endTurn()
    if event.x >= 370 and event.x <= 390 and event.y >= 395 and event.y <= 410 and is3ofakind2() == True:
        is3ofakind2()
        endTurn()
    if event.x >= 370 and event.x <= 390 and event.y >= 415 and event.y <= 430 and is4ofakind2() == True:
        is4ofakind2()
        endTurn()
    if event.x >= 370 and event.x <= 390 and event.y >= 435 and event.y <= 450 and isfullhouse2() == True:
        isfullhouse2()
        endTurn()
    if event.x >= 370 and event.x <= 390 and event.y >= 455 and event.y <= 470 and issmallstraight2() == True:
        issmallstraight2()
        endTurn()
    if event.x >= 370 and event.x <= 390 and event.y >= 475 and event.y <= 490 and islargestraight2() == True:
        islargestraight2()
        endTurn()
    if event.x >= 370 and event.x <= 390 and event.y >= 495 and event.y <= 510 and ischance2() == True:
        ischance2()
        endTurn()  
    if event.x >= 370 and event.x <= 390 and event.y >= 515 and event.y <= 530 and isYahtzee2() == True:
        isYahtzee2()
        endTurn()
#################################redrawAll################################
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
        
    oneScore = TextAsset(str(data['scoreCard'][0][0]) ,fill=black, style='8pt Times')
    twoScore = TextAsset(str(data['scoreCard'][1][0]) ,fill=black, style='8pt Times')
    threeScore = TextAsset(str(data['scoreCard'][2][0]) ,fill=black, style='8pt Times')
    fourScore = TextAsset(str(data['scoreCard'][3][0]) ,fill=black, style='8pt Times')
    fiveScore = TextAsset(str(data['scoreCard'][4][0]) ,fill=black, style='8pt Times')
    sixScore = TextAsset(str(data['scoreCard'][5][0]) ,fill=black, style='8pt Times')
    is3ofakindScore = TextAsset(str(data['scoreCard'][6][0]) ,fill=black, style='8pt Times')
    is4ofakindScore = TextAsset(str(data['scoreCard'][7][0]) ,fill=black, style='8pt Times')
    isfullhouseScore = TextAsset(str(data['scoreCard'][8][0]) ,fill=black, style='8pt Times')
    issmallstraightScore = TextAsset(str(data['scoreCard'][9][0]) ,fill=black, style='8pt Times')
    islargestraightScore = TextAsset(str(data['scoreCard'][10][0]) ,fill=black, style='8pt Times')
    ischanceScore = TextAsset(str(data['scoreCard'][11][0]) ,fill=black, style='8pt Times')
    isyahtzeeScore = TextAsset(str(data['scoreCard'][12][0]) ,fill=black, style='8pt Times')
    sumPlayer1 = TextAsset(sum(data['scoreCard'][:][0]+data['scoreCard'][:][1]+data['scoreCard'][:][2]+data['scoreCard'][:][3]+data['scoreCard'][:][4]+data['scoreCard'][:][5]+data['scoreCard'][:][6]+data['scoreCard'][:][7]+data['scoreCard'][:][8]+data['scoreCard'][:][9]+data['scoreCard'][:][10]+data['scoreCard'][:][11]) ,fill=black, style='8pt Times')
    
    oneScore2 = TextAsset(str(data['scoreCard2'][0][0]) ,fill=black, style='8pt Times')
    twoScore2 = TextAsset(str(data['scoreCard2'][1][0]) ,fill=black, style='8pt Times')
    threeScore2 = TextAsset(str(data['scoreCard2'][2][0]) ,fill=black, style='8pt Times')
    fourScore2 = TextAsset(str(data['scoreCard2'][3][0]) ,fill=black, style='8pt Times')
    fiveScore2 = TextAsset(str(data['scoreCard2'][4][0]) ,fill=black, style='8pt Times')
    sixScore2 = TextAsset(str(data['scoreCard2'][5][0]) ,fill=black, style='8pt Times')
    is3ofakindScore2 = TextAsset(str(data['scoreCard2'][6][0]) ,fill=black, style='8pt Times')
    is4ofakindScore2 = TextAsset(str(data['scoreCard2'][7][0]) ,fill=black, style='8pt Times')
    isfullhouseScore2 = TextAsset(str(data['scoreCard2'][8][0]) ,fill=black, style='8pt Times')
    issmallstraightScore2 = TextAsset(str(data['scoreCard2'][9][0]) ,fill=black, style='8pt Times')
    islargestraightScore2 = TextAsset(str(data['scoreCard2'][10][0]) ,fill=black, style='8pt Times')
    ischanceScore2 = TextAsset(str(data['scoreCard2'][11][0]) ,fill=black, style='8pt Times')
    isyahtzeeScore2 = TextAsset(str(data['scoreCard2'][12][0]) ,fill=black, style='8pt Times')
    sumPlayer2 = TextAsset(sum(data['scoreCard2'][:][0]+data['scoreCard2'][:][1]+data['scoreCard2'][:][2]+data['scoreCard2'][:][3]+data['scoreCard2'][:][4]+data['scoreCard2'][:][5]+data['scoreCard2'][:][6]+data['scoreCard2'][:][7]+data['scoreCard2'][:][8]+data['scoreCard2'][:][9]+data['scoreCard2'][:][10]+data['scoreCard2'][:][11]) ,fill=black, style='8pt Times')
    
    
    Sprite(greenRectangle,(0,0))
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
    
    
####################Card 1################# Sprites
    Sprite(textOne,(60,280))
    Sprite(oneScore,(110,280))
    Sprite(textTwo,(60,300))
    Sprite(twoScore,(110,300))
    Sprite(textThree,(60,320))
    Sprite(threeScore,(110,320))
    Sprite(textFour,(60,340))
    Sprite(fourScore,(110,340))
    Sprite(textFive,(60,360))
    Sprite(fiveScore,(110,360))
    Sprite(textSix,(60,380))
    Sprite(sixScore,(110,380))
    Sprite(text3ofakind,(60,400))
    Sprite(is3ofakindScore,(120,400))
    Sprite(text4ofakind,(60,420))
    Sprite(is4ofakindScore,(120,420))
    Sprite(textfullhouse,(60,440))
    Sprite(isfullhouseScore,(120,440))
    Sprite(textsmallstraight,(60,460))
    Sprite(issmallstraightScore,(120,460))
    Sprite(textlargestraight,(60,480))
    Sprite(islargestraightScore,(120,480))
    Sprite(textchance,(60,500))
    Sprite(ischanceScore,(120,500))
    Sprite(textYahtzee,(60,520))
    Sprite(isyahtzeeScore,(120,520))
    Sprite(texttotal,(130,280))
    Sprite(sumPlayer1, (160,280))
##################Card 2################### Sprites
    Sprite(textOne,(310,280))
    Sprite(oneScore2,(360,280))
    Sprite(textTwo,(310,300))
    Sprite(twoScore2,(360,300))
    Sprite(textThree,(310,320))
    Sprite(threeScore2,(360,320))
    Sprite(textFour,(310,340))
    Sprite(fourScore2,(360,340))
    Sprite(textFive,(310,360))
    Sprite(fiveScore2,(360,360))
    Sprite(textSix,(310,380))
    Sprite(sixScore2,(360,380))
    Sprite(text3ofakind,(310,400))
    Sprite(is3ofakindScore2,(370,400))
    Sprite(text4ofakind,(310,420))
    Sprite(is4ofakindScore2,(370,420))
    Sprite(textfullhouse,(310,440))
    Sprite(isfullhouseScore2,(370,440))
    Sprite(textsmallstraight,(310,460))
    Sprite(issmallstraightScore2,(370,460))
    Sprite(textlargestraight,(310,480))
    Sprite(islargestraightScore2,(370,480))
    Sprite(textchance,(310,500))
    Sprite(ischanceScore2,(370,500))
    Sprite(textYahtzee,(310,520))
    Sprite(isyahtzeeScore2,(370,520))
    Sprite(texttotal,(390,280))
    Sprite(sumPlayer2, (420,280))

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
    data['dice'] = [1,1,1,1,1]
    data['dicePick'] = [1,2,3,4,5]
    data['rollCount'] = [1,1,1]
    data['scoreCard'] = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    data['scoreCard2'] = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
 
    redrawAll()
    App().listenMouseEvent("click", mouseClick)
    App().run()