import pygame
from pygame.constants import MOUSEBUTTONDOWN

from sandstorm import Tornado
pygame.init()
pygame.font.init()
import random
from variables import*
from object import Object, Rocher
from rover import Rover
from flag import Flag


class Game:
    def __init__(self, largeur, hauteur, title, background_path):
        self.clock = pygame.time.Clock()
        
        self.running = True
        self.largeur_ecran = largeur
        self.hauteur_ecran = hauteur
        self.screen = pygame.display.set_mode((self.largeur_ecran, self.hauteur_ecran))
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (self.largeur_ecran, self.hauteur_ecran))
        
        pygame.display.set_caption(title)
        
        self.rover = Rover(rover_path, 200, 200,80,64)
        self.flag = Flag(820, 500, 80,80)
        
        self.flag_group = pygame.sprite.Group()
        self.flag_group.add(self.flag)
        
        self.rover_group = pygame.sprite.Group()
        self.rover_group.add(self.rover)
        
        self.is_playing = True
        self.is_pausing = False
        self.did_win = False
        self.did_lose = False
        self.is_game_over = False
        self.calibri =  pygame.font.SysFont('Calibri', 70)
        
        
        self.victory_message = self.calibri.render('You win !', True, (0,0,0))
        self.victory_message_bas = self.calibri.render('Press r to continue', True, (0,0,0))
        self.losing_message = self.calibri.render('You lose !',True, (255,0,0))
        self.losing_message_bas = self.calibri.render('Press r to restart level', True, (255,0,0))
        
        self.keys_pressed  = {}
        self.current_level = 1
        self.affiche_niveau_rect = pygame.Rect(0,0, 250, 80)
        self.affiche_hitbox = False
        self.tornados_behaviours = ['vertical', 'horizontal']
        self.restart_level()
        
        
        
        
    def restart_level(self):
        self.rover = Rover(rover_path, 0, 200,80,64)
        self.flag = Flag(820, 500, 80,80)
        
        self.flag_group = pygame.sprite.Group()
        self.flag_group.add(self.flag)
        
        self.rover_group = pygame.sprite.Group()
        self.rover_group.add(self.rover)
        self.did_win = False
        self.did_lose = False
        
        self.rocks =pygame.sprite.Group()
        for x in range(3):
            rocher = Rocher(x*90, 80)
            self.rocks.add(rocher)   
        self.rocks.add(Rocher(250, 0))
        
        self.tornados = pygame.sprite.Group()
        nombre_tornades = int(0.7+0.5*self.current_level)
        
        if nombre_tornades >3:
            nombre_tornades = 3
        for a in range(nombre_tornades):
            x = random.randint(200, 900)
            y = random.randint(200, 900)
            
            if int(0.7*self.current_level+0.3) >3:
                return 0
            
            type = self.tornados_behaviours[random.randint(0,1)]
            tornado = Tornado(x,y,type, tornado_speed+self.current_level)
            self.tornados.add(tornado)
        
        
        
        for a in range(self.current_level):
            x = random.randint(200, 900)
            y = random.randint(100, 600) 
            self.rocks.add(Rocher(x,y))  
        
          
    

    def upper_stage(self):
        self.restart_level()
        for a in range(2):
            x = random.randint(200, 900)
            y = random.randint(100, 600) 
            self.rocks.add(Rocher(x,y))  
        self.current_level+=1
        
        
        
    def main(self):
        
        self.mouse_pos = pygame.mouse.get_pos()
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.keys_pressed[event.key] = True
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    self.running = False
                    
                    
                elif event.key == pygame.K_r:
                    if self.did_win:
                        self.upper_stage()
                    elif self.did_lose:
                        self.restart_level()
                elif event.key == pygame.K_h:
                    self.affiche_hitbox = not(self.affiche_hitbox)
                    
            elif event.type == pygame.KEYUP:
                self.keys_pressed[event.key] = False
                
            elif event.type == MOUSEBUTTONDOWN:
                print(self.mouse_pos)
                
        #self.did_win = 

        if pygame.display.get_active():
            
            
            
            
            
            
            
            
            
            self.screen.blit(self.background, (0,0))
            pygame.draw.rect(self.screen, (255,255,255),self.affiche_niveau_rect )
            
            for flag in self.flag_group:
                if self.affiche_hitbox:
                    flag.draw_hitbox(self.screen)
                flag.main(self.screen)
            
            
                
            
            for sprite in self.rover_group:
                if self.affiche_hitbox:
                    sprite.draw_hitbox(self.screen)

                if self.did_win or self.did_lose:
                    sprite.allowed_to_move = False
                else:
                    sprite.allowed_to_move = True
                
                sprite.main(self.screen)
                if sprite.detect_collision(self.flag_group):
                    self.did_win = True
                    
                if sprite.detect_collision(self.rocks) or sprite.detect_collision(self.tornados):
                    self.did_lose = True
            for rock in self.rocks:
                if self.affiche_hitbox:
                    rock.draw_hitbox(self.screen)

                rock.main(self.screen)

                



                
                
            for tornado in self.tornados:

                if self.affiche_hitbox:
                    tornado.draw_hitbox(self.screen)


                
                tornado.main(self.screen)   
                if tornado.detect_collision(self.rover_group):
                    self.did_lose = True 
                if self.did_lose or self.did_win:
                    tornado.allowed_to_move = False
                
            if self.did_win:
                self.screen.blit(self.victory_message,  (400, 200))
                self.screen.blit(self.victory_message_bas, (300, 250))
                self.is_game_over = True
                        
                
            if self.did_lose:
                self.screen.blit(self.losing_message, (400, 200))
                self.is_game_over = True
               
            self.affiche_level = self.calibri.render('Level : %s' % self.current_level, True, (0,0,0))
            
            self.screen.blit(self.affiche_level, (0,0))
            
            pygame.display.flip()
            
            
            
        self.clock.tick(60)
