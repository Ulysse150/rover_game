from object import*
from variables import*

class Rover(Object):
    
    def __init__(self, path, x, y, largeur, hauteur):
        Object.__init__(self, path, x, y, largeur, hauteur)
        self.original_image = self.image
        
        self.image_right = self.original_image
        self.image_up = pygame.transform.rotate(self.original_image, 90)
        self.image_down = pygame.transform.rotate(self.original_image, -90)
        self.image_left = pygame.transform.flip(self.original_image, True, False)
        
        self.images = {'right':self.image_right,
                      'left':self.image_left,
                       'down':self.image_down,
                       'up' : self.image_up 
            
        }
        
        
        self.rect_horizontal = self.rect.copy()
        self.rect_vertical = pygame.Rect(self.x, self.y, self.hauteur, self.largeur)
        
        self.moving_speed_x = rover_speed
        self.moving_speed_y = rover_speed
        
        
        self.speed_x = 0
        self.speed_y = 0
        self.direction = 'right'
        
    def get_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT]:
            self.direction = 'right'
            self.speed_x = self.moving_speed_x
            self.speed_y = 0
            self.rect = self.rect_horizontal
            
        elif pressed[pygame.K_LEFT]:
            self.direction = 'left'
            self.speed_x = -1* self.moving_speed_x
            self.speed_y = 0
            self.rect = self.rect_horizontal
            
        elif pressed[pygame.K_UP]:
            self.direction = 'up'
            self.speed_y =-1* self.moving_speed_y
            self.speed_x = 0
            self.rect  = self.rect_vertical
            
        elif pressed[pygame.K_DOWN]:
            self.direction = 'down'
            self.speed_y = self.moving_speed_y
            self.speed_x = 0
            self.rect  = self.rect_vertical
        
        else:
            self.speed_x = 0
            self.speed_y = 0
        
    def update(self):
        self.old_position = [self.x, self.y]
        if self.allowed_to_move:
            self.get_input()
            self.image = self.images[self.direction]
        
            self.x += self.speed_x
            self.y += self.speed_y
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        
        
        if not(self.is_on_screen()):
            self.x=self.rect.x = self.old_position[0]
            self.y =self.rect.y = self.old_position[1]
            
            
        
    