import pygame
import os
import random as rn




main_dir = os.path.split(os.path.abspath(__file__))[0] 
image_dir = os.path.join(main_dir, "images") 


def load_image(name,scale=1):
    '''Purpose:to load an image 
    :param name: name of the image 
    :param scale:int representing size multiplier
    :note:must be in images directory in order to load
    :return:image a Suface object that represents the image
    :return:image.get_rect() a Rect object that represents image as Rect
    '''
    
    abs_path = os.path.join(image_dir,name)
    image = pygame.image.load(abs_path)
    size = image.get_size()
    size = (size[0]*scale,size[1]*scale)
    

    image = pygame.transform.scale(image,size)
    image = image.convert()
    return image,image.get_rect()



class Alien(pygame.sprite.Sprite):

    def __init__(self,image):
        super().__init__()
        self.image,self.rect = load_image(image)
        
    

    def update(self,right=True,down = False):
        """Purpose: move the sprite left of right
        :param right: boolean indicating if the sprite is moving right or not
        param down: boolean indicating if the sprite is moving down or not """
        if right:
            self.rect.x +=1
        else:
            self.rect.x -=1
        
        if down:
            self.rect.y +=5
    
    def shoot(self):
        """Purpose:to return a bullet object at the position of the shooter"""
        is_player = isinstance(self,Player)
        return bullet(self.rect.x,self.rect.y,is_player)
    
    def set(self,x,y):
        """Purpose: move the alien to an x,y coordinate
        Param x: int representing x coordinate
        Param y: int representing y coordinate
        :Note: Will not do anything once an alien has been moved"""
        if self.rect.x !=0 or self.rect.y != 0:
            return
        self.rect.x,self.rect.y = x,y

    
        



class Squid_Alien(Alien):
    def __init__(self, image):
        super().__init__(image)
        self.score = 30


class Minion_Alien(Alien):
    def __init__(self, image):
        super().__init__(image)
        self.score = 10

    def shoot(self):
        pass


class Player(Alien):
    def __init__(self, image):
        super().__init__(image)
        self.lives = 3

    
    def move_left(self):
        '''Purpose: move the player character to the left'''
        self.rect.x -=2
    
    def move_right(self):
        '''Purpose: move the player character to the right'''
        self.rect.x +=2
    
    def set(self):
        """Purpose:overide the set method being inherited, this class should not have that functionality"""
        pass
    
    def update(self):
        """Purpose:overide the update method being inherited, this class should not have that functionality"""
        pass

class bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,player = True) -> None:
        super().__init__()
        self.image = pygame.Surface((4,15))
        self.rect = self.image.get_rect()
        self.image.fill((0, 128, 0))
        self.rect.x,self.rect.y = x,y
        self.is_player = player
    
    def update(self):
        if self.is_player:
            self.rect.y -=1

            if self.rect.y < -10:
                self.kill()
        else:
            self.rect.y +=1

            if self.rect.y > 1010:
                self.kill()


