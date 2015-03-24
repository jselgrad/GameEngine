'''
Created on Feb 25, 2015

@author: SIU853541579
'''
from ActionPlayer import *
from PlayerInputController import *

class PlayerInputManager(object):
    '''
    classdocs 
    '''
    inputList = []
    
    #buildActionPlayer - acts as a player factory
    @staticmethod
    def buildActionPlayer( upKey, downKey, leftKey, rightKey,
                           action1Key, 
                           xPos, yPos,
                           width, height,
                           vx, vy):
        player = ActionPlayer(xPos, yPos, width, height, vx, vy)
        input = PlayerInputController(upKey, downKey, leftKey, rightKey,
                                      action1Key, player)
        PlayerInputManager.inputList.append(input)
        return player
        
    @staticmethod
    def update(keyboard):
        for input in PlayerInputManager.inputList:
            input.update(keyboard)
    
    def __init__(self, params):
        '''
        Constructor
        '''
        