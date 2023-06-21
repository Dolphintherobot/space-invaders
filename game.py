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


class Space_invaders:

    def __init__(self) -> None:
        '''Initialize a game of space invaders'''
        size = (1000,1000)
        self.screen_color = (255,255,255)
        self.screen = pygame.display.set_mode(size)
        self.score = 0
        self.lives = 3
        self.aliens = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = aln.Player("player.png")
    
    def create_walls(self):
        '''Purpose:create walls for collision detection'''
        top_wall = Wall(1,1000,(0,0),self.screen_color)
        left_wall = Wall(1000,1,(0,0),self.screen_color)
        right_wall = Wall(1000,1,(1000,0),self.screen_color)
        self.walls.add(top_wall,left_wall,right_wall)

    
        

