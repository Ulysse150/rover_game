import pygame
from object import Object
from variables import*


class Flag(Object):
    
    def __init__(self, x, y, largeur, hauteur):
        Object.__init__(self, flag_path, x, y, largeur, hauteur)
        self.images = self.import_folder('Assets/flag')
        
        self.index_max = len(self.images) -1
        self.index = 0
        self.animation_speed = animation_speed
        
    def animate(self):
        if self.index +1 > self.index_max:
            self.index = 0
        else:
            self.index += self.animation_speed
            
        self.image = self.images[int(self.index)]
        
    def update(self):
        self.animate()

        
    