'''
Created on Mar 2, 2015

@author: SIU853541579
'''
from Vector2 import *
import pygame

class Gun():
    '''
    Gun for now is not going to be an entity... if your game would have a gun sprite, then
    that should change
    '''

    '''
        OK ...
        we're aiming for a gun that will shoot at the mouse 
        
        owner
        Vector for aiming
        coordinates
        bullet speed
         
        
    '''
    def __init__(self, mount, aimVector):
        self.origin = Vector2(mount.x, mount.y)
        self.aimVector = Vector2(aimVector.x, aimVector.y)
        self.canShoot = True
        self.keyUp = True
        self.previousInput = True
        
        self.bulletSpeed = 1
        self.isRapidFire = False
        self.timer = pygame.time.get_ticks() #get current time in miliseconds
        self.delay = 100 #delay between bullets
    
    
    def shoot(self):
        pass
    
    def generateBullets(self):
        pass
    
    def update(self,mount, aimVector, keyState):
        self.origin.x = mount.x
        self.origin.y = mount.y
        self.aimVector.x = aimVector.x
        self.aimVector.y = aimVector.y
        self.internalUpdate(keyState)
        self.previousInput = keyState
    
    def internalUpdate(self,keyState):
        self.canShoot = False
        #timers - the current time - the last time I captured it >= delay
        #print "gun.internal: ", pygame.time.get_ticks() - self.timer, "delay",self.delay
        if(pygame.time.get_ticks() - self.timer >= self.delay):
            self.canShoot = True #enough time has passed and I can shoot again
            
        #check if we're a rapid fire gun
        if(self.isRapidFire == False):
            #now we check for the keystate ... if the gun is not rapid fire, we don't want to keep shooting
            if((keyState == True) and (self.previousInput == True)):
                self.canShoot = False
    
        
    