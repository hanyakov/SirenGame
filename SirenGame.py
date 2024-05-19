import random
import pgzrun


WIDTH = 800
HEIGHT = 480
CENTER_X = WIDTH/2
CENTER_Y = HEIGHT/2
CENTER = (CENTER_X,CENTER_Y)
FINAL_LEVEL = 4

speed = 3
score=0
won=True
game_over = False
game_complete = False
level = 0
siren=Actor("siren")
finish=Actor("finish")
pearl1=Actor("pearl",pos = (100,-150))
pearl2=Actor("pearl",pos = (100,-150))
siren.pos=(CENTER_X,HEIGHT-35)
finish.pos=(CENTER_X,10)
wire_right=Actor("wire")
wire_left=Actor("wire")
  #level 2
wire_top=Actor(("wire") , pos=(HEIGHT-290,-150))
  #level 3
wire_bottom=Actor(("wire"), pos=(CENTER_X,-150))




def update_wires():
    global score, speed, pearls
    wire_right.x = wire_right.x+(speed)
    wire_left.x =  wire_left.x-(speed)
    wire_top.x = wire_top.x+(speed)
    wire_bottom.y=wire_bottom.y-(0.6)
    
    if wire_right.x>=WIDTH-180 or wire_right.x<=170 or wire_top.x>=WIDTH-180:
        speed=speed *-1

def update_level(level):
    global  score, game_over, pearls,won,speed,game_complete, wire_right, wire_left, wire_top ,wire_pos, pearls_pos
    won  = False
    siren.pos=(CENTER_X,HEIGHT-50)

    
    if level==1 :
      
        wire_right.pos=(200,300)
        wire_left.pos=(600,150)
        speed +=1
        pearl1.pos = (CENTER_X,CENTER_Y)
        pearl2.pos = (CENTER_X,CENTER_Y)


    elif level==2 :
        wire_top.draw()
        wire_right.pos=(200,350)
        wire_left.pos=(600,210)
        wire_top.pos=(HEIGHT-290,90)
        speed +=1.5
        pearl1.pos = (200,200)
        pearl2.pos = (500,400)
        
    elif level==3:
        wire_right.pos=(200,350)
        wire_left.pos=(600,210)
        wire_top.pos=(HEIGHT-290,90)
        wire_bottom.pos=(CENTER_X,500)
        speed +=1
        pearl1.pos = (200,300)
        pearl2.pos = (500,150)
        
    elif level == FINAL_LEVEL:
        game_complete = True

        
def update_siren():
    global game_over, game_complete, won, level, score,pearl1,pearl2
    if keyboard.left:
       siren.x=siren.x-6
    elif keyboard.right:
       siren.x=siren.x+6
    elif keyboard.up:
       siren.y=siren.y-6
    elif keyboard.down:
       siren.y=siren.y+6

    if siren.colliderect(wire_right) or siren.colliderect(wire_left) or siren.colliderect(wire_bottom) or siren.colliderect(wire_top) :
        game_over=True
        
    elif siren.colliderect(finish) and score == 30:
        won=True
        
    elif siren.colliderect(pearl1):
        score=score+10
        pearl1.pos = (0,10000)
        
    elif siren.colliderect(pearl2):
        score=score+10
        pearl2.pos = (0,10000)
    
    if won:
        game_over = False

def update():
    global level,wire_left,wire_right,won, update_level,speed, pearls_pos
    
    if won or siren.colliderect(finish):
        level+=1 
        update_level(level)
        
    update_wires()
    update_siren()
    
def draw():
    global score,game_over,game_complete, level, speed, update_wires
    screen.clear()
    screen.blit('sea',(0,0))
    screen.draw.text("LEVEL "+str(level), color="pink", topleft=(10,10), fontsize=20, shadow=(1,1))
    screen.draw.text("SCORE "+str(score),color="pink",topleft=(10,30),fontsize=30, shadow=(1,1))
    wire_right.draw()
    wire_left.draw()
    wire_top.draw()
    finish.draw()
    siren.draw()
    wire_bottom.draw()
    pearl1.draw()
    pearl2.draw()
    
    if game_over:
        screen.clear()
        screen.blit('sea',(0,0))
        display_message('GAME OVER :(' , "imbecile..")
    elif game_complete:
        screen.clear()
        screen.blit('sea',(0,0))
        display_message('You Won :D', "yay.")
   

def display_message(heading_text,sub_heading_text):
    screen.draw.text(heading_text, fontsize= 60, center = CENTER, color = 'pink', shadow=(1,1))
    screen.draw.text(sub_heading_text,fontsize = 25,center = (CENTER_X, CENTER_Y +35), color = 'pink', shadow=(1,1))

    
pgzrun.go()
