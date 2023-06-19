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