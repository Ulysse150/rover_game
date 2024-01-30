import pygame
import sys
from os import*
from variables import*

class Object(pygame.sprite.Sprite):
    
    def __init__(self, path, x,y, largeur, hauteur):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (largeur, hauteur))
        self.largeur = largeur
        self.hauteur = hauteur
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.largeur, self.hauteur)
        self.allowed_to_move = True
        
    def show(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_hitbox(screen)
        
    def main(self, screen):
        #self.draw_hitbox(screen)
        self.update()
        self.show(screen)
        
    def draw_hitbox(self, screen):
        pygame.draw.line(screen, (255,0,0), self.rect.topleft, self.rect.topright )
        pygame.draw.line(screen, (255,0,0), self.rect.topright, self.rect.bottomright )
        pygame.draw.line(screen, (255,0,0), self.rect.bottomright, self.rect.bottomleft )
        pygame.draw.line(screen, (255,0,0), self.rect.topleft, self.rect.bottomleft)
        
    def detect_collision(self, group):
        for lutin in group:
            if pygame.sprite.collide_rect(self, lutin):
                return True
        return False
    

    def import_folder(self, path):
        surface_list=[]
        for _ ,__,img_files in walk(path):
            for img in img_files:
                full_path = path+'/'+img
                #print(full_path)
                image = pygame.image.load(full_path)
                image = pygame.transform.scale(image, (self.largeur, self.hauteur))
                surface_list.append(image)
            
        return surface_list
        

    def is_on_screen(self):
        return self.rect.left > 0 and self.rect.right < largeur_ecran and self.rect.top >0 and self.rect.bottom < hauteur_ecran
        
    def update(self):
        #la boucle de l'objet dépendra de ce qu'il est
        #le code ne sera pas le même si l'objet est le joueur, un ennemi, une destination
        pass
    
class Rocher(Object):
    def __init__(self, x,y):
        Object.__init__(self, rock_path, x, y, 90, 80)
        