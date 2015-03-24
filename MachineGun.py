'''
Created on Mar 6, 2015

@author: SIU853541579
'''
from Gun import *
from Vector2 import *
from BulletManager import *
import pygame

class MachineGun(Gun):
    '''
    classdocs
    '''
    def __init__(self, mount, aimVector):
        Gun.__init__(self, mount, aimVector)
        self.delay = 100
        self.bulletSpeed = 5
        self.timer = pygame.time.get_ticks()
        self.isRapidFire = True
        
    def shoot(self):
        print "machinegun.shoot", self.canShoot
        if self.canShoot:
            self.timer = pygame.time.get_ticks()
            self.generateBullets()
    
    def generateBullets(self):
        BulletManager.buildBaseBullet(self.origin.x, self.origin.y, 
                                      self.aimVector.x, self.aimVector.y, self.bulletSpeed)