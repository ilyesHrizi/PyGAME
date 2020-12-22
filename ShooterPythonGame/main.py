#this the first window that gona show at the first screen 1
import random
import math
import  pygame
from pygame import mixer

# initalize pygame 2
pygame.init()
#Create the screen 3
screen = pygame.display.set_mode((800,600))
# Title and Icon 5
pygame.display.set_caption("Space Game")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)
# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

#Background
background = pygame.image.load("BackGround.jpg")
# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10
# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
#Player  6
playerImg = pygame.image.load("Player.png")
playerX = 370
playerY = 480
player_change = 0
def player(x,y) :
    screen.blit(playerImg , (x,y))
#enemy
enemyImg = []
enemyX =[]
enemyY =[]
enemy_changeX =[]
enemy_changeY =[]
num_of_enemie = 6
for i in range(6) :
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemy_changeX.append(0.4)
    enemy_changeY.append(40)
def enemy(x,y,i) :
    screen.blit(enemyImg[i],(x,y))
#bullet
#ready state you can see the bullet on the screen
#bullet moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bullet_changeX = 0.2
bullet_changeY = 2
bullet_state = "ready"
def fire_bullet(x,y) :
    global  bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg , (x + 16,y + 10))
def isCollision(enemyX,enemyY,bulletX,bulletY) :
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if(distance <27 ) :
        return True
    else :
        return False
Score = 0
#Game Loop turn off the screen 4
running = True
while running:

    #playerX += 0.1
    # RGB = ref , green , blue 5
    screen.fill((0, 0, 0))
    #backgrounfd image
    screen.blit(background ,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #check wish key is pressed

        if(event.type == pygame.KEYDOWN) :
            if(event.key== pygame.K_LEFT) :
                player_change -= 0.8

            if (event.key == pygame.K_RIGHT):
                player_change += 0.8
            if (event.key == pygame.K_SPACE):
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if(event.type == pygame.KEYUP):
            if (event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT):
                player_change = 0
    if bulletY <=0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bullet_changeY


    #Call Player
    playerX += player_change
    #Check for boundries
    if(playerX <= 0 ):
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX,playerY)
    #Call enemy
    # Check for boundries
    for i in range(num_of_enemie):
        # Game Over
        if score_value > 7 :
            game_over_text()
            break
        enemyX[i] += enemy_changeX[i]
        if (enemyX[i] <= 0):
            enemy_changeX[i] = 0.2
            enemyY[i] += enemy_changeY[i]
        elif enemyX[i] >= 736:
            enemy_changeX[i] = -0.2
            enemyY[i] += enemy_changeY[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(Score)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)
# bullet movement
    show_score(textX, testY)

    #every change you need to update the display
    pygame.display.update()
