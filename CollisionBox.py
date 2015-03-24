'''
Created on Feb 20, 2015

@author: SIU853541579
'''
import pygame

class CollisionBox():
    '''
    CollisionBox class
    This is a stand-alone collision box that is going to be separate from our entities
    This will handle all of the collision checks, but not reactions.  Reacting to collisions
    belongs in the purview of the entity it is assigned to
    
    This class will have a "has a" relationship to entities
    '''
    def __init__(self, x, y, width, height, owner):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.owner = owner
        self.isAlive = True #this is an active collisionBox
        #debugging information
        self.color = (255,0,0) #incase we want to draw it on the screen for debuggin
    
    ''' 
    we need:
        - check bound hits
        - return information about a bound hit
        - check a collision with another box
        - determine direction of collision
        - return information about it
    '''
    '''
    checkBoundHit
    checks a hit on defined bounds
    parameters: lowerbound, 2-tupple that defines the lower bound
                upperbound, 2-tupple that defines the upper bound
    returns: 2-array defining how the hit occured, [0,0] meaning no hit ...
    NOTE: might separate this behavior later
    '''
    def checkBoundHit(self, lowerBound, upperBound):
        #print "entered collisionbox.checkboundHit"
        result = [0,0]
        if(self.x <= lowerBound[0]):
            result[0] = -1
        elif(self.x+self.width >= upperBound[0]):
            result[0] = 1
        
        if(self.y <= lowerBound[1]):
            result[1] = -1
        elif(self.y+self.height >= upperBound[1]):
            result[1] = 1
        
        return result
    
    #box collisions
    def checkBoxHit(self, other):
        #min1----------max1
        #    min2-------------max2
        if((self.x <= (other.x+other.width)) and (other.x <= (self.x + self.width))):
            if((self.y <= (other.y + other.height)) and (other.y <= (self.y + self.height))):
                return True
            else:
                return False
        else:
            return False
    
    
    #get hit direction
    def getHitDirection(self, other):
        result = [0,0]
        #self's perspective
        dTop = abs(self.y - (other.y + other.height))
        dBot = abs((self.y + self.height) - other.y)
        dLeft = abs(self.x - (other.x + other.width))
        dRight = abs((self.x + self.width) - other.x)
        
        if (dTop <= dRight) and (dTop <= dLeft) and (dTop < dBot):
            #top
            #check corner
            if(dTop == dRight):
                result[0] = 1
            elif(dTop == dLeft):
                result[0] = -1
                
            result[1] = -1
            
        elif(dBot <= dRight) and (dBot <= dLeft):
            #bot
            if(dBot == dRight):
                result[0] = 1
            elif(dBot == dLeft):
                result[0] = -1
            
            result[1] = 1
            
        elif(dRight < dLeft):
            #right
            result[0] = 1
        else:
            #left
            result[0] = -1
        
        return result
    
    def update(self,x,y):
        self.x = x
        self.y = y
    
    def debugDraw(self, target):
        pygame.draw.rect(target, self.color, (self.x, self.y, self.width, self.height), 2)
    