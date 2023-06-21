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

    
        
def create_aliens(self):
        pass
    
def create_alien_helper(self,x,y):
    '''Purpose: to create a 1x5 column of aliens
    :param x: int,representing x coordinate on the screen
    :param y: int,representing y coordinate on the screen'''
    
    margin = 15

    squid = aln.Squid_Alien("green_squid.png")
    squid.set(x,y)
    space = margin +squid.image.get_size()[1]
    y+=space
    self.aliens.add(squid)

    for n in range(2):
        frog_alien = aln.Minion_Alien("frog_alien.png")
        frog_alien.set(x,y)
        y+=space
        self.aliens.add(frog_alien)

    for n in range(2):
        grumpy_alien = aln.Minion_Alien("grumpy_alien.png")
        grumpy_alien.set(x,y)
        y+=space
        self.aliens.add(grumpy_alien)

            

