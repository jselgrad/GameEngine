'''
Created on Feb 20, 2015

@author: SIU853541579
'''
from CollisionBox import *

class CollisionManager():
    '''
    CollisionManger
    This class will provide factories for building collision boxes
    It will also maintain all collisions in our game
    The entities will not run collisions, the manager will
    When a collision happens, the entity will be informed of the who/how 
        and be told to deal with it /sunglasses
        
    The collision manager will contain a list of all collisionBoxes in the game
    The collision manager should use a lot of static functions so we don't have to have an object for it
    
    '''
    
    #collision list
    collisionList = []
    
    @staticmethod
    def buildCollisionBox(x,y,width,height,owner):
        temp = CollisionBox(x,y,width,height, owner)
        CollisionManager.collisionList.append(temp)
        return temp
    
    @staticmethod
    def test():
        print CollisionManager.collisionList;
    
    def __init__(self):
        '''
        Constructor
        '''
        