#Morgan Baughman
#12/19/17
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

Sprite(blackCircle,(150,125))
Sprite(blackCircle,(150,150))
Sprite(blackCircle,(150,175))
Sprite(blackCircle,(200,125))
Sprite(blackCircle,(200,150))
Sprite(blackCircle,(200,175))
App().run()
