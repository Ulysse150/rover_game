import pygame
from object import Object
from variables import*


class Tornado(Object):
    def __init__(self, x, y, behaviour, speed):
        Object.__init__(self,sandstorm_path, x,y,110, 120)
        self.movement_speed = speed
        self.behaviour = behaviour
        self.allowed_to_move = True
        
        if self.behaviour == 'horizontal':
            self.speed_x = self.movement_speed
            self.speed_y =0
        else:
            self.speed_y = self.movement_speed
            self.speed_x = 0
            
        
    def update(self):
        if self.allowed_to_move:
            if self.behaviour == 'horizontal':
                if self.rect.right >= largeur_ecran:
                    self.speed_x = self.movement_speed *-1
                if self.rect.left <=0:
                    self.speed_x = self.movement_speed
                    
            elif self.behaviour == 'vertical':
                if self.rect.top <=0:
                    self.speed_y = self.movement_speed
                elif self.rect.bottom >= hauteur_ecran:
                    self.speed_y = self.movement_speed *-1
            
            
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            
            