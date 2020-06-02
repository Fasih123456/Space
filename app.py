import pygame
import random
import math

from pygame import mixer

# CRTL + ALT + L will give you good formatting
# TO commit to github: Right click venv -> Git -> Commit Directory -> Crtl + Shift + K

pygame.init()

# create the screen of 800x600
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Background image
Background = pygame.image.load('background.png')

#background Sound
mixer.music.load("background.wav")
mixer.music.play(-1)


# enemy
enemyimage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numenemies = 6

for i in range(numenemies):
    enemyimage.append(pygame.image.load('enemy.PNG'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1.75)
    enemyY_change.append(40)


def enemy(x, y, i):
    screen.blit(enemyimage[i], (x, y))


# player
playerimage = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerchange = 0

# ready state is when you cant see the bullet and fire state is when it is fired
# bullet
bulletimg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletchange = 3
bullet_state = "ready"

# score
#too add more fonts just dowload the file and add the .ttf file to folder

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

#Game Over Test
over_font = pygame.font.Font("freesansbold.ttf", 64)

def gameover():
    over_text = over_font.render("Game Over",True,(255,255,255))
    screen.blit(over_text,(203,250))
    isDone = False

def show_score(x, y, ):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerimage, (x, y))


def firebullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))  # this will make sure it fires from the center


def isCollison(enemyX, enemyY, bulletX, bullterY):
    dis = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if dis < 27:
        return True
    else:
        return False


# Game loop
isDone = True

while isDone:
    screen.fill((255, 255, 255))
    # background image
    screen.blit(Background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
        # if keystroke is pressed check wheater its right or left
        if event.type == pygame.KEYDOWN:  # keeps checking for any key pressed
            if event.key == pygame.K_LEFT:  # if left key is pressed if statment is excecuted
                if playerX < 800 and playerX > 0:
                    playerchange = -5
            if event.key == pygame.K_RIGHT:
                playerchange = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    bulletX = playerX
                    firebullet(playerX, bulletY)
        if event.type == pygame.KEYUP:  # keyup is when you pick your finger up from that button
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerchange = 0

    playerX += playerchange

    # This prevents the space ship from going out of bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Makes the enemy move
    for i in range(numenemies):

        #Game over
        if enemyY[i] > 440:
            for j in range(numenemies):
                enemyY[i] = 2000
                gameover()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1.75
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1.75
            enemyY[i] += enemyY_change[i]

        collision = isCollison(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet moves
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        firebullet(bulletX, bulletY)
        bulletY -= bulletchange

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
