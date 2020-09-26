# This is the main Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""
Imports
"""
import os, sys
import pygame
import colors as c
import random
from Items.Equipment.Weapons.Sword.wooden_sword import WoodenSword
from Entity.Player import Player
from Entity.Enemy.Sprite import Sprite
from Sequences import Battle
import numpy as np
from Map import Map
import Utils


"""
Sandbox
"""
# newSword = WoodenSword
# newSword.name(newSword)
# print(f'{newSword.attack(newSword)} damage!')

# rand = np.random.uniform(0.5, 2.5)
# print(rand)
# print(np.round(rand))

# player = Player()
# player.setName('Miles')
#
# sprite = Sprite()
#
# newBattle = Battle((player, sprite))
#
# print(f"{player.name}'s HP = {player.hp}")

# newMap = Map()
# i = 0
# while i <= 5:
#     move = input('> ')
#     newMap.update(move)
#     i += 1

# print(random.randint(0, 1))


"""
Start main
"""
# Initialize pygame
pygame.init()

# Set clock object
clock = pygame.time.Clock()

# Set screen settings
width = 1200
height = 850
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Ultimate Dungeon Master')
background = pygame.image.load('dungeon3.jpg')
bSize = background.get_size()
screen.blit(background, ((width - bSize[0]) / 2, 0))  # Screen update


"""
textObjects()
Creates textual objects for other pygame methods to use
"""
def textObjects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


"""
button()
Mimics an interactive button and performs a given action based on mouse proximity and click status
"""
def button(msg, x, y, w, h, inactiveColor, activeColor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, activeColor, (x, y, w, h))

        if click[0] == 1 and action is not None:
            print('CLICKED')
            action()
    else:
        pygame.draw.rect(screen, inactiveColor, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = textObjects(msg, smallText, c.white)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)


"""
dispImage()
Displays an image to the current pygame display
"""
def dispImage(image, x, y):
    screen.blit(image, (x, y))  # Draw an image on an object (surface, display, etc.)


"""
findDist()
Finds euclidean distance between two objects
"""
def findDist(obj1, obj2):
    pass
    """
    pos1 = obj1.getPos()
    pos2 = obj2.getPos()
    return np.getEuclideanDistance(pos1, pos2) ????
    """


"""
findNearestEnemy()
Finds the nearest enemy to the given player
"""
def findNearestEnemy(player):
    pass
    """
    registry = getRegistry()
    dist = []
    i = 0
    for e in registry:  # Is there a better way to search than a for loop???
        dist[0] = findDist(player, e)
        i += 1
    return np.max(dist)  # Will this work??
    """


"""
isInDmgRange()
Determines if the two given objects are within a range in which they can damage eachother
"""
def isInDmgRange(obj1, obj2):
    pass
    """
    threshold = 2
    findDist(obj1, obj2)
    if dist <= threshold:
        return True
    return False
    """


"""
isInSightRange()
Determines if the given enemy can see the given object
"""
def isInSightRange(enemy, obj):
    pass
    """
    dist = findDist(enemy, obj)
    if dist <= enemy.sightRange:
        return Ture
    return False
    """


"""
>>> Game Loop <<<
startGame()
"""
def startGame():
    # Initialization
    player = Player()
    player.setName('Miles')
    playerImg = pygame.image.load('male_back_still.png')
    spriteImg = pygame.image.load('sprite.jpg')
    x = 0
    y = 0
    dx = 0
    dy = 0

    while True:
        # Doesn't work...
        # key = pygame.key.get_pressed()
        # if key[pygame.K_w]:
        #     print('w')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Why is this needed?
                quit()

            try:  # This try-catch is here for the unicode buttonPress implementation only
                dx, dy = Utils.buttonPress(event, player)

                if event.type == pygame.KEYUP:
                    # if event.key == pygame.K_w or event.key == pygame.K_a or event.key == pygame.K_s or event.key == pygame.K_d:
                    dx = 0
                    dy = 0

            except AttributeError:
                dx = 0
                dy = 0

        x += dx
        y += dy

        # Update screen
        screen.blit(background, ((width - bSize[0]) / 2, 0))

        # Update player
        dispImage(playerImg, x, y)
        dispImage(spriteImg, 100, 100)

        # Update display
        pygame.display.update()
        clock.tick(60)  # Gates the fps to a maximum of 60

"""
intro()
Game intro sequence
"""
def intro(screenWidth):
    # Set game title
    titleFont = pygame.font.Font('freesansbold.ttf', 45)
    textSurf, textRect = textObjects('Ultimate Dungeon Master', titleFont, c.white)
    textRect.center = (width / 2, height / 6)
    screen.blit(textSurf, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Why is this needed?
                quit()

        # Setup buttons
        sw = screenWidth
        w = 120
        button('Play', (sw - w) / 2, 400, w, 50, c.dullgreen, c.brightgreen, startGame)
        w = 100
        button('Exit', (sw - w) / 2, 470, w, 30, c.gray, c.brightgray, quit)
        button('Credits', (sw - w) / 2, 520, w, 30, c.gray, c.brightgray)

        pygame.display.update()


intro(width)