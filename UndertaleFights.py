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

UndertaleFightsLabel = Label('Undertale Fights', 200, 50, fill='white', size= 40, bold=True)
UndyneButtonRect = Rect(135, 100, 130, 60, fill= 'black', border= 'white', borderWidth=3)
UndyneButtonLabel = Label('Undyne', UndyneButtonRect.centerX, 
UndyneButtonRect.centerY, size= 30, fill='white', bold=True)

CharaButtonRect = Rect(135, 200, 130, 60, fill= 'black', border= 'white', borderWidth=3)
CharaButtonLabel = Label('Chara', CharaButtonRect.centerX, 
CharaButtonRect.centerY, size= 30, fill='white', bold=True)

DifficultyButtonRect = Rect(135, 300, 130, 60, fill= 'black', border= 'white', borderWidth=3)
DifficultyButtonLabel = Label('Difficulty', DifficultyButtonRect.centerX, 
DifficultyButtonRect.centerY, size= 27.5, fill='white', bold=True)

DifficultiesLabel = Label('Difficulties', 200, 50, fill='white', size= 40, bold=True)
EasyButtonRect = Rect(135, 100, 130, 60, fill= 'black', border= 'white', borderWidth=3)
EasyButtonLabel = Label('Easy', EasyButtonRect.centerX, 
EasyButtonRect.centerY, size= 30, fill='white', bold=True)

MediumButtonRect = Rect(135, 200, 130, 60, fill= 'black', border= 'white', borderWidth=3)
MediumButtonLabel = Label('Medium', MediumButtonRect.centerX, 
MediumButtonRect.centerY, size= 30, fill='white', bold=True)

HardButtonRect = Rect(135, 300, 130, 60, fill= 'black', border= 'white', borderWidth=3)
HardButtonLabel = Label('Hard', HardButtonRect.centerX, 
HardButtonRect.centerY, size= 27.5, fill='white', bold=True)

app.Character = None
app.Difficulty = None

MousePressCount = Label(0, 300, 50, visible= False)

SelectionScreen = Group(UndertaleFightsLabel, UndyneButtonRect, UndyneButtonLabel,
                        CharaButtonRect, CharaButtonLabel, DifficultyButtonRect, 
                        DifficultyButtonLabel)

DifficultyScreen= Group(DifficultiesLabel, EasyButtonRect, EasyButtonLabel,
                        MediumButtonRect, MediumButtonLabel, HardButtonRect,
                        HardButtonLabel)     

DifficultyScreen.visible= False    

Knife = Group(Rect(20, 50, 5, 10, fill='red', border='darkRed'),
                Arc(20, 50, 20, 75, 0, 90, fill='red', border='darkRed')  
                )

Knife.visible= False  
Knife.speed= 5  

'''
for i in range (5):
    GreenLine1 = Line(100*i, 0, 100*i, 400, fill='limeGreen')
    GreenLine2 = Line(0, 100*i, 400, 100*i, fill='limeGreen')
    
GreenLine1.toBack()
GreenLine2.toBack()
'''
#Undyne = Image('https://www.pngkey.com/png/full/170-1707652_undyne-the-undying-undyne-the-undying-sprite-png.png', 115, 0)
Undyne= Image('UndyneSprite.gif', 115, 0)
Undyne.width= Undyne.width/1.5
Undyne.height = Undyne.height/1.5
Undyne.visible = False

Chara = Image('https://i.ytimg.com/vi/qE2Ng3-yKjk/hqdefault.jpg', 80, -10)
Chara.width= Chara.width/2
Chara.height= Chara.height/2
Chara.visible = False
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

GameScreen = Group(timer1, Canvas, PointCounter, Score, HpDepleted, 
                    HpBar, HpText, HpCounter, HpMax, LV, Instructions, Player)  

GameScreen.visible = False          

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

