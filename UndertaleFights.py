from cmu_graphics import *

import random

Damage= Sound('https://audio.jukehost.co.uk/tFaRS9C8yNDqqTcnrnY698Ccgtb6kc9R')

TrueHero = Sound('TrueHero.mp3')

GameOverTheme = Sound('https://audio.jukehost.co.uk/HZHmjiT4ZqqfPEj9A3F9Bts0F9ERiWiE')

Instructions = Group(
                    Label('WASD or', 55, 20, size=20, fill='white'),
                    Label('arrows', 55, 40, size=20, fill='white'),
                    Label('to move', 55, 55, size=20, fill='white')
                    )
Instructions.toFront()

for i in range (5):
    GreenLine1 = Line(100*i, 0, 100*i, 400, fill='limeGreen')
    GreenLine2 = Line(0, 100*i, 400, 100*i, fill='limeGreen')
    
GreenLine1.toBack()
GreenLine2.toBack()

#Undyne = Image('https://www.pngkey.com/png/full/170-1707652_undyne-the-undying-undyne-the-undying-sprite-png.png', 115, 0)
Undyne= Image('UndyneSprite.gif', 115, 0)
Undyne.width= Undyne.width/1.5
Undyne.height = Undyne.height/1.5

Chara = Image('https://i.ytimg.com/vi/qE2Ng3-yKjk/hqdefault.jpg', 115, 0)
Chara.width= Chara.width/2
Chara.height= Chara.height/2
timer1 = Label(20, 500, 500)
app.background = 'black'
Canvas = Rect(100, 200, 200, 150, fill= 'black', border= 'white', borderWidth= 5)

SpearSoundEffect = Sound('https://audio.jukehost.co.uk/Hsm3kq9pqnjgOXzR7JuYjX8JRdurNHPo')

Spear = Line(50, 5, 50, 50, fill='lightBlue', arrowStart=True, lineWidth=2, visible=False)
Spear.speed=5

PointCounter = Label(0, 360, 35, size=25, fill='white')

Score = Label('Score:', 288, 35, size=25, fill='white')

HpDepleted = Rect(160, 365, 92, 19, fill='darkRed')

HpBar = Rect(160, 365, 92, 19, fill='yellow')

HpText = Label('HP', 140, 375, fill='white', size=20)

HpCounter = Label(92, 270, 375, size=20, fill='white')

HpMax = Label('/92', 295, 375, size=20, fill='white')

LV= Label('LV 19', 90, 375, size=20, fill='white')

GameOverPointCounter = Label(PointCounter.value, 230, 150, fill='white', size = 20, visible=False)
    
Player = Group(
        Rect(Canvas.centerX, Canvas.centerY-2, 10, 15, fill='Red', rotateAngle=45),
        Rect(Canvas.centerX-4, Canvas.centerY-2, 10, 15, fill='Red', rotateAngle=-45)
        )

def onKeyHold(keys):
    if (('up' in keys) or ('w' in keys)):
        Player.centerY-=7
    if (('down' in keys) or ('s' in keys)):
        Player.centerY+=7 
    if (('left' in keys) or ('a' in keys)):
        Player.centerX-=7
    if (('right' in keys) or ('d' in keys)):
        Player.centerX+=7
        
    if Player.top < 205:
        Player.top = 205
    
    if Player.bottom >345:
        Player.bottom = 345
    
    if Player.left < 105:
        Player.left=105
    
    if Player.right >295:
        Player.right=295
        

spawnPosition = [(70, 315,20), (70, 225,30), (120,170,40), (280,175,60),(325,230,140),(330,320,200)]
def spawn():
    Chance = randrange(100)
    #print(Chance,Spear.visible,Spear.centerX,Spear.centerY)
    if Chance < 50 and Spear.visible==False:
        max_len = len(spawnPosition)
        X, Y, rotateAngle= spawnPosition[randrange(max_len)]   
        
        Spear.visible=True
        Spear.centerX= X
        Spear.centerY= Y
        Spear.rotateAngle= rotateAngle
        #SpearSoundEffect.play()
        if Spear.speed<20:
            Spear.speed+=0.5
        
        Spear.rotateAngle = angleTo(Spear.centerX, Spear.centerY, Player.centerX, Player.centerY)

GameOverScreen = Group(
                Rect(0, 0, 400, 400, fill='black'),
                Label('GAME OVER', 200, 100, fill='white', size = 25),
                Label('Score:', 170, 150, fill='white', size = 20),
                GameOverPointCounter,
                Label('Press Run to try again', 200, 200, fill='white', size=20),
                )
GameOverScreen.visible = False  

def onStep():
                
    if GameOverScreen.visible==False:
        PointCounter.value+=10
        spawn()  
    
    if timer1.value < 0:
        Spear.visible=False
    Spear.toFront()    
    
    if Spear.visible:
        Spear.centerX, Spear.centerY = getPointInDir(Spear.centerX, Spear.centerY, Spear.rotateAngle, Spear.speed)
    if Spear.centerX>410 or Spear.centerY>410 or Spear.centerX<-10 or Spear.centerY<-10:
        Spear.visible=False
    if Spear.hitsShape(Player) and HpBar.width>1:
        HpBar.width-=1
        HpCounter.value-=1
        #Damage.play()
        
    if Spear.hitsShape(Player) and HpBar.width==1:
        HpBar.visible=False
        GameOverScreen.visible=True   
    #if GameOverScreen.visible==False:
        #TrueHero.play(loop=True) 
    elif GameOverScreen.visible==True:
        #TrueHero.pause()
        #SpearSoundEffect.pause()
        Spear.visible=False
        #GameOverTheme.play(loop=True)
        Instructions.visible=False
    GameOverPointCounter.value=PointCounter.value    

cmu_graphics.run()