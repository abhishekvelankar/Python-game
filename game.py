#pygame
import pygame


def checkCollision(x,y,treasureX,treasureY):
    global screen,textWin
    collisionState = False
    if y >= treasureY and y <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            
            y = 650
            collisionState = True
        elif x +35 >= treasureX and x + 35 <= treasureX + 35: 
            
            y = 650
            collisionState = True
    elif y + 40 >= treasureY and y + 40 <= treasureY + 40:
        if x >= treasureX and x <= treasureX + 35:
            
            y = 650
            collisionState = True
        elif x+35 >= treasureX and x+35 <= treasureX + 35:
            
            y = 650
            collisionState = True
    return collisionState, y
pygame.init()
#creating screen with size
screen = pygame.display.set_mode((900,700))

#to check whether the game is finished or not
finished = False
x = 450-35/2
y = 650
playerImage = pygame.image.load("Player.png")
playerImage = pygame.transform.scale(playerImage,(35,40))#rescaling image
playerImage = playerImage.convert_alpha() #make it ready to use. alpha to get rid of background

backgroundImage = pygame.image.load("bg.png")
backgroundImage = pygame.transform.scale(backgroundImage,(900,700))
screen.blit(backgroundImage,(0,0))

treasureImage = pygame.image.load("Treasure.png")
treasureImage = pygame.transform.scale(treasureImage,(35,40))
treasureImage = treasureImage.convert_alpha()
treasureX = 450-35/2
treasureY = 50

enemyImage = pygame.image.load("Enemy.png")
enemyImage = pygame.transform.scale(enemyImage,(35,40))
enemyImage = enemyImage.convert_alpha()
enemyX = 100
enemyY = 580-10

screen.blit(treasureImage,(treasureX,treasureY))

font = pygame.font.SysFont("comicsans",60)
level = 1
enemyNames = {0:"MAX",1:"JOHN",2:"YO",3:"TINITNI"}

textWin = font.render("Great Treasure!!",True,(0,0,0)) #creating winning screen True for anti aliasing
name = ""
movingRight = True
enemies = [(enemyX,enemyY,movingRight)]

frame = pygame.time.Clock() # using clock for limiting frame rate
collisionTreasure = False
collisionEnemy = False
#print pygame.K_SPACE #space bar key in game
#-------------------------start of while --------------------------------------
while finished == False: # while game is not finished
    for event in pygame.event.get(): # event object into get method gives all the info about latest info
        #pass #if you dont want to do anything in loop put pass 
        if event.type == pygame.QUIT: #type is a property of event. checking if pygame contains quit event or not
            finished = True



    pressedKeys = pygame.key.get_pressed()#returns all of the pressed keys in list
    #[....,UP,DOWN,SPACE,.....]
    enemyIndex = 0
    for enemyX,enemyY,movingRight in enemies:
        if enemyX >= 800-35:
            movingRight = False
        elif enemyX <= 100:
            movingRight = True

        if movingRight == True:
            enemyX = enemyX + 5 * level
        else:
            enemyX = enemyX - 5 * level
        enemies[enemyIndex] = (enemyX,enemyY,movingRight)
        enemyIndex = enemyIndex + 1
    if pressedKeys[pygame.K_SPACE] == 1:
        y = y - 5
    #rectOne = pygame.Rect(x,y,30,30) #x y width height
    color = (0,0,255)  #RGB
    white = (255,255,255)
    #screen.fill(white) #to eliminate the blue trail of moving block
    screen.blit(backgroundImage,(0,0))
    screen.blit(treasureImage,(treasureX,treasureY))
    screen.blit(playerImage, (x,y))

    enemyIndex = 0
    for enemyX,enemyY,movingRight in enemies:
        screen.blit(enemyImage, (enemyX,enemyY))
        collisionEnemy,y = checkCollision(x,y,enemyX,enemyY)
        if collisionEnemy == True:
            name = enemyNames[enemyIndex]
            textLose = font.render("YOU were killed by " + name,True,(255,0,0))
            screen.blit(textLose,(450-textLose.get_width()/2,350-textLose.get_height()/2))
            pygame.display.flip()
            frame.tick(1)
        frame.tick(30)
        enemyIndex = enemyIndex + 1
    collisionTreasure,y = checkCollision(x,y,treasureX,treasureY)

    if collisionTreasure == True:
        level = level + 1
        enemies.append((enemyX-50*level,enemyY-50*level,False))
        textNextLevel = font.render("LOADING NEXT LEVEL " + str(level),True,(0,0,0))
        screen.blit(textNextLevel,(450-textNextLevel.get_width()/2,350-textNextLevel.get_height()/2))
        pygame.display.flip()
        frame.tick(1)
    
    #pygame.draw.rect(screen,color,rectOne)
    pygame.display.flip() #flip method allows us to update display
    frame.tick(30) #number represents the frame rate




    
