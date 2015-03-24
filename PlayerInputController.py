'''
Created on Feb 25, 2015

@author: SIU853541579
'''
from Player import *

class PlayerInputController():
    '''
    This class is an inbetween for handling and calling input events in a player
    This class allows us to easily change key bindings
    '''

    #constructor sets up initial bindings for keys
    def __init__(self, up, down, left, right, act1, player):
        self.upKey = up
        self.downKey = down
        self.leftKey = left
        self.rightKey = right
        self.actionKey1 = act1
        
        self.owningPlayer = player
        
        self.upPrevInput = False
        self.downPrevInput = False
        self.rightPrevInput = False
        self.leftPrevInput = False
        self.actionKey1PrevInput = False
    

    def ProcessUpKey(self, keyboard):
        if (keyboard[self.upKey] == True):
            if (self.upPrevInput == False):
                self.owningPlayer.inputUpInit()
                self.upPrevInput = True
            self.owningPlayer.inputUpKeyAction()
        elif (self.upPrevInput == True):
            self.owningPlayer.inputUpKeyRelease()
            self.upPrevInput = False
            
    def ProcessDownKey(self, keyboard):
        if (keyboard[self.downKey] == True):
            if (self.downPrevInput == False):
                self.owningPlayer.inputDownInit()
                self.downPrevInput = True
            self.owningPlayer.inputDownKeyAction()
        elif (self.downPrevInput == True):
            self.owningPlayer.inputDownKeyRelease()
            self.downPrevInput = False
    
    def ProcessRightKey(self, keyboard):
        if (keyboard[self.rightKey] == True):
            if (self.rightPrevInput == False):
                self.owningPlayer.inputRightInit()
                self.rightPrevInput = True
            self.owningPlayer.inputRightKeyAction()
        elif (self.rightPrevInput == True):
            self.owningPlayer.inputRightKeyRelease()
            self.rightPrevInput = False
    
    def ProcessLeftKey(self, keyboard):
        if (keyboard[self.leftKey] == True):
            if (self.leftPrevInput == False):
                self.owningPlayer.inputLeftInit()
                self.leftPrevInput = True
            self.owningPlayer.inputLeftKeyAction()
        elif (self.leftPrevInput == True):
            self.owningPlayer.inputLeftKeyRelease()
            self.leftPrevInput = False
            
    def update(self, keyboard):
        self.ProcessUpKey(keyboard)
            
        self.ProcessDownKey(keyboard)
        
        self.ProcessRightKey(keyboard)
        
        self.ProcessLeftKey(keyboard)
        
        if(keyboard[self.actionKey1] == True):
            self.owningPlayer.inputAction1()
        #else:
            #self.owningPlayer.releaseAction1()
            
            
            
            
        