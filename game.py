import pygame
import aliens as aln

class Wall(pygame.sprite.Sprite):
    """Create a wall used for collision detection"""

    def __init__(self,height,width,pos,color) -> None:
        '''
         Param height: int representing how tall the wall is
        :Param width: int, representing how wide the wall is
        :Param pos: tuple, representing the x,y coordinates of the wall
        :Param color: tuple,representing the rgb value of the color being represented'''
        super().__init__()
        self.surface = pygame.Surface((width,height))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.x,self.rect.y = pos