def onMouseMove(mouseX,mouseY):
    if UndyneButtonRect.hits(mouseX, mouseY) or UndyneButtonLabel.hits(mouseX, mouseY):
        UndyneButtonRect.border = 'yellow'
        UndyneButtonLabel.fill= 'yellow'
    
    if UndyneButtonRect.hits(mouseX, mouseY) == False:
        UndyneButtonRect.border = 'white'
        UndyneButtonLabel.fill= 'white'    
    
    if CharaButtonRect.hits(mouseX, mouseY) or CharaButtonLabel.hits(mouseX, mouseY):
        CharaButtonRect.border = 'yellow'
        CharaButtonLabel.fill= 'yellow'
    
    if CharaButtonRect.hits(mouseX, mouseY) == False:
        CharaButtonRect.border = 'white'
        CharaButtonLabel.fill= 'white'  

    if DifficultyButtonRect.hits(mouseX, mouseY) or DifficultyButtonLabel.hits(mouseX, mouseY):
        DifficultyButtonRect.border = 'yellow'
        DifficultyButtonLabel.fill= 'yellow'
        
    if DifficultyButtonRect.hits(mouseX, mouseY) == False:
        DifficultyButtonRect.border = 'white'
        DifficultyButtonLabel.fill= 'white'   
    
    if EasyButtonRect.hits(mouseX, mouseY) or EasyButtonLabel.hits(mouseX, mouseY):
        EasyButtonRect.border = 'yellow'
        EasyButtonLabel.fill= 'yellow'
    
    if EasyButtonRect.hits(mouseX, mouseY) == False:
        EasyButtonRect.border = 'white'
        EasyButtonLabel.fill= 'white' 
    
    if MediumButtonRect.hits(mouseX, mouseY) or MediumButtonLabel.hits(mouseX, mouseY):
        MediumButtonRect.border = 'yellow'
        MediumButtonLabel.fill= 'yellow'
    
    if MediumButtonRect.hits(mouseX, mouseY) == False:
        MediumButtonRect.border = 'white'
        MediumButtonLabel.fill= 'white' 
    
    if HardButtonRect.hits(mouseX, mouseY) or EasyButtonLabel.hits(mouseX, mouseY):
        HardButtonRect.border = 'yellow'
        HardButtonLabel.fill= 'yellow'
    
    if HardButtonRect.hits(mouseX, mouseY) == False:
        HardButtonRect.border = 'white'
        HardButtonLabel.fill= 'white'       

def onMousePress(mouseX,mouseY):
    if UndyneButtonRect.hits(mouseX, mouseY):
        app.Character = 'Undyne'
    if CharaButtonRect.hits(mouseX, mouseY):
        app.Character = 'Chara'
    if UndyneButtonRect.hits(mouseX, mouseY) or CharaButtonRect.hits(mouseX, mouseY):
        SelectionScreen.visible= False 
        DifficultyScreen.visible=False
    if DifficultyButtonRect.hits(mouseX,mouseY):
        DifficultyScreen.visible= True
        MousePressCount.value+=1

    if UndyneButtonRect.hits(mouseX, mouseY) or CharaButtonRect.hits(mouseX, mouseY) or DifficultyButtonRect.hits(mouseX,mouseY):
        SelectionScreen.visible= False
        
    if EasyButtonRect.visible==True and EasyButtonRect.hits(mouseX,mouseY):
        app.Difficulty = 'Easy'
        
    if MediumButtonRect.visible==True and MediumButtonRect.hits(mouseX,mouseY):
        app.Difficulty = 'Medium'    
    
    if HardButtonRect.visible==True and HardButtonRect.hits(mouseX,mouseY) and MousePressCount.value>=2:
        app.Difficulty = 'Hard'   

    if app.Difficulty != None:
        DifficultyScreen.visible=False
        SelectionScreen.visible=True               



