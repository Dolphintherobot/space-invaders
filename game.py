import pygame
import aliens as aln
import random as rn

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

class text(object):
    """Purpose:create a text object that can be blitted on screen """
    def __init__(self,text,size,color = (0, 128, 0),) -> None:
        """
        Param text: string representing the text you want on screen
        Param size: tuple (height,width) representing size of text
        Param color: tuple representing rgb value of the color of the text """
        self.size = size
        self.color = color
        self.text = self.create_text(text,size,color)
    
    def create_text(self,text,size,color):
        ''''Purpose: to generate text that can be drawn onto screen
        Param text: string representing the text you want on screen
        Param size: tuple (height,width) representing size of text
        Param color: tuple representing rgb value of the color of the text
        Return font: Surface object that represents the font'''
        font_type = pygame.font.get_default_font()
        font = pygame.font.Font(font_type)
        font = font.render(text,True,color)
        font = pygame.transform.smoothscale(font,size)
        return font
    
    def draw(self,screen,pos):
        """Purpose: draw text on screen
        Param screen: surface wanting to blit onto
        Param pos: x,y tuple of where the text should be drawn onto"""
        
        screen.blit(self.text,pos)
    
    def update_text(self,new_text):
        '''Purpose:change the text that the text object is displaying
        Param text: string representing the new text'''
        self.text = self.create_text(new_text,self.size,self.color)

    
    
    

class Space_invaders:

    def __init__(self) -> None:
        '''Initialize a game of space invaders'''
        self.setup_game()
    


    def setup_game(self):
        """Purpose:to create the data being modified during the game"""
        size = (1000,1000)
        self.screen_color = (0,0,0)
        self.screen = pygame.display.set_mode(size)
        self.score = 0
        self.lives = 3
        self.aliens = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.player = aln.Player("player (1).png")
        self.all_sprites = pygame.sprite.Group()
    
    def create_walls(self):
        '''Purpose:create walls for collision detection'''
        top_wall = Wall(1,1000,(0,-1),self.screen_color)
        left_wall = Wall(1000,1,(-1,0),self.screen_color)
        right_wall = Wall(1000,1,(1001,0),self.screen_color)
        self.walls.add(top_wall,left_wall,right_wall)
        

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
            size_alien = aln.Alien("enemy1.png")
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

        squid = aln.Squid_Alien("enemy3.png")
        squid.set(x,y)
        space = margin +squid.image.get_size()[1]
        y+=space
        self.aliens.add(squid)
       

        for n in range(2):
            frog_alien = aln.Minion_Alien("enemy2.png")
            frog_alien.set(x,y)
            y+=space
            self.aliens.add(frog_alien)
            

        for n in range(2):
            grumpy_alien = aln.Minion_Alien("enemy1.png")
            grumpy_alien.set(x,y)
            y+=space
            self.aliens.add(grumpy_alien)
            
        
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

    def move_player(self):
        '''Purpose:check to see if a key is being held down so the player can move
        :Return:None
        '''
        keys = pygame.key.get_pressed()  
        if keys[pygame.K_LEFT]:
            self.player.move_left()

        if keys[pygame.K_RIGHT]:
            self.player.move_right()

    def alien_shoot(self):
        '''Purpose: to simulate the firing of the aliens
        :Note: only the squid aliens are allowed to fire and has a 1/50 chance of not firing'''
        is_firing = rn.choice([False for i in range(49)] + [True])

        if is_firing:
            alien = rn.choice(self.aliens.sprites())
            bullet = alien.shoot()
            if isinstance(bullet,aln.bullet):
                self.bullets.add(bullet)
                self.all_sprites.add(bullet)
    
    def update_screen_text(self,score:text,lives:text) -> None:
        '''Purpose:to draw and update text on screen
        param score: text object representing the score
        param lives: text object representing the lives
        note: will change what is being written on text if conditions are meet
        '''
        score.update_text(f"score:{self.score}")
        score.draw(self.screen,(900,650))
        lives.update_text(f"lives:{self.lives}")
        lives.draw(self.screen,(800,650))

    def update_screen(self):
        """Purpose: update objects on screen
        Return: None"""

        self.screen.fill(self.screen_color)
        self.all_sprites.draw(self.screen)
        self.aliens.draw(self.screen)
        self.all_sprites.update()


    def start(self):
        """Purpose:to display the start screen
        """
        self.screen.fill(self.screen_color)
        game_text = text("Space invaders",(400,100))
        play_text = text("Press s to start",(300,100))
        game_text.draw(self.screen,(313,28))
        play_text.draw(self.screen,(350,330))
        pygame.display.flip()

    def game_over(self):
        """Purpose:displays the game over screen and re-runs the game if neccesary
        """
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        print("hallo")
                        self.setup_game()
                        self.play()
                if event.type == pygame.QUIT:
                    done = True
                    continue
            self.screen.fill(self.screen_color)
            game_over_text = text("Game over",(400,100))
            play_again_text = text("Press s to restart",(300,100))
            game_over_text.draw(self.screen,(313,28))
            play_again_text.draw(self.screen,(350,330))
            pygame.display.flip()

    pygame.quit()



    def hit_checker(self,player_bullets:pygame.sprite.Group,bullet:aln.bullet):
        """Purpose:check for collisions between sprites and bullets
        :Param player_bullets: sprite group of the players bullets
        :Param bullet: bullet object
        :Note: will remove sprites from groups if collision is detected"""
        if len(player_bullets) > 0:
            collision = pygame.sprite.spritecollide(bullet,self.aliens,True)  

            if len(collision) > 0:
                bullet.kill()
                for alien in collision:
                    self.score += alien.score


        if len(self.bullets) > 0:
            collision = pygame.sprite.spritecollide(self.player,self.bullets,True) 
            if len(collision) > 0:
                self.lives -=1 

    
    def alien_rengenerator(self):
        '''Purpose to create more aliens once the player has killed them all
        :Note: will update self.aliens and self.bullets '''
        if len(self.aliens.sprites()) == 0:
            self.create_aliens()
            self.bullets.clear(self.screen,self.screen_color)
            self.bullets.empty()
            self.lives +=1



    def play(self):
        """Purpose:to play the game"""
        pygame.init()
        clock = pygame.time.Clock()
        self.create_aliens()
        self.create_walls()
        self.setup_player()
        player_bullets = pygame.sprite.Group()
    
        done = False
        move_right = True
        is_started = False
        bullet = None

        score_text = text(f"score:{self.score}",(50,25))
        lives_text = text(f"score:{self.lives}",(50,25))

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s and not is_started:
                        is_started = True
                    if event.key == pygame.K_SPACE and is_started:
                        if len(player_bullets) > 0:
                            continue
                        bullet = self.player.shoot()
                        player_bullets.add(bullet)
                        self.all_sprites.add(bullet)


            #check if game is being played
            if not is_started:
                self.start()
                continue
            
            if self.lives < 1:
                self.game_over()
                continue
                 
            self.move_player()
            self.alien_shoot()
            self.alien_rengenerator()

            #checking for sprite collisions

            if self.collision_checker(self.walls,self.aliens):
                move_right = not move_right
                self.aliens.update(move_right,True)
           
            self.hit_checker(player_bullets,bullet)
            

            #draw and update images on screen
            self.update_screen()
            self.aliens.update(move_right)
            player_bullets.update()
            self.update_screen_text(score_text,lives_text)
            
            pygame.display.flip()
            clock.tick(60)
            
        pygame.quit()


sv = Space_invaders()
sv.play()