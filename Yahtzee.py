#Morgan Baughman
#12/14/17
#Yahtzee.py

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

Sprite(whiteRectangle,(100,100))
Sprite(whiteRectangle,(200,100))
Sprite(whiteRectangle,(300,100))
Sprite(whiteRectangle,(400,100))
Sprite(blackCircle,(150,150))
Sprite(blackCircle,(250,150))
Sprite(blackCircle,(350,150))
Sprite(blackCircle,(450,150))
Sprite(text, (200,0))
App().run()



