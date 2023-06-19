import pygame
import os


import aliens as aln










# pygame.draw.rect(screen,
#                  color,
#                  [(margin + width) * column + margin,
#                   (margin + height) * row + margin,
#                   width,
#                   height])       






def main():
    '''
    Purpose:program that runs the gui
    '''

    
    pygame.init()
    pygame.font.init()

    size = (1000, 1000)
    screen = pygame.display.set_mode(size)
    
    done = False
    clock = pygame.time.Clock()


    
    GREEN = (0,255,0)
    BLACK = (255,255,255)
    # background = pygame.Surface(screen.get_size())
    
    player = aln.Player("player.png")
    player.rect.y = 500
    alien1 = aln.Minion_Alien("purple_alien.png")
    alien2 = aln.Squid_Alien("green_squid.png")

    alien_group = pygame.sprite.Group()
    alien_group.add(alien1,alien2) 
    all_sprites = pygame.sprite.Group() 
    all_sprites.add(alien1,alien2,player)  
    

    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                
                if event.key == pygame.K_LEFT:
                    player.move_left()
            
        screen.fill(BLACK)
        # alien_group.update()
        all_sprites.draw(screen)
        

        
        
        pygame.display.flip()
        clock.tick(60)
 

    pygame.quit()



main()