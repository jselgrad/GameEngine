import pygame
#@staticmethod
def gameprint(screen,text,xx,yy,color):
    font = pygame.font.SysFont("Courier New",18)
    ren = font.render(text,1,color)
    screen.blit(ren, (xx,yy))