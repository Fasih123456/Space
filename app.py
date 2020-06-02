import pygame
import random

#CRTL + ALT + L will give you good formatting

pygame.init()

# create the screen of 800x600
screen = pygame.display.set_mode((800, 600))
screen = pygame.display.set_mode((800, 600))
# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# enemy
enemyimage = pygame.image.load('enemy.PNG')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemychange = 0


def enemy(x, y):
    screen.blit(enemyimage, (x, y))


# player
playerimage = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerchange = 0


def player(x, y):
    screen.blit(playerimage, (x, y))


# Game loop
isDone = True;

while isDone:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
        # if keystroke is pressed check wheater its right or left
        if event.type == pygame.KEYDOWN:  # keeps checking for any key pressed
            if event.key == pygame.K_LEFT:  # if left key is pressed if statment is excecuted
                if playerX < 800 and playerX > 0:
                    playerchange = -0.3
            if event.key == pygame.K_RIGHT:
                playerchange = 0.3
        if event.type == pygame.KEYUP:  # keyup is when you pick your finger up from that button
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerchange = 0

    playerX += playerchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()
