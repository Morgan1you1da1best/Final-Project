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

def pickNum():
    if event.x <= 150 and event.y <= 150:
        Sprite(whiteRectangle,(100,100))
        












def mouseClick(event):
    diceRoll()
    diceRoll2()
    diceRoll3()
    diceRoll4()
    diceRoll5()

def diceRoll():
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
        Sprite(blackCircle,(130,125))
        Sprite(blackCircle,(130,150))
        Sprite(blackCircle,(130,175))
        Sprite(blackCircle,(170,125))
        Sprite(blackCircle,(170,150))
        Sprite(blackCircle,(170,175))
        
def diceRoll2():
    num = randint(1,6)
    if num == 1:
        Sprite(blackCircle,(250,150))
    if num == 2:
        Sprite(blackCircle,(265,130))
        Sprite(blackCircle,(235,170))
    if num == 3:
        Sprite(blackCircle,(265,130))
        Sprite(blackCircle,(250,150))
        Sprite(blackCircle,(235,170))
    if num == 4:
        Sprite(blackCircle,(230,130))
        Sprite(blackCircle,(230,170))
        Sprite(blackCircle,(270,130))
        Sprite(blackCircle,(270,170))
    if num == 5:
        Sprite(blackCircle,(230,130))
        Sprite(blackCircle,(230,170))
        Sprite(blackCircle,(250,150))
        Sprite(blackCircle,(270,130))
        Sprite(blackCircle,(270,170))
    if num == 6:
        Sprite(blackCircle,(230,125))
        Sprite(blackCircle,(230,150))
        Sprite(blackCircle,(230,175))
        Sprite(blackCircle,(270,125))
        Sprite(blackCircle,(270,150))
        Sprite(blackCircle,(270,175))
        
def diceRoll3():
    num = randint(1,6)
    if num == 1:
        Sprite(blackCircle,(350,150))
    if num == 2:
        Sprite(blackCircle,(365,130))
        Sprite(blackCircle,(335,170))
    if num == 3:
        Sprite(blackCircle,(365,130))
        Sprite(blackCircle,(350,150))
        Sprite(blackCircle,(335,170))
    if num == 4:
        Sprite(blackCircle,(330,130))
        Sprite(blackCircle,(330,170))
        Sprite(blackCircle,(370,130))
        Sprite(blackCircle,(370,170))
    if num == 5:
        Sprite(blackCircle,(330,130))
        Sprite(blackCircle,(330,170))
        Sprite(blackCircle,(350,150))
        Sprite(blackCircle,(370,130))
        Sprite(blackCircle,(370,170))
    if num == 6:
        Sprite(blackCircle,(330,125))
        Sprite(blackCircle,(330,150))
        Sprite(blackCircle,(330,175))
        Sprite(blackCircle,(370,125))
        Sprite(blackCircle,(370,150))
        Sprite(blackCircle,(370,175))
        
def diceRoll4():
    num = randint(1,6)
    if num == 1:
        Sprite(blackCircle,(450,150))
    if num == 2:
        Sprite(blackCircle,(465,130))
        Sprite(blackCircle,(435,170))
    if num == 3:
        Sprite(blackCircle,(465,130))
        Sprite(blackCircle,(450,150))
        Sprite(blackCircle,(435,170))
    if num == 4:
        Sprite(blackCircle,(430,130))
        Sprite(blackCircle,(430,170))
        Sprite(blackCircle,(470,130))
        Sprite(blackCircle,(470,170))
    if num == 5:
        Sprite(blackCircle,(430,130))
        Sprite(blackCircle,(430,170))
        Sprite(blackCircle,(450,150))
        Sprite(blackCircle,(470,130))
        Sprite(blackCircle,(470,170))
    if num == 6:
        Sprite(blackCircle,(430,125))
        Sprite(blackCircle,(430,150))
        Sprite(blackCircle,(430,175))
        Sprite(blackCircle,(470,125))
        Sprite(blackCircle,(470,150))
        Sprite(blackCircle,(470,175))

def diceRoll5():
    num = randint(1,6)
    if num == 1:
        Sprite(blackCircle,(550,150))
    if num == 2:
        Sprite(blackCircle,(565,130))
        Sprite(blackCircle,(535,170))
    if num == 3:
        Sprite(blackCircle,(565,130))
        Sprite(blackCircle,(550,150))
        Sprite(blackCircle,(535,170))
    if num == 4:
        Sprite(blackCircle,(530,130))
        Sprite(blackCircle,(530,170))
        Sprite(blackCircle,(570,130))
        Sprite(blackCircle,(570,170))
    if num == 5:
        Sprite(blackCircle,(530,130))
        Sprite(blackCircle,(530,170))
        Sprite(blackCircle,(550,150))
        Sprite(blackCircle,(570,130))
        Sprite(blackCircle,(570,170))
    if num == 6:
        Sprite(blackCircle,(530,125))
        Sprite(blackCircle,(530,150))
        Sprite(blackCircle,(530,175))
        Sprite(blackCircle,(570,125))
        Sprite(blackCircle,(570,150))
        Sprite(blackCircle,(570,175))

Sprite(whiteRectangle,(100,100))
Sprite(whiteRectangle,(200,100))
Sprite(whiteRectangle,(300,100))
Sprite(whiteRectangle,(400,100))
Sprite(whiteRectangle,(500,100))
Sprite(text, (250,0))
App().listenMouseEvent("click", mouseClick)
App().run()



