import pygame
from objects import *
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
#background
background = pygame.image.load('images/background.jpg')
#characters
#player
me = character('images/student.png', screen)
#wall
wall = obstacle('images/wall.png', screen)
#monster
dragon = enemy('images/dragon.png', screen)
#bullet
bullet = projectile('images/bullet.png', screen)

running = True
while running:
    screen.blit(background, (0,0))
    #exit program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #controls
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            me.updateVx(-5)
        if event.key == pygame.K_RIGHT:
            me.updateVx(5)
        if event.key == pygame.K_UP:
            me.updateVy(-(me.Vy+20))
            me.updatey()
        if event.key == pygame.K_SPACE:
            if bullet.ready == True:
                bullet.fire(me.x, me.y)
    #wall mechanic
    if wall.x < -64:
        wall.restart()

    if wallcollision(me.x, me.y, wall.x, wall.gapy):
        pass
        # gameover screen
    #dragon mechanic
    if dragon.x < -32:
        dragon.restart()

    if isCollision(me.x, me.y, dragon.x, dragon.y):
        print("game over")
        # gameover screen
    #bullet mechanic
    if not bullet.ready:
        bullet.updatex()
        bullet.updatey()
        bullet.show()
        if isCollision(bullet.x, bullet.y, dragon.x, dragon.y):
            dragon.restart()
            bullet.ready = True
        elif bullet.x > 800:
            bullet.ready = True
        else: 
            bullet.ready = False
    else:
        bullet.x = -32
        bullet.y = -32




    #ground
    if me.y < 568:
        me.updatey()
    #player
    me.updatex()
    me.show()
    #wall
    wall.updatex()
    wall.show()
    #dragon
    # dragon.updatex()
    # dragon.show()

    #bullet test
    
    
    

    pygame.display.update()

