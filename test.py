import pygame
import os


import aliens as aln










# pygame.draw.rect(screen,
#                  color,
#                  [(margin + width) * column + margin,
#                   (margin + height) * row + margin,
#                   width,
#                   height])       






def movement_Test():
    '''
    Purpose:check to see that if everything is working and interacting with each other correctly
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
    player_bullets = pygame.sprite.Group() 
    

    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_SPACE:
                    if len(player_bullets) > 0:
                        continue
                    bullet = player.shoot()
                    player_bullets.add(bullet)
                    all_sprites.add(bullet)


        if len(player_bullets) > 0:
            collision = pygame.sprite.spritecollide(bullet,alien_group,True)  

            if len(collision) > 0:
                bullet.kill()
        player_bullets.update()
        screen.fill(BLACK)
        alien_group.update()
        all_sprites.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)
 

    pygame.quit()



movement_Test()