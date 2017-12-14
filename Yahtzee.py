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
text = TextAsset('Yahtzee' ,fill=red, style='bold 40pt Times')

def mouseClick(event):
    if event.x <= 150 and event.y <= 150:
        return diceRoll1()
        return diceRoll2()

def diceRoll1():
    num = randint(1,6)
    if num == 1:
        Sprite(blackCircle,(150,150))
    if num == 2:
        Sprite(blackCircle,(165,130))
        Sprite(blackCircle,(135,170))
    if num == 3:
        Sprite(blackCircle,(165,130))
        Sprite(blackCircle,(150,150))
        Sprite(blackCircle,(135,170))
    if num == 4:
        Sprite(blackCircle,(130,130))
        Sprite(blackCircle,(130,170))
        Sprite(blackCircle,(170,130))
        Sprite(blackCircle,(170,170))
    if num == 5:
        Sprite(blackCircle,(130,130))
        Sprite(blackCircle,(130,170))
        Sprite(blackCircle,(150,150))
        Sprite(blackCircle,(170,130))
        Sprite(blackCircle,(170,170))
    if num == 6:
        Sprite(blackCircle,(130,130))
        Sprite(blackCircle,(130,150))
        Sprite(blackCircle,(130,170))
        Sprite(blackCircle,(170,130))
        Sprite(blackCircle,(170,150))
        Sprite(blackCircle,(170,170))
        
def diceRoll2():
    num = randint(1,6)
    if num == 1:
        Sprite(blackCircle,(250,250))
    if num == 2:
        Sprite(blackCircle,(265,230))
        Sprite(blackCircle,(235,270))
    if num == 3:
        Sprite(blackCircle,(265,230))
        Sprite(blackCircle,(250,250))
        Sprite(blackCircle,(235,270))
    if num == 4:
        Sprite(blackCircle,(230,230))
        Sprite(blackCircle,(230,270))
        Sprite(blackCircle,(270,230))
        Sprite(blackCircle,(270,270))
    if num == 5:
        Sprite(blackCircle,(230,130))
        Sprite(blackCircle,(230,170))
        Sprite(blackCircle,(250,150))
        Sprite(blackCircle,(270,130))
        Sprite(blackCircle,(270,170))
    if num == 6:
        Sprite(blackCircle,(230,130))
        Sprite(blackCircle,(230,150))
        Sprite(blackCircle,(230,170))
        Sprite(blackCircle,(270,130))
        Sprite(blackCircle,(270,150))
        Sprite(blackCircle,(270,170))
        
Sprite(whiteRectangle,(100,100))
Sprite(whiteRectangle,(200,100))
Sprite(whiteRectangle,(300,100))
Sprite(whiteRectangle,(400,100))
Sprite(text, (200,0))
App().listenMouseEvent("click", mouseClick)
App().run()



