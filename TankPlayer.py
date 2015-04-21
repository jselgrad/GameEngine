'''
Created on Apr 21, 2015

@author: SIU853541579
'''
import pygame
import math
from Player import *
from Vector2 import *
from CollisionManager import *
from Colors import *
from MachineGun import *
from sprite_class import *

class TankPlayer(Player):
    '''
    classdocs
    '''

    def __init__(self, x,y,width,height,vx,vy):
        Player.__init__(self,x,y,width,height,vx,vy)
        self.sprite = sprite_class("./sprites/tank.bmp",526,64,8,1)
        self.sprite.play(True)
        self.sprite.set_animation_delay(100)
                self.sprite.set_animation_frame(1)
        self.sprite.set_image_color_key(255, 0, 255)
        self.sprite.scale_sprite(1)
        self.dimensions.x = self.sprite.get_width()
        self.dimensions.y = self.sprite.get_height()
        self.colBoxAnchorOffset = Vector2(0,0) #since we have no art, this can be 0,0
        self.collisionBox = CollisionManager.buildCollisionBox(self.position.x + self.colBoxAnchorOffset.x,
                                                              self.position.y + self.colBoxAnchorOffset.y,
                                                              self.dimensions.x,self.dimensions.y,
                                                              self)
        self.equipedGun = MachineGun(Vector2(self.position.x + self.dimensions.x/2,
                                             self.position.y + self.dimensions.y/2),
                                     Vector2(1,1))
        self.facing = Vector2(0,0)
        self.gunOrigin = Vector2(0,0)
        self.color = Color.cyan
        
        