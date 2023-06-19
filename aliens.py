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
        self.image,self.rect = load_image(image,0.2)
        
    

    def update(self,right=True):
        """Purpose: move the sprite left of right
        :param right: boolean indicating if the sprite is moving right of not"""
        if right:
            self.rect.x +=1
        else:
            self.rect.x -=1


class Squid_Alien(Alien):
    def __init__(self, image):
        super().__init__(image)
        self.score = 10


class Minion_Alien(Alien):
    def __init__(self, image):
        super().__init__(image)
        self.score = 10



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
    


class bullet(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image,self.rect = load_image("bullet.png")
        self.rect.x,self.rect.y = x,y
    
    def update(self):
        self.rect.y +=1
        