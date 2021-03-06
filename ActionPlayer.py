'''
Created on Feb 27, 2015

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

class ActionPlayer(Player):
    '''
    ActionPlayer is a top-down arena shooter player character
    It will move in simple up/down/left/right & diagonal patterns
    It will eventually shoot through vectors at the mouse 
    '''
    def __init__(self, x,y,width,height,vx,vy):
        Player.__init__(self,x,y,width,height,vx,vy)
        self.sprite = sprite_class("./sprites/spearGuy.png",832,1344,13,21)
        self.sprite.play(True)
        self.sprite.set_animation_delay(100)
        #self.sprite.set_animation_range(40,80)
        self.sprite.create_animation("walkUp", 105, 113, 100)
        self.sprite.create_animation("walkLeft", 118, 126, 100)
        self.sprite.create_animation("walkDown", 131, 139, 100)
        self.sprite.create_animation("walkRight", 144, 152, 100)
        self.sprite.create_animation("idle",130,130,500)
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
        
        
    
    #input hooks
    def inputUpInit(self):        
        self.sprite.load_animation("walkUp")        
    def inputUpKeyAction(self):        
        self.position.y -= self.velocity.y
        self.updateCollisionBox()    
    def inputUpKeyRelease(self):
        self.sprite.load_animation("idle")
    
    def inputDownInit(self):
        self.sprite.load_animation("walkDown")        
    def inputDownKeyAction(self):
        self.position.y += self.velocity.y
        self.updateCollisionBox()    
    def inputDownKeyRelease(self):
        self.sprite.load_animation("idle")

    def inputRightInit(self):
        self.sprite.load_animation("walkRight")
    def inputRightKeyAction(self):
        self.position.x += self.velocity.x
        self.updateCollisionBox()    
    def inputRightKeyRelease(self):
        self.sprite.load_animation("idle")
        
    def inputLeftInit(self):
        self.sprite.load_animation("walkLeft")
    def inputLeftKeyAction(self):        
        self.position.x -= self.velocity.x
        self.updateCollisionBox()    
    def inputLeftKeyRelease(self):
        self.sprite.load_animation("idle")
    
    def inputAction1(self):
        #print "actionplayer.actionkey1"
        self.calculateGunOrigin()
        
        self.equipedGun.update(self.gunOrigin,self.facing, True)
        self.equipedGun.shoot()
    #more to come
    
        #in our action game, we want to aim at the mouse
    #so we need the mouse location
    def calculateAimingVector(self):
        mousePos = Vector2(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
        midPoint = Vector2(self.position.x + self.dimensions.x/2, 
                           self.position.y + self.dimensions.y/2)
        
        vector = Vector2(mousePos.x - midPoint.x, mousePos.y - midPoint.y)
        if(vector.x != 0 or vector.y != 0):
            size = math.sqrt(vector.x**2 + vector.y**2)
            self.facing.x = vector.x/size
            self.facing.y = vector.y/size
            
    def calculateGunOrigin(self):
        self.calculateAimingVector() #update aiming vector
        midPoint = Vector2(self.position.x + self.dimensions.x/2, 
                           self.position.y + self.dimensions.y/2)
        self.gunOrigin.x = midPoint.x + (self.facing.x * 75)
        self.gunOrigin.y = midPoint.y + (self.facing.y * 75)
    
    
    def handleBoundHit(self, direction):
        #options:
        # - set up a flag preventing movement - basically turning off velocity in a direction
        # - set up a velocity backup variable and set velocity to 0?
        # - back the player up one velocity step
        if(direction[0] == -1):
            self.position.x += self.velocity.x
        elif(direction[0] == 1):
            self.position.x -= self.velocity.x
            
        if(direction[1] == -1):
            self.position.y += self.velocity.y
        elif(direction[1] == 1):
            self.position.y -= self.velocity.y
            
        self.updateCollisionBox()
    
    def drawIt(self,drawTarget):
        #using primitives for now ... sprites later
        #pygame.draw.rect(drawTarget,self.color,self.toRect())
        #self.collisionBox.debugDraw(drawTarget)
        self.sprite.draw(drawTarget, self.position.x, self.position.y)
        
    
    def update(self, drawTarget, lowBound, upBound):
        #is our collisionmanger handling bound hits? ... should it?
        #print "Entered ActionPlayerUpdate"
        self.handleBoundHit(self.collisionBox.checkBoundHit(lowBound, upBound)) #derp ... 
        self.drawIt(drawTarget)
        
    