def spawn():
    Chance = randrange(100)
    #print(Chance,Spear.visible,Spear.centerX,Spear.centerY)
    if Chance < 50 and Spear.visible==False and app.Character == 'Undyne':
        max_len = len(spawnPosition)
        X, Y, rotateAngle= spawnPosition[randrange(max_len)]   
        
        Undyne.visible=True
        Spear.visible=True
        Spear.centerX= X
        Spear.centerY= Y
        Spear.rotateAngle= rotateAngle
        #SpearSoundEffect.play()
        if Spear.speed<20 and app.Difficulty=='Easy':
            Spear.speed+=0.1

        if Spear.speed<20 and app.Difficulty=='Medium':
            Spear.speed+=0.5

        if Spear.speed<25 and app.Difficulty=='Hard':
            Spear.speed+=1 
        
        Spear.rotateAngle = angleTo(Spear.centerX, Spear.centerY, Player.centerX, Player.centerY)

    if Chance < 50 and Knife.visible==False and app.Character == 'Chara':
        max_len = len(spawnPosition)
        X, Y, rotateAngle= spawnPosition[randrange(max_len)]   
        
        Chara.visible=True
        Knife.visible=True
        Knife.centerX= X
        Knife.centerY= Y
        Knife.rotateAngle= rotateAngle
    
        #SpearSoundEffect.play()

        if Knife.speed<15 and app.Difficulty=='Easy':
            Knife.speed+=0.1

        if Knife.speed<20 and app.Difficulty=='Medium':
            Knife.speed+=0.5

        if Knife.speed<25 and app.Difficulty=='Hard':
            Knife.speed+=1        
        
        Knife.rotateAngle = angleTo(Knife.centerX, Knife.centerY, Player.centerX, Player.centerY)

GameOverScreen = Group(
                Rect(0, 0, 400, 400, fill='black'),
                Label('GAME OVER', 200, 100, fill='white', size = 25),
                Label('Score:', 170, 150, fill='white', size = 20),
                GameOverPointCounter,
                Label('Press Run to try again', 200, 200, fill='white', size=20),
                )
GameOverScreen.visible = False  

def onStep():
                
    if SelectionScreen.visible==False and GameOverScreen.visible==False and DifficultyScreen.visible==False:
        PointCounter.value+=10
        spawn()  
        GameScreen.visible=True    
    
    if timer1.value < 0:
        Spear.visible=False
        Knife.visible=False
    Spear.toFront()  
    Knife.toFront()  
    
    if Spear.visible:
        Spear.centerX, Spear.centerY = getPointInDir(Spear.centerX, Spear.centerY, Spear.rotateAngle, Spear.speed)
    if Spear.centerX>410 or Spear.centerY>410 or Spear.centerX<-10 or Spear.centerY<-10:
        Spear.visible=False
    if Spear.hitsShape(Player) and HpBar.width>1:
        HpBar.width-=1
        HpCounter.value-=1
        #Damage.play()

    if Knife.visible:
        Knife.centerX, Knife.centerY = getPointInDir(Knife.centerX, Knife.centerY, Knife.rotateAngle, Knife.speed)
    if Knife.centerX>410 or Knife.centerY>410 or Knife.centerX<-10 or Knife.centerY<-10:
        Knife.visible=False
    if Knife.hitsShape(Player) and HpBar.width>1:
        HpBar.width-=1
        HpCounter.value-=1      
        
    if (Spear.hitsShape(Player) or Knife.hitsShape(Player)) and HpBar.width==1:
        HpBar.visible=False
        GameOverScreen.visible=True   
    #if GameOverScreen.visible==False:
        #TrueHero.play(loop=True) 
    elif GameOverScreen.visible==True:
        #TrueHero.pause()
        #SpearSoundEffect.pause()
        Spear.visible=False
        Knife.visible=False
        #GameOverTheme.play(loop=True)
        Instructions.visible=False
        GameScreen.visible=False
    GameOverPointCounter.value=PointCounter.value    

cmu_graphics.run()