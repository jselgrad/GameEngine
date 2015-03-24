'''
Created on Feb 23, 2015

@author: SIU853541579
'''

class Vector2():

    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
    def __add__(self,other):
        temp = Vector2(0,0)
        temp.x = self.x + other.x
        temp.y = self.y + other.y
        return temp
    
    
        