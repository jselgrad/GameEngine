'''
Created on Feb 23, 2015

@author: SIU853541579
'''
import pygame
from Vector2 import *
from Colors import *



class Entity():
    '''
    Entity is going to be the base class for pretty much everything that moves on a game screen
    
    It's going contain all sort of prototypes for our other entities to override
    Abstract Base Class
    '''

    '''
    Constructor ...
    Needs everything that will common to all of our game entities    
    '''
    def __init__(self, x,y,width,height, vx, vy ):
        self.position = Vector2(x,y) #might change this back to x & y as separate
        self.dimensions = Vector2(width, height)
        
        self.velocity = Vector2(vx,vy)        
        self.facing = Vector2(1,0) #this is an actual vector ... more on this later
        
        self.isAlive = True
        self.hitPoints = 1 #this will be changed by the particular entity
        self.damage = 1 #this will also be changed by the particular entity
        
        self.colBoxAnchorOffset = Vector2(0,0)
        self.collisionBox = 0 #null for now, collisionBoxes are built by the entities
        #NOTE: remember to do the ID's ... 
        
        self.color = Color.red
        
    def updateCollisionBox(self):
        self.collisionBox.update(self.position.x + self.colBoxAnchorOffset.x, 
                                 self.position.y + self.colBoxAnchorOffset.y)
    
    def toRect(self):
        return (self.position.x, self.position.y, self.dimensions.x, self.dimensions.y)
    '''
    onHit
    will be called on by the collision manager
    It will need information
    '''
    def onHit(self, other, direction):
        pass
    
    def debugDraw(self, target):
        pygame.draw.rect(target, self.color,self.toRect())
        
       
    