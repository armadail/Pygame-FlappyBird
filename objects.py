import pygame
import math
import random

class character:
    # position of object
    x = 50
    y = 0
    # velocity of object
    Vx = 0
    Vy = 0
    # external forces
    Ag = 5
    t = 0.25
    #double jump
    energy = 20
    

    def __init__(self, image, mainscreen):
        self.characterImg = pygame.image.load(image)
        self.screen = mainscreen

        
    def show(self):
        self.screen.blit(self.characterImg, (self.x, self.y))

    #update the velocity
    
    def updateVy(self,Vy):
        #Vf = Vi + Ag*t + Velocity_from_controls
        self.Vy = self.Vy +self.Ag*self.t + Vy

    def updateVx(self,Vx):
        #Vf = Vi + u*Ag*t 
        if self.Vx > 0:
            self.Vx = self.Vx - self.Ag*self.t
        elif self.Vx < 0:
            self.Vx = self.Vx + self.Ag*self.t
        else:
            pass
        if self.Vx > 10:
            self.Vx = self.Vx
        else:
            self.Vx = self.Vx + Vx



    def updatey(self):

        self.updateVy(0)
        # Xf = Xi + V*t + 0.5*Ag*t^2
        self.y = self.y + self.Vy*self.t 
    
    def updatex(self):
        self.updateVx(0)
        self.x = self.x + self.Vx*self.t
    
class projectile:
    # position of object
    x = 50
    y = 0
    # velocity of object
    Vx = 50
    Vy = 0
    # external forces
    Ag = 5
    t = 0.25
    #bullet state: Ready = True: bullet is off screen | Ready = False: bullet is on the air
    ready = True
    def __init__(self, image, mainscreen):
        self.characterImg = pygame.image.load(image)
        self.screen = mainscreen

    def show(self):
        self.screen.blit(self.characterImg, (self.x, self.y))
    
    def fire(self, playerx, playery):
        self.x = playerx
        self.y = playery
        self.ready = False


    def updateVy(self):
        #Vf = Vi + Ag*t 
        self.Vy = self.Vy +self.Ag*self.t 

    def updatey(self):
        self.updateVy()
        # Xf = Xi + V*t + 0.5*Ag*t^2
        self.y = self.y + self.Vy*self.t 
    
    def updatex(self):
        self.x = self.x + self.Vx*self.t


class obstacle:
    x = 736
    y = 0
    speed = 3
    #gapy is a number from 0 to 8, multipy the value by 64 to find the corresponding screen position
    gapy = 0

    def __init__(self, image, mainscreen):
        self.characterImg = pygame.image.load(image)
        self.screen = mainscreen
        self.restart()


        
    def show(self):
        for i in range (10):
            if (i == self.gapy) or (i == self.gapy + 1):
                continue
            else:
                self.screen.blit(self.characterImg, (self.x, 0 + i*64))
    
    def updatex(self):
        self.x = self.x - self.speed

    def restart(self):
        self.x = 800
        self.gapy = random.randint(0, 8)
        self.speed += 0.2


class enemy:
    x = 736
    y = 0
    speed = 3

    def __init__(self, image, mainscreen):
        self.characterImg = pygame.image.load(image)
        self.screen = mainscreen
        self.restart()


    def show(self):
        self.screen.blit(self.characterImg, (self.x, self.y))
    
    def updatex(self):
        self.x = self.x - self.speed

    def restart(self):
        self.x = 800
        self.y = random.randint(0, 568)
        self.speed += 1


        
    

def wallcollision(playerx, playery, gapx, gapy):
    #threshold = sqrt(32^2 + 64^2) distance from closest wall point to gap midpoint
    threshold = 72
    # the blitz function display an image such that the top right corner of an image is at x,y
    pmidx = playerx + 16
    pmidy = playery + 16

    gmidx = gapx + 32
    gmidy = gapy*64 + 64

    distance = math.sqrt(math.pow(pmidx-gmidx, 2) + math.pow(pmidy-gmidy, 2))
    if (playerx > gapx) & (playerx <gapx+32):
        if distance > threshold:
            return True
        else:
            return False
    else:
        return False

def isCollision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))
    if distance < 27:
        return True
    else:
        return False    