'''
Created on Mar 6, 2015

@author: SIU853541579
'''
from baseBullet import *
class BulletManager():
    '''
    This is going to be a manager and factory class for bullets
    '''

    bulletList = []
    
    @staticmethod
    def buildBaseBullet(spawnX, spawnY, aimX, aimY, speed):
        print "BulletManager.buildBaseBullet"
        temp = BaseBullet(spawnX, spawnY, aimX, aimY, speed)
        BulletManager.bulletList.append(temp)
        return temp
    
    @staticmethod
    def update(screen, lowBound, upBound):
        for bullet in BulletManager.bulletList:
            bullet.update(screen, lowBound, upBound)
    
    def __init__(self, params):
        '''
        Constructor
        '''
        