from cmu_graphics import *

import random

Megalovania= Sound('https://audio.jukehost.co.uk/1KkKDRSfDttpIK19wYzJDHaO7FKdufVR')

#Megalovania.play()

Damage= Sound('https://audio.jukehost.co.uk/tFaRS9C8yNDqqTcnrnY698Ccgtb6kc9R')

GameOverTheme = Sound('https://audio.jukehost.co.uk/HZHmjiT4ZqqfPEj9A3F9Bts0F9ERiWiE')

Instructions = Group(
                    Label('WASD or', 55, 20, size=20, fill='white'),
                    Label('arrows', 55, 40, size=20, fill='white'),
                    Label('to move', 55, 55, size=20, fill='white')
                    )

g_sound =Sound("https://audio.jukehost.co.uk/Qpuq8LOKO64BZyFapHfyx6QrBUZhqzYY")
timer1 = Label(20, 500, 500)
app.background = 'black'

Canvas = Rect(100, 200, 200, 150, fill= None, border= 'white', borderWidth= 5)

Sans= Image('https://c.tenor.com/fwKuqJstpRIAAAAC/undertale-sans.gif', 145, 20)
Sans.width=Sans.width/3
Sans.height=Sans.height/3

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

spawnPosition = [(75, 315,-95), (75, 225,-55), (120,160,-45), (280,175,25),(320,230,50),(320,320,100)]

GasterBlaster = Image('https://www.pngkit.com/png/full/905-9058014_gaster-blaster-sprite.png', 0, 0, visible = False)
GasterBlaster.height= GasterBlaster.height/6
GasterBlaster.width= GasterBlaster.width/6

GasterBlasterFire = Image('http://pixelartmaker-data-78746291193.nyc3.digitaloceanspaces.com/image/84a6e1145acc52a.png', 0, 0, visible = False)
GasterBlasterFire.height= GasterBlaster.height
GasterBlasterFire.width= GasterBlaster.width

BlasterBeam = Rect(GasterBlaster.centerX, GasterBlaster.centerY, 30, 400, 
                fill='white', rotateAngle=GasterBlaster.rotateAngle, 
                visible=False, align='top-left', opacity=90)

def spawn():
    Chance = randrange(100)
    if Chance < 4 and GasterBlaster.visible==False:
        max_len = len(spawnPosition)
        X, Y, rotateAngle= spawnPosition[randrange(max_len)]
        if GasterBlaster.centerX==X and g_sound.play()==False:
            return
        
        GasterBlaster.visible=True
        GasterBlaster.centerX=X
        GasterBlaster.centerY=Y
        GasterBlaster.rotateAngle=rotateAngle
        #if GameOverScreen.visible==False:
            #g_sound.play()
        BlasterBeam.rotateAngle= rotateAngle
        GasterBlasterFire.centerX=X
        GasterBlasterFire.centerY=Y
        GasterBlasterFire.rotateAngle= rotateAngle
        timer1.value=40
        BlasterBeam.top= Y
        if GasterBlasterFire.centerX<250:
            BlasterBeam.left= X
        if GasterBlasterFire.centerX>250:
            BlasterBeam.right= X

        if BlasterBeam.rotateAngle==-95:
            BlasterBeam.centerY-=51
        if BlasterBeam.rotateAngle==100:
            BlasterBeam.centerY-=45
        if BlasterBeam.rotateAngle==100:
            BlasterBeam.centerY-=40
        if BlasterBeam.rotateAngle==25:
            BlasterBeam.centerX+=12
        if BlasterBeam.rotateAngle==-55:
            BlasterBeam.centerY-=8
        if BlasterBeam.rotateAngle==50:
            BlasterBeam.centerY-=3
        
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
    
    timer1.value -=1
    if timer1.value < 0:
        GasterBlaster.visible = False
    
    if BlasterBeam.hitsShape(Player) and BlasterBeam.visible==True and HpBar.width>1:    
        HpBar.width-=1
        HpCounter.value-=1
        #Damage.play()
   
    if GasterBlaster.visible==False and GasterBlasterFire.centerY>50:
        BlasterBeam.visible=True
        GasterBlasterFire.visible=True
        GasterBlasterFire.toFront()
        
        
    if GasterBlaster.visible==True:
        BlasterBeam.visible=False
        GasterBlasterFire.visible=False 
        #g_sound.play()
    
    
    if GasterBlasterFire.visible==True:
        BlasterBeam.visible=False
        GasterBlasterFire.visible=False
    
    if BlasterBeam.hitsShape(Player) and HpBar.width==1:
        HpBar.visible=False
        GameOverScreen.visible=True   
    #if GameOverScreen.visible==False:
        #Megalovania.play(loop=True) 
    elif GameOverScreen.visible==True:
        Megalovania.pause()
        #g_sound.pause()
        GasterBlaster.visible=False
        GasterBlasterFire.visible=False
        BlasterBeam.visible=False
        #GameOverTheme.play(loop=True)
        Instructions.visible=False
    GameOverPointCounter.value=PointCounter.value

cmu_graphics.run()