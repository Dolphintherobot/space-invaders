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
        self.all_sprites = pygame.sprite.Group()
    
    def create_walls(self):
        '''Purpose:create walls for collision detection'''
        top_wall = Wall(1,1000,(0,-1),self.screen_color)
        left_wall = Wall(1000,1,(-1,0),self.screen_color)
        right_wall = Wall(1000,1,(1001,0),self.screen_color)
        self.walls.add(top_wall,left_wall,right_wall)
        # self.all_sprites.add(top_wall,left_wall,right_wall)

    def setup_player(self,x = 500,y = 500):
        '''Purpose:get player class staged'''
        self.player.rect.x = x
        self.player.rect.y = y
        self.all_sprites.add(self.player)
        
    def create_aliens(self):
            """Purpose:to create a 11x5 section of aliens
            """
            x = 0
            y = 0
            size_alien = aln.Alien("green_squid.png")
            size = size_alien.image.get_size()
            margin  = 15
            space = margin + size[0]
            for n in range(11):
                self.create_alien_helper(x,y)
                x+= space
        
    def create_alien_helper(self,x,y):
        '''Purpose: to create a 1x5 column of aliens
        :param x: int,representing x coordinate on the screen
        :param y: int,representing y coordinate on the screen
        :Note: will modfiy the aliens group class'''
        
        margin = 15

        squid = aln.Squid_Alien("green_squid.png")
        squid.set(x,y)
        space = margin +squid.image.get_size()[1]
        y+=space
        self.aliens.add(squid)
        # self.all_sprites.add(squid)

        for n in range(2):
            frog_alien = aln.Minion_Alien("frog_alien.png")
            frog_alien.set(x,y)
            y+=space
            self.aliens.add(frog_alien)
            # self.all_sprites.add(frog_alien)

        for n in range(2):
            grumpy_alien = aln.Minion_Alien("grumpy_alien.png")
            grumpy_alien.set(x,y)
            y+=space
            self.aliens.add(grumpy_alien)
            # self.all_sprites.add(grumpy_alien)
        
    def collision_checker(self,group,other):
        '''Purpose: check if any memeber of 2 groups of sprites have collided
        with each other
        :Param group:a sprite object
        :Param other:another sprite object
        :Return: True if collision is detected, False otherwise'''

        for sprite in group:
            a_list = pygame.sprite.spritecollide(sprite,other,False)
            if len(a_list) > 0:
                return True 
        return False



    def play(self):
        pygame.init()
        clock = pygame.time.Clock()
        self.create_aliens()
        self.create_walls()
        self.setup_player()
    
        done = False
        move_right = True
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                
                       
            keys = pygame.key.get_pressed()  
            if keys[pygame.K_LEFT]:
                self.player.move_left()
            if keys[pygame.K_RIGHT]:
                self.player.move_right()

            if self.collision_checker(self.walls,self.aliens):
                move_right = not move_right
           
            
            #draw and update images on screen

            self.screen.fill(self.screen_color)
            self.all_sprites.draw(self.screen)
            self.aliens.draw(self.screen)
            self.all_sprites.update()
            self.aliens.update(move_right)
            
            pygame.display.flip()
            clock.tick(60)
            
        pygame.quit()


sv = Space_invaders()
sv.